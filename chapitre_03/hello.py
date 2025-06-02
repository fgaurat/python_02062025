import sys
import copy

print("Hello World")



the_world_is_flat = True
if the_world_is_flat:
    print("Be careful not to fall off!")


print("la fin")


p = r"c:\project\test\new"

print(p)

mult = """Ligne 01
Ligne 02
Ligne 03
Ligne 04
"""

print(mult)


a = 2
b = "deux"
print( str(a) + b)

a = 2
b = "3"
print( a + int(b))

print(50*'#')

a = 8
b = "deux"
print(b*a)


s = "Python"
print(s[0])
l = len(s)
print(s[l-1])
print(s[-3])

s = "Python"

print(s[1:3]) # [1:3[
print(s[1:4])

print(s[1:3])
print(s[3:5])

print(s[:3])
print(s[3:])

print(s[3:567])
# print(s[567]

print(50*'-')
squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[0])
print(squares[:4])
print(50*'-')

s = 5
print(hex(id(s)))
s = 6
print(hex(id(s)))

the_value = 6
print(hex(id(the_value)))


s = 342245342423534545632435435646
print(sys.getrefcount(s))
d = 342245342423534545632435435646
print(sys.getrefcount(s))

print(50*'-')
squares = [1, 4, 9, 16, 25]

squares.append(36)

print(50*"-")

squares = [1, 4, 9, 16, 25]
squares[0] = 1000
print(squares)
squares2 = squares
squares2[0] = 1
print(squares)
print(squares2)
# squares2 = squares[:]
squares2 = squares.copy()
squares[0] = 1000
print(squares)
print(squares2)
print(50*'-')

squares = [
    [1, 4], 
    [9, 16], 
    [25,36]
    ]

# import copy
squares2 = copy.deepcopy(squares)
squares[1][1] = 1000
print(squares2)


# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    breakpoint()
    a, b = b, a+b


