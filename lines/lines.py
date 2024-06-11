import sys
import os

def main():
    # Vérifier le nombre d'arguments de ligne de commande
    if len(sys.argv) != 2:
        sys.exit("Usage: python lines.py FILENAME")

    # Récupérer le nom du fichier
    filename = sys.argv[1]

    # Vérifier que le fichier se termine par .py
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    # Vérifier que le fichier existe
    if not os.path.isfile(filename):
        sys.exit("File does not exist")

    # Compter les lignes de code
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except Exception as e:
        sys.exit(f"Error reading file: {e}")

    loc = count_lines_of_code(lines)
    print(loc)

def count_lines_of_code(lines):
    loc = 0
    for line in lines:
        stripped_line = line.strip()
        # Ignorer les lignes vides et les commentaires
        if stripped_line and not stripped_line.startswith("#"):
            loc += 1
    return loc

if __name__ == "__main__":
    main()
