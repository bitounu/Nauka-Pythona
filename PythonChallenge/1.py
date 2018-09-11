import string
import sys
alf = list(string.lowercase)
print alf
#tekst = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
tekst = "www.pythonchallenge.com/pc/def/map.html"
print tekst
for i in tekst:
    if i not in (" ", ".", "'", "(", ")", "/"):
        indx = alf.index(i)
        if indx >= 24:
            sys.stdout.write(alf[indx+2-26])
        else:
            sys.stdout.write(alf[indx+2])
    else:
        sys.stdout.write(i)
print ""
