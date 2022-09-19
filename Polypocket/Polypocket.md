# Polypocket

## Énoncé

*Encore un spam !*

Il faut vraiment que nos services mettent à jour notre serveur de messagerie.

[spam.eml](spam.eml)

## Solution

Dans le spam.eml, on trouve une pièce jointe :

```
Content-Type: application/pdf; name="prize.pdf"
Content-Transfer-Encoding: base64
Content-Disposition: inline; filename="prize.pdf"
Content-ID: <ae0357e57f04b8347f7621662cbe3855.pdf>
UEsDBBQAAAAAABkIBFW+[...]
```

On extrait la pièce jointe, et on ouvre le PDF, qui affiche : 
![pdf](pdf.png)

C'est un indice. Mais en regardant le type du fichier, on a une surprise :
```console
$ file prize.pdf 
prize.pdf: Zip archive data, at least v2.0 to extract, compression method=store
```

C'est un fichier polyglot, qui est à la fois un PDF et une archive ZIP. Et même une archive JAR si l'on en croit le contenu :

```console
$ unzip -t prize.pdf
Archive:  prize.pdf
    testing:                          OK
    testing: META-INF/                OK
    testing: META-INF/MANIFEST.MF     OK
    testing: PDF/Main.class           OK
No errors detected in compressed data of prize.pdf.
```

Tentons de le lancer ?

```console
$ java -jar prize.pdf
VAAA{C0ylty0ty0g_S1y3_X4a_O3_Qnatre0hf}
```

Ça ressemble à un flag, mais pas tout à fait. On se souvient que le PDF évoquait ROT13, donc :

```console
$ java -jar prize.pdf | tr "A-Za-z" "N-ZA-Mn-za-m"
INNN{P0lygl0gl0t_F1l3_K4n_B3_Danger0us}
```