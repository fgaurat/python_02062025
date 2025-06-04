from Carre import Carre
from Cercle import Cercle

def main():
    c = Carre(2)
    print(c.cote)
    print(c.surface)
    c.cote = 12
    print(c.surface)
    print(c)
    print(50*'-')
    ce = Cercle(12)
    # print(ce.surface)

if __name__=='__main__':
    main()
