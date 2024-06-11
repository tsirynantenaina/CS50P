import inflect

def main():
    # Créer une instance de inflect.engine
    p = inflect.engine()

    # Initialiser une liste pour stocker les noms
    names = []

    print("Enter names (Ctrl-D to end):")
    # Demander à l'utilisateur de saisir des noms jusqu'à EOF
    try:
        while True:
            name = input('Name:')
            names.append(name)
    except EOFError:
        pass

    # Formater et afficher le message d'adieu
    farewell_message = "Adieu, adieu, to " + p.join(names)
    print(farewell_message)

if __name__ == "__main__":
    main()
