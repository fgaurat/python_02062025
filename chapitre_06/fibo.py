# Fibonacci numbers module




def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


def show_a():
    global a
    print(a)
    if True:
        a=1000



def main():
    pass

if __name__=='__main__':
    main()
