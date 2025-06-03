
def main():
    a=2
    b=3
    c = a/b
    # result = f"{a=} / {b=} = {c*100=:.2f}%"
    result = f"{a=} / {b=} = {c=:.2%}"
    print(result)

    s = "{} / {} = {:.2%}".format(a,b,c)
    print(s)
    
    l = [a,b,c]

    s = "{0} / {1} = {2:.2%}".format(*l)
    print(s)

    d = {
        "val_1":a,
        "val_2":b,
        "val_3":c
    }

    s = "{a} / {b} = {c:.2%}".format(a = d["val_1"],b = d["val_2"],c = d["val_3"])
    print(s)

    s = "{val_1} / {val_2} = {val_3:.2%}".format(val_1 = d["val_1"],val_2 = d["val_2"],val_3 = d["val_3"])
    print(s)
    
    s = "{val_1} / {val_2} = {val_3:.2%}".format(**d)
    print(s)


if __name__=='__main__':
    main()
