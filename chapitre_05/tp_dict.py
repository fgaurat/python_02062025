d = {
    "name":"GAURAT",
    "firstname":"Fred",
    "age":49,
}

print(d['name'])
d['name'] = "MARTIN"
print(d['name'])

for k in d:
    print(k, d[k])

print(d.items())

items = list(d.items())
print(items[0])
key,value = items[0]


for key,value in d.items():
    print(key,value)

l = [10,20,30,40]
# for i in l:
for pos,i in enumerate(l):
    print(pos,i)