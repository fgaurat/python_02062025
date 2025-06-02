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
