def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Vérifier si la plaque commence par au moins deux lettres
    if len(s) < 2 or not s[:2].isalpha():
        return False

    # Vérifier si la plaque contient au maximum 6 caractères
    if len(s) > 6:
        return False

    # Vérifier si la plaque ne contient pas de chiffres au milieu
    if any(char.isdigit() for char in s[2:-1]):
        return False

    # Vérifier si le premier chiffre n'est pas 0
    if s[-1].isdigit() and s[-1] == '0':
        return False

    # Vérifier si aucun caractère n'est un point, espace ou signe de ponctuation
    if any(char in '. ,;:!?()[]{}' for char in s):
        return False

    return True

if __name__ == "__main__":
    main()
