# Demander à l'utilisateur d'entrer un nombre
n = int(input("Enter n: "))

# Vérifier si le nombre est négatif
if n < 0:
    print("Invalid number")
else:
    fact = 1
    i = 1

    # Boucle pour calculer la factorielle
    while i <= n:
        fact = fact * i
        i = i + 1

    # Afficher le résultat
    print("Factorial =", fact)