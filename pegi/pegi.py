import itertools

def tonum(stri, vals):
    v = 0
    for k in stri:
        v  = v * 2 + vals[k]
    return v


def decode(stri, chiffres):
    s = ""
    k = 8
    for p in range(0, len(stri), k):
        v = tonum(stri[p:p+k], dict(zip(chiffres, (0, 1))))
        s = s + chr(v)
    return s

txt_ = """\
01100101 10010110
01100101 10101001
01100101 10101001
01100101 10101001
01101010 10011010
01100101 01011001
01101001 10100101
01101010 01100110
01011010 01011010
01100110 10101010
01100101 10100110
01011010 01010101
01101001 10101010
01101001 10101001
01101010 10100110

"""

txt = "".join([_ for _ in txt_ if _ in '01'])

res = []
for a, b in zip(txt[::2], txt[1::2]): # Manchester !
    if a + b == "01":
        res.append("0")
    elif a + b == "10":
        res.append("1")
    else:
        print("MERDE...")

print(decode("".join(res), "01"))
