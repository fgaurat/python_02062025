def f(i=5):
    print(i)

# Avant modification
f()  # Affiche 5

# Modification de la valeur par défaut
f.__defaults__ = (6,)

# Après modification
f()  # Affiche 6