
def canBeEqual(s1, s2):
    
    para = ""
    parb =""
    impara = ""
    imparb = ""
    for x in range(4):
        if x % 2==0:
            para += s1[x]
            parb += s2[x] 
        else:
            impara += s1[x]
            imparb += s2[x]

    return sorted(para) == sorted(parb) and sorted(impara) == sorted(imparb)



print(canBeEqual(s1, s2))