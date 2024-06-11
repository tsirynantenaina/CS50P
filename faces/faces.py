# faces.py

def convert(text):
    """
    Remplace :) par 🙂 et :( par 🙁 dans la chaîne de caractères donnée.

    :param text: Chaîne de caractères à convertir.
    :return: Chaîne de caractères avec les émoticônes converties.
    """
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    """
    Demande une entrée à l'utilisateur, convertit les émoticônes et affiche le résultat.
    """
    user_input = input("Veuillez entrer une phrase : ")
    converted_input = convert(user_input)
    print(converted_input)

# Appeler la fonction main si ce fichier est exécuté en tant que script
if __name__ == "__main__":
    main()
