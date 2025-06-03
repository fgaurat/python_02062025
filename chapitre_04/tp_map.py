

def old_mult2(values):
    r = []
    for i in values:
        r.append(i*2)
    
    return r


def mult2(i):
    return i*2

l = [10,20,30,40,50]
# m=mult2(l)

m = list(map(lambda i:i*2,l))
print(m) # [20,40,60,80,100]
