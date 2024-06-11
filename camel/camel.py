
def main():
    # Demander à l'utilisateur le nom d'une variable en cas de chameau
    camel_case = input("Entrez le nom d'une variable en cas de chameau : ")

    # Convertir le nom de variable en cas de chameau en cas de serpent
    snake_case = convert_to_snake_case(camel_case)

    # Afficher le nom de variable en cas de serpent
    print("En cas de serpent :", snake_case)

def convert_to_snake_case(camel_case):
    snake_case = ""
    for char in camel_case:
        # Si le caractère est en majuscule, ajoutez un trait de soulignement suivi de sa version minuscule
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    # Si le premier caractère est un trait de soulignement, supprimez-le
    if snake_case.startswith("_"):
        snake_case = snake_case[1:]
    return snake_case

if __name__ == "__main__":
    main()
