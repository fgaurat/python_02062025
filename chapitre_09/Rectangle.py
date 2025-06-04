class Rectangle:

    __cpt:int=0

    def __init__(self, longueur: int, largeur: int):
        self.__longueur = longueur
        self.__largeur = largeur
        Rectangle.__cpt+=1

    @classmethod
    def buildFromStr(cls,value:str):
        # v = value.split(";") # ["2","3"]
        v = [int(a) for a in value.split(";")] # [2,3]
        return cls(*v)

    @staticmethod
    def get_cpt()-> int:
        return Rectangle.__cpt
    

    @property
    def longueur(self) -> int:
        return self.__longueur

    @longueur.setter
    def longueur(self, longueur: int) -> None:
        assert longueur > 0
        self.__longueur = longueur

    @property
    def largeur(self) -> int:
        return self.__largeur

    @largeur.setter
    def largeur(self, largeur: int) -> None:
        assert largeur > 0
        self.__largeur = largeur
    
    @property
    def surface(self):
        return self.__longueur * self.__largeur

    def __str__(self) -> str:
        return f"{__class__.__name__} {self.__longueur=}, {self.__largeur=}"

    def __eq__(self, value):
        return self.__longueur == value.__longueur and self.__largeur == value.__largeur
