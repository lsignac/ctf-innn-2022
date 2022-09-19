import itertools
import string

# Super chiant à saisir ça.... 
code = "pspvpvpv1tp6rnu1un1pcounpccorv1rru1j1punp6ru16cpjcchuncs1l"

code = code.translate(str.maketrans("psv1tl", "49E7BD"))

adechiffrer = "".join(sorted(set(code) - set("psv1tl49E7BD")))
##
reste = "01235681CF" #0123456789ABCDEF"


for essai in itertools.permutations(reste, len(adechiffrer)):
    dictrans = str.maketrans(adechiffrer, "".join(essai))
    dictransprint = {chr(k): chr(v) for k, v in dictrans.items()}
    res = code.translate(dictrans)
    resultat = bytes.fromhex(res)
    try:
        resustr = resultat.decode("ascii")
    except UnicodeDecodeError:
        pass
    else:
        # Un peu de devinette...
        if "t0_C0nvert" in resustr or "t0_c0nvert" in resustr:
            print(resustr)
            # print(dictransprint)


