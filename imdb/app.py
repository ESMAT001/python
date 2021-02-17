def _readLine(data):
    next(data)
    for line in data:
        yield line.split()[:2]

def _max(gen):
    m=0
    name=None
    for x in gen:
        temp=float(x[1])
        if temp>m:
            m=temp
            name=x[0]
    else: 
        return name,m

data=open('./data.tsv','r')

gen=_readLine(data)
print(_max(gen))

data.close()