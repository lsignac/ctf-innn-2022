# Interdit aux Humains

Nous avons reçu un code étrange.
Pouvez vous l'analyser et l'exécuter ?

[Fichier fourni](code.txt)

## Résolution

Le fichier contient une chaîne bzippée, puis encodée en base64.
La chaîne en question est un programme Python, qui règle une variable 
`complex` à une certaine chaîne de caractères.

Cette chaîne n'est pas un programme dans un [langage ésotérique](https://esolangs.org/wiki/Main_Page) mais simplement le flag à afficher d'une certaine manière. Les indices permettant de s'en apercevoir : 
- toutes les occurrences sauf en début et fin de ligne de `@` vont par paire. Probablement que ça ne sert à rien (pas économe en caractères)
- si on supprime les `@`, on a une vague impression de distinguer un truc, et il y a pile 7 lignes (comme certains afficheurs à led)
- pour avoir une image plus claire, on cherche à remplacer les deux caractères restants `{}` par des caractères plus contrastés, comme ` ` et `#`

Flag : `INNN{PL4y_W1th_D00M}`
