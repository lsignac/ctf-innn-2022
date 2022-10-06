# Qui est Qui ?

Des tentatives de connexion à nos serveurs de base de données clients ont été observées.

Trouvez le coupable !

Le flag est sous le format INNN{login_du_coupable}

Fichier fourni : [log.tar.gz](log.tar.gz)

## Solution

On est face à fichier de log Unix, qui contient de nombreuses erreurs d'authentification SSH. On va commencer par supprimer le SSH pour voir ce qui reste :

```console
$ grep -v sshd auth.log 
Jul 22 14:31:55 ubt-server sudo: pam_unix(sudo:session): session closed for user root
Jul 22 14:38:44 ubt-server systemd-logind[816]: New session 9 of user alex.
Jul 22 14:38:48 ubt-server systemd-logind[816]: Session 9 logged out. Waiting for processes to exit.
Jul 22 14:38:48 ubt-server systemd-logind[816]: Removed session 9.
Jul 22 15:17:01 ubt-server CRON[32451]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)
Jul 22 15:17:01 ubt-server CRON[32451]: pam_unix(cron:session): session closed for user root
```

Intéressant, il ne reste pas grand chose ! On voit une session qui a fonctionné. Regardons d'un peu plus près cet utilisateur `alex`:

```console
$ grep " alex " auth.log 
Jul 22 14:38:23 ubt-server sshd[7866]: Failed password for alex from 192.168.1.13 port 37284 ssh2
Jul 22 14:38:23 ubt-server sshd[7867]: Failed password for alex from 192.168.1.13 port 37286 ssh2
Jul 22 14:38:23 ubt-server sshd[7866]: Disconnected from authenticating user alex 192.168.1.13 port 37284 [preauth]
Jul 22 14:38:23 ubt-server sshd[7867]: Disconnected from authenticating user alex 192.168.1.13 port 37286 [preauth]
Jul 22 14:38:44 ubt-server sshd[7956]: Accepted password for alex from 192.168.1.13 port 37422 ssh2
Jul 22 14:38:48 ubt-server sshd[8209]: Disconnected from user alex 192.168.1.13 port 37422
```

On voit que cet utilisateur a réussi à se connecter à 14:38:44. Y'a-t-il quelqu'un d'autre qui est parvenu ?

```console
$ grep "Accepted password" auth.log 
Jul 22 14:38:44 ubt-server sshd[7956]: Accepted password for alex from 192.168.1.13 port 37422 ssh2
```

Non, c'est donc notre homme ! `INNN{alex}`


