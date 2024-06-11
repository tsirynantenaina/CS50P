def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):

    # Supprimer le symbole $ et convertir le reste en float
    return float(d.strip('$'))


def percent_to_float(p):
    # Supprimer le symbole % et convertir le reste en float, puis diviser par 100
    return float(p.strip('%')) / 100


# Appeler la fonction main si ce fichier est exécuté en tant que script
if __name__ == "__main__":
    main()
