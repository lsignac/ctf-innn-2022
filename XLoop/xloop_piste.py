from pathlib import Path
import string
import base64
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

def reverse(val, k):
    s = f"{val:08b}"[-k:][::-1]
    return int(s, 2)

def smartprint(stri, f, larg=80):
    s = []
    sm = []
    for k, c in enumerate(stri, 1):
        s.append(c)
        sm.append(f(c))
        if k % larg == 0 or k == len(stri):
            print("".join(s))
            print("".join(sm))
            s = []
            sm = []
    return


data1 = Path("Charlie.txt").read_bytes()
data2 = base64.a85decode(data1)
data = data2
data_s = data.decode("latin1")
c = Counter(list(data))
print(Counter(data_s))
print()

#cs = sorted(c.items(), key=lambda x: x[1], reverse=True)
#csl = [(chr(a), a, b) for a, b in cs]

smartprint(data_s,
           lambda x: "|" if x in string.digits else " ", 80)
print()
smartprint(data_s,
           lambda x: "|" if x in string.ascii_letters else " ", 80)
print()
smartprint(data_s,
           lambda x: "|" if x not in (string.ascii_letters  + string.digits) else " ", 80)

print()
print("Plage octets")
print(min(data), max(data))
print("Absents de cette plage : ",
      set([chr(a) for a in range(min(data), max(data) + 1)]) - set(data_s),
      "Chelou non ?")


## Combiner 2 à 2:
lst = []
for a, b in zip(data[0::2], data[1::2]):
    lst.append((a -33)^(b -33) + 33)
res = bytes(lst)
print(res.decode("latin1"))
print("------------------------------")

## Combiner 2 à 2:
lst = []
for a, b in zip(data[:], data[::-1]):
    lst.append((a)^(b) + 33)
res = bytes(lst)
print(res.decode("latin1"))
print("------------------------------")

## bits à l'envers...
lst = []
for a in data:
    lst.append(reverse(a, 7))
res = bytes(lst)
print(res.decode("latin1"))
print("------------------------------")

## bits à l'envers et xor
lst = []
for a, b in zip(data[::2], data[1::2]):
    lst.append(reverse(a, 7) ^ b)
res = bytes(lst)
print(res.decode("latin1"))
print("------------------------------")

## Flot de bits
lst = []
lst2 = []
for k in data:
    lst.extend(int(_) for _ in f"{k:07b}")

#plt.imshow(np.array(lst).reshape((7, 38**2*2*2)))
plt.imshow(np.array(lst).reshape((38*2*2*2,7)).transpose())
#plt.imshow(np.array(lst).reshape((8, 38*2*2*2)))
#plt.imshow(np.array(lst).reshape((38*2*2*2, 8)).transpose())
plt.show()
#
txt = """\
0NgDV90$*!=X63j-#d3C4^r%Y:GR$*5r!7?:,=kQ2fD_p<Hg,i<B;g*;cGh@5rLMN@65Ya9OfPP2FVgt9.`bZ7kRdb.8XnC/ibR012o9`.P)rA.s*RT5XfrN85!T@0iLb=3DMFq6$H45;*7u53d)`03c72X7klN>F@\Ya89-:83G)&W4=,,E;`B#3@sBV9;e86W-7i[m<+p5D696o(8jP^N06B63?WBUA3C,2KAN`7)+Zhk`9.M_]8Mj7C2,#J_B0Tg<?:I^D4BY?Q>"1V[4Zt&?E%u61-mLHG=]TK#20j?s;-%UQE&]XD>9u(5=]&F$?Z.WD0J>":+\jgL84,0\A10&d?</I.5X\(A?nOi$=^O0X0I(R9.7$?p1ga6^"""
