from Rectangle import Rectangle
from DataRectangle import DataRectangle

def oldmain():
    r = Rectangle(2,3)
    # print(r.__largeur)
    # print(r.__longueur)
    # r._largeur = 1000
    # print(r._Rectangle__largeur)
    # print(r._Rectangle__longueur)

    # print(r.get_longueur()) # 2
    # r.set_longueur(12)
    # print(r.get_longueur()) # 12
    # print(r.get_surface()) # 36

    str_r = str(r)
    print(str_r)

    print(50*'-')
    r = Rectangle(2,3)
    r1 = Rectangle(2,3)
    
    if r==r1:
        print("ok")
    else:
        print("ko")
    
    print(50*'-')
    r = Rectangle(2,3)
    r.longueur = 12
    print(r.longueur)
    # r.longueur = -12
    # print(r.longueur)
    print(50*'-')

    r = DataRectangle(12,2)
    print(r.longueur)
    print(r.largeur)
    print(r.surface)

def main():
    r = Rectangle(2,3)
    r1 = Rectangle(2,3)
    print(r.get_cpt()) # 2 
    print(Rectangle.get_cpt()) # 2 
    
    print(50*'-')
    r = Rectangle.buildFromStr("2;3")


if __name__=='__main__':
    main()
