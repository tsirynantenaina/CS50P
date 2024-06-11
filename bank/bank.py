# bank.py

def main():
    # Demander à l'utilisateur d'entrer un message d'accueil
    greeting = input("Entrez un message d'accueil : ")

    # Supprimer les espaces de début et convertir en minuscules
    greeting = greeting.strip().lower()

    # Vérifier les conditions spécifiées
    if greeting.startswith("bonjour"):
        print("$0")
    if greeting.startswith("Hello"):
        print("$0")
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

# Appeler la fonction main si ce fichier est exécuté en tant que script
if __name__ == "__main__":
    main()
