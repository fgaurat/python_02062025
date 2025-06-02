# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))



for i in range(10):
    print(i)

print(50*'-')
for i in range(5,10,2):
    print(i)


a = list(range(12))
print(a)

print(50*'-')

l = [10,20,30,40,50,60]
to_find = 30

found = False
for value in l:
    print(value)
    if value == to_find:
        print("found")
        break
else:
    print("not found")
    

# if found:
#     print("found")
# else:
#     print("not found")


a = 12

if True:
    pass

print(a)