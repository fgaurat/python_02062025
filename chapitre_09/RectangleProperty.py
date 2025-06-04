class Rectangle:

    def __init__(self, longueur: int, largeur: int):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self) -> int:
        return self.__longueur

    def set_longueur(self, longueur: int) -> None:
        assert longueur > 0

        self.__longueur = longueur

    def get_largeur(self) -> int:
        return self.__largeur

    def set_largeur(self, largeur: int) -> None:
        assert largeur > 0
        self.__largeur = largeur

    def get_surface(self):
        return self.__longueur * self.__largeur

    def __str__(self) -> str:
        return f"{__class__.__name__} {self.__longueur=}, {self.__largeur=}"

    def __eq__(self, value):
        return self.__longueur == value.__longueur and self.__largeur == value.__largeur

    longueur = property(
        get_longueur,
        set_longueur,
        doc="propriété longueur")

    largeur = property(
        get_largeur,
        set_largeur,
        doc="propriété largeur")

    surface = property(get_surface, doc="propriété surface")
