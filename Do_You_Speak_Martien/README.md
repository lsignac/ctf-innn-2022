# Do you Speak Martian

Nos analystes en crypto-linguistique ne sont pas venus à bout de ce code.

Pouvez vous les aider ?

Ce defi est recommandé pour l'epreuve finale

![](screenshot.png)

## Résolution

Le décalage des plans CMY ne sert à rien à part brouiller les pistes.
On se concentre sur les symboles magenta.

Le répétition du modif `pvpvpv` du début rappelle `NNN`, ce qui laisse penser qu'on a 
deux symboles pour une lettre. Il n'y a pas beaucoup de symbols différerents. 
C'est peut être de l'ascii hexa.
Si c'est le cas, on identifie `pspvpvpv1t` à `INNN{` donc `494E4E4E7B`. Et le dernier
symbole `1l` à `}` donc `7D`.

Il reste à essayer toutes les combinaisons, et voir ce que ça donne.
On procède à taton en essayant de repérer du texte qui a un sens et qui ne contient pas de caractère
non imprimable. Une fois repéré la châine `t0_c0nvert`, on n'affiche plus que les solutions
qui contiennent cette chaîne.

Flag : `INNN{HoW_t0_C0nvert_Hex4#1_9}`

