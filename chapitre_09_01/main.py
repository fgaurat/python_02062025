from Carre import Carre

def main():
    c = Carre(2)
    print(c.cote)
    print(c.surface)
    c.cote = 12
    print(c.surface)
    print(c)

if __name__=='__main__':
    main()
