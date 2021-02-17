def fn(x):
    if x in ")]}":
        return chr(ord(x)-2) if x in "]}" else chr(ord(x)-1)
    else:
        return x
def are_braces_closed(txt):
    braces="{[()]}"
    txt = [x for x in txt if x in braces]
    if len(txt)%2!=0:
        return False
    txt=list(map(fn,txt))
    x=len(txt)
    for i in range(len(txt)//2):
        if txt[i]!=txt[x-1:x-2:-1][0]:
            return False
        x-=1
    else:
        return True

res=are_braces_closed("{()[]}")
print(res)
