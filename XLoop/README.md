# X-Loop

Charlie, notre expert cryptographe, a développé un mode de chiffrement robuste, sans clé partagée ou asymetrique, pour transmettre nos messages en toute sécurité.

Bien que Charlie ai un ego surdimensionné et soit sûr de lui, nous voulons valider l'usage de ce nouveau chiffrement pour le chiffrage d'un devis confidentiel pour un de nos clients 😉

Pouvez vous déchiffer ce message ?

[Charlie.txt](Charlie.txt)

## Solution

L'analyse des fréquences de la chaîne contenue dans `Charlie.txt` montre que les codes ASCII des caractères sont compris entre 33 et 117.
Ceci oriente vers un encodage en base85 (https://www.dcode.fr/code-ascii-85).
Une fois cette première chaîne décodée, on obtient une seconde chaîne mais dont les codes ASCII des caractères sont compris entre 33 et 122 :
```
0Y9rK9X#Y$?7%p_-=bg1O2thA1n=N38v7oVRUw0KU:0IST;<A63-a;",Lc*U6Ew`K-JvG.U!)Pn:.9/#2p:b*,'M+t3`@Ey.HKgy1SLK9N5>AwR^Q<Y-:v#;:n@NG1+ytH@CHr-/9fOG<%uMS7zbcx.cSeA<&,d@ThpKB:3WJA@a/t:4_UGy9A,.e=?&!;>OK+1?I4PT5L*=g?ah^FO/<YLNZF<]==$*p1nU(#1TYVp75yv-QVonp83G[%3`YQ\Q_o0y0/-7!N33HC3'd(.3^V(0@DFU`.D0Y_9E0#qS)ADK4_UT
```
On remarque que les caractères `i`, `j`, `k`, `l` et `m` (entre autres) sont absents. L'idée est de « décaler l'alphabet » (comme un chiffre de César) pour que ces 5 lettres manquantes se retrouvent en fin, ce qui permettrait de retrouver un espaces des codes ASCII entre 33 et 117.
- La première idée a été de décaler tous les caractères... On obtenait 2 décalages valides : +12 et +13 (ROT-13 https://www.dcode.fr/chiffre-rot-13). Mais les chaînes décodées générait du binaire qui ne semblait pas exploitable
- La seconde idée a été de considérer que le décalage attendu était ROT-13, et que celui-ci ne devait s'appliquer que sur les lettres (minuscules et majuscules) ; cela permettait d'éjecter les codes ASCII supérieurs à 117 qui correspondent aux minuscules de l'alphabet !

```python
ROT13 = str.maketrans('ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
                      'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')

tmp = open('Charlie.txt').read()
print(f"{CIPHER}")
while not tmp.startswith("INNN"):
  tmp = base64.a85decode(tmp).decode().translate(ROT13)
  print(f"{tmp}")
```

Lancements successifs :

```
0NgDV90$*!=X63j-#d3C4^r%Y:GR$*5r!7?:,=kQ2fD_p<Hg,i<B;g*;cGh@5rLMN@65Ya9OfPP2FVgt9.`bZ7kRdb.8XnC/ibR012o9`.P)rA.s*RT5XfrN85!T@0iLb=3DMFq6$H45;*7u53d)`03c72X7klN>F@\Ya89-:83G)&W4=,,E;`B#3@sBV9;e86W-7i[m<+p5D696o(8jP^N06B63?WBUA3C,2KAN`7)+Zhk`9.M_]8Mj7C2,#J_B0Tg<?:I^D4BY?Q>"1V[4Zt&?E%u61-mLHG=]TK#20j?s;-%UQE&]XD>9u(5=]&F$?Z.WD0J>":+\jgL84,0\A10&d?</I.5X\(A?nOi$=^O0X0I(R9.7$?p1ga6^

0NgDY6W6^&<(&rB5tG<54#'>W5!2dk0emQ51j2_n8mZI$B0.P*/R'K?AlL$VARdE7E$["k9e:F,<*`1:3)O$qBOFeO,W&Ua=C$&P2.\jo2D&,l=CG/n@TQVh+[7bG2*alI1-Ai9/pTN-=t4eYF[IK80L[iK;_WJm@U)Y`2d.t3GVr2f1K%=24$HG31-[R7.naq96U>X2:Gm2b2DK/0DBq;C?8Oo0:N^5o;a3*6?VYlQ9fb+)=t0

0L9hPFZiGQ?VNU^,;1W*><G&11aP4iDDW^c?t;)=-[$dsG$Irp0ec%+4Z,hdG]Yc8D_tu`Gs$4K:K]hL5r;k6-[7KnG?oJJ6!?3=5@Zr2<]Y.l;)M*l:hP&80R5*F0lBo\A27M2Ak5ZW3EK3;>BV2?3d+Xf.PNbeB5fV61c7a$;G^4@<BhrlF?4A_Al^Z:4YM*

0NhUh=Z0_Z;H#/-4[<=;4%;^a4'#`q4#'i%:i\F)10Rp=5W1kg4Xb4q7l<hGBL=RN4]O'k5#j]l0NM7V?p@.I:bXD5AiCtl;0l)E1aFUq2_csUA99JH4[i"*:iL;*06^tc2`45SFECD+H?*7g:cgsI2*=/m

0L[oL6oTEF-9=@^>;ST";I`^;1K?Ce5r2M\3@6@:=(b&T5UnuP3A=H-5>H<&0IJJ`?TNC0+us7$4DmD\4$,!71/Tqg/g=RX;Cca//jr675X%ggE$me\EC;N[5<NQ

0R7)Q7m/&:?U[4@1EpHq3H8.N3Hd9&.6JtU,@*?090HZ?AgK0'.q_:jF"9sN<a@C;;,f2D67."]4E+dg.QU[@>X'c'=sdQ1F?<t

0lnmT="e_R@:3"t>9dK*9i5h)<'E#]:GX=`5s%1V+tRdf+ZNI]06DG/AO&mL<cp6*:Ko\?,>M&^1g;p

1f,oJ/i4n`F>[#_+ZDbBG>1#B3&NN;<'",f.!8H8/gkTr@X:Ih4^B[5>#AC&4[8

4C1f.4&ng5G@!7P0jZ7m854#G:K^(hF&.'c6omRm=].XMDKI=@

<^B#;HU;j^8i1^(?UZbiBLQMfBl[Q:@8LEQ<ag)u

INNN{Oh_W4it_R3cuRs1ve_3nCodIng}
```