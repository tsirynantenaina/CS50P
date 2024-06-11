
def main():
    # Demander à l'utilisateur la réponse à la grande question
    answer = input("Quelle est la réponse à la grande question de la vie, de l'univers et de tout ? ")

    # Convertir la réponse en minuscules pour comparaison
    answer_lower = answer.lower()

    # Vérifier si la réponse est correcte
    if answer == "42" or answer_lower == "forty-two" or answer_lower == "forty two":
        print("Yes")
    else:
        print("No")

# Appeler la fonction main si ce fichier est exécuté en tant que script
if __name__ == "__main__":
    main()
