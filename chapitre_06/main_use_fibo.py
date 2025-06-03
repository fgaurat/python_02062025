import fibo as fb
from fibo import fib
import sys

# def fib(v):
#     print("local fib",v)

def main():
    # import fibo
    # fibo.fib(1000)
    # print(sys.argv)
    n =  int(sys.argv[-1])
    fb.fib(n)

    fib(n)

if __name__=='__main__':
    main()
