# Le meilleur de nos Parefeu

D'après une comparaison d'empreinte SHA1, la documentation sur notre nouveau pare feu a été falsifiée.

Pouvez vous le confirmer ?

[Fichier fourni](ZEDKAZED.pdf)

## Résolution

Il y a du texte en noir sur noir en haut à droite. Récupérable avec Inkscape par exemple.
On relève le texte : 

`$9$4zaGjn6CBIh7-QnCt1I-VbsYo.mT9pO8XjHmPn6lKMXVY24aGjqWLTFn6AtWLxd4JikmTF/q.9p0BSyYgoGHmApB`

C'est un mot de passe au format Juniper (?) (connais pas... j'ai cherché sur le net, 
le `$9$` du début invite à faire ça, ça rappelle les pass unix standars `$1$...`.)

C'est simplement un mode de stockage des passwords obfusqué. 
On peut lire la spec ou trouver un outil pour décoder :

- <https://github.com/mhite/junosdecode/blob/master/junosdecode.py>
- ou en ligne : <http://password-decrypt.com/>

Avec l'outil en ligne, on obtient le flag :
`INNN{W3ak_P4ssw0rd_1s_Us3less}`

