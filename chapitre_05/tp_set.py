s = {12,20,30,11,12,20,100}
s1 = {120,220,30,11,12,420,100}

print(s)
for i in s:
    print(i)

print(s - s1)
print(s | s1)
print(s & s1)
print(s ^ s1)


lines = [
    "Ligne01",
    "Ligne02",
    "Ligne02",
    "Ligne01",
    "Ligne03",
    "Ligne03",
    "Ligne01"
]

print(lines)
lines = list(set(lines))
print(lines)


