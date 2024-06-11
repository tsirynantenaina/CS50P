
def main():
    # Constante de la vitesse de la lumière en mètres par seconde
    c = 300000000  # ou 3 * 10^8

    # Demander à l'utilisateur d'entrer la masse en kilogrammes
    mass = int(input("Veuillez entrer la masse (en kilogrammes) : "))

    # Calculer l'énergie en utilisant la formule E = mc^2
    energy = mass * c**2

    # Afficher l'énergie en Joules
    print(f"L'énergie équivalente est de {energy} Joules.")

# Appeler la fonction main si ce fichier est exécuté en tant que script
if __name__ == "__main__":
    main()
