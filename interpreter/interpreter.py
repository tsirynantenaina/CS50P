
def main():
    # Demander à l'utilisateur de saisir une expression arithmétique
    expression = input("Entrez une expression arithmétique (x y z) : ").strip()

    # Diviser l'expression en trois parties, en tenant compte de multiples espaces
    parts = expression.split()

    # Vérifier que nous avons bien trois parties
    if len(parts) != 3:
        print("Erreur : veuillez entrer l'expression sous la forme 'x y z' avec des espaces entre chaque partie.")
        return

    x, y, z = parts

    # Convertir les opérandes en entiers
    try:
        x = int(x)
        z = int(z)
    except ValueError:
        print("Erreur : x et z doivent être des entiers.")
        return

    # Effectuer l'opération arithmétique en fonction de l'opérateur
    if y == "+":
        result = x + z
    elif y == "-":
        result = x - z
    elif y == "*":
        result = x * z
    elif y == "/":
        result = x / z
    else:
        print("Opérateur non valide.")
        return

    # Afficher le résultat sous la forme d'une valeur à virgule flottante formatée à une décimale
    print(f"{result:.1f}")

# Appeler la fonction main si ce fichier est exécuté en tant que script
if __name__ == "__main__":
    main()
