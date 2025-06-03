def fib(n):    # write Fibonacci series less than n
    """Print a Fibonacci series less than n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


def fib2(n: int=12) -> list:
    """Return a Fibonacci series less than n."""
    a, b = 0, 1
    r = []
    while a < n:
        r.append(a)
        a, b = b, a+b

    return r


# Now call the function we just defined:
fib(2000)
print(fib.__doc__)
values = fib2(2000)
print(values)

values = fib2()
print(values)

print(50*'-')


def hello(name,first_name,age):
    print("Hello",name,first_name)


h = hello("GAURAT","Fred",49)

h = hello("GAURAT",first_name="Fred",age=49)
# h = hello(first_name="Fred", name="GAURAT",49)

print(50*'-')


def add(*l):
    """Renvoie la somme de la liste l"""
    print(l)
    a=0
    for i in l:
        # a =a +i
        a+=i
    
    return a


values = [10,20,30,40,50]
s = add(*values) # package ([10,20,30,40,50])
print(s)# 150

s = add(10,20,30,40,50)  # package (10,20,30,40,50)
print(s)



a,b,*c = 0,1,2,3,4,5

print(a)
print(b)


values = [10,20,30,40,50]
print(values) # [10,20,30,40,50]
print(*values,sep=";")

# convention passage de paramètre par position en nombre variable:  *args
# convention passage de paramètre par keywords en nombre variable:  **kwargs
def hello(**kwargs):
    print(kwargs)
    print(kwargs['name'])

hello(name="GAURAT",first_name="Fred",age=49)



def hello1(name,firstname,/):
    print(name,firstname)

def hello2(*,name,firstname):
    print(name,firstname)

hello1("toto","titi")
hello2(name="toto",firstname="titi")
hello2("toto","titi")

input()