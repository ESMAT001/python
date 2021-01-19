def commonCharacterCount(s1, s2):
    s2=list(s2)
    res=0
    for c in s1:
        s=''.join(s2)
        i=s.find(c)
        if i != -1:
            res+=1
            s2.pop(i)
    return res

commonCharacterCount("aabcc", "adcaa")