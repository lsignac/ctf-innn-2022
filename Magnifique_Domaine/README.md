# Énoncé

Le domaine `drri.sk` vient d'apparaître.

Cela semble augurer une nouvelle action de la part du Dr Risk.

Inspectez ce domaine en détail.

# Solution

```
> dig TXT drri.sk

; <<>> DiG 9.18.7 <<>> TXT drri.sk
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 63463
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
; COOKIE: 839f9193dc7e95de010000006337e87695cd8f1464824705 (good)
;; QUESTION SECTION:
;drri.sk.			IN	TXT

;; ANSWER SECTION:
drri.sk.		300	IN	TXT	"QXVzc2kgZmFjaWxlIHF1ZSAxIDIgMw=="

;; Query time: 89 msec
;; SERVER: 192.168.1.1#53(192.168.1.1) (UDP)
;; WHEN: Sat Oct 01 09:15:32 CEST 2022
;; MSG SIZE  rcvd: 109
```

```
echo QXVzc2kgZmFjaWxlIHF1ZSAxIDIgMw== | base64 -d
Aussi facile que 1 2 3
```

```
> dig TXT 1.drri.sk | grep ^..drri
1.drri.sk.		268	IN	TXT	"SU5OTntIMWQz"
> dig TXT 2.drri.sk | grep ^..drri
2.drri.sk.		300	IN	TXT	"X015X0Q0dDR"
> dig TXT 3.drri.sk | grep ^..drri
3.drri.sk.		300	IN	TXT	"fMW5fRE41fQ"
```

```
> echo SU5OTntIMWQzX015X0Q0dDRfMW5fRE41fQ | base64 -d
INNN{H1d3_My_D4t4_1n_DN5}base64: entrée incorrecte
```

Pb de padding ?

Flag : `INNN{H1d3_My_D4t4_1n_DN5}`
