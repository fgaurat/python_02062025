from collections import deque


l = [10,20,30,40,50]
l.append(60)
print(l)
last_value = l.pop()
print(last_value)
l.insert(0,-10)
print(l)

first_value =  l.pop(0)
print(first_value)
print(l)


d = deque(l)
print(d)


print(50*'-')

l = []
for i in range(0,100,10):
    l.append(i)
print(l)

l = list(map(lambda i:i*10,range(10)))
print(l)


l = [i for i in range(0,100,10)]
print(l)


lines = ["ligne 01","   ligne 02","   ligne 03   "]

clean_lines = [l.strip() for l in lines]
print(clean_lines)
lines = ["01","02","03"]
cast_to_int = [int(l) for l in lines]
print(cast_to_int)


a = 0
del a
print(a)