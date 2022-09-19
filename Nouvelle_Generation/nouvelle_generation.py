import itertools

def tonum(stri, vals):
    v = 0
    for k in stri:
        v  = v * 4 + vals[k]
    return v


def decode(stri, chiffres):
    s = ""
    for p in range(0, len(stri), 4):
        v = tonum(stri[p:p+4], dict(zip(chiffres, (0, 1, 2, 3))))
        s = s + chr(v)
    return s

txt_col = "RJRRBBJRVRRVRRJJRJBVBBVRJJRRVRVJRBBJBVRRJJRBVRJRRRRBBJVRJJRBVBVJRJRVJBRBVJRJJRRRRVJBRJJRBVRJVRBJBBVR"
txt_lig = txt_col[0::4] + txt_col[1::4] + txt_col[2::4] + txt_col[3::4]

for ordre in itertools.permutations("RVBJ", 4):
    s = decode(txt_lig, ordre)
    if "INNN" in s:
        print(s)


