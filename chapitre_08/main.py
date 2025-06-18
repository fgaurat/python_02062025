import traceback

def divi(a,b):
    if b==12:
        raise ArithmeticError('Division par 12 !')
    return a/b

def call_divi(a,b):
    r = 0
    try:
        print('OPEN LOG')
        r = divi(a,b)
    finally:
        print('CLOSE LOG')
    return r



def main():
    try:
        a = 2
        b = 12
        # b = int(input("b: "))
        c =call_divi(a,b)
    except ZeroDivisionError as e:
        print("ZeroDivisionError",e)
        traceback.print_exc()

    except TypeError as e:
        print("TypeError",e)
        traceback.print_exc()
    
    except ValueError as e:
        print("ValueError",e)
        traceback.print_exc()
    
    except Exception as e:
        print("Exception",e)
        traceback.print_exc()
    else:
        print("pas d'erreur")
    print("La suite")


if __name__=='__main__':
    main()
