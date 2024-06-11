import sys
import random
from pyfiglet import Figlet

def main():
    # Créer une instance de Figlet
    figlet = Figlet()

    # Vérifier les arguments de ligne de commande
    if len(sys.argv) == 1:
        # Aucun argument de ligne de commande, utiliser une police aléatoire
        fonts = figlet.getFonts()
        font = random.choice(fonts)
        figlet.setFont(font=font)
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
        # Vérifier si la police spécifiée est valide
        font = sys.argv[2]
        if font not in figlet.getFonts():
            sys.exit("Invalid font")
        figlet.setFont(font=font)
    else:
        sys.exit("Usage: figlet.py [-f | --font] <fontname>")

    # Demander à l'utilisateur de saisir un texte
    text = input("Input: ")

    # Afficher le texte avec la police spécifiée ou aléatoire
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
