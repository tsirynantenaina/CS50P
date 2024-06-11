import sys
import os
import csv
from tabulate import tabulate

def main():
    # Vérifier le nombre d'arguments de ligne de commande
    if len(sys.argv) != 2:
        sys.exit("Usage: python pizza.py FILENAME")

    # Récupérer le nom du fichier
    filename = sys.argv[1]

    # Vérifier que le fichier se termine par .csv
    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    # Vérifier que le fichier existe
    if not os.path.isfile(filename):
        sys.exit("File does not exist")

    # Lire le fichier CSV et afficher le tableau
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            rows = [row for row in reader]
            print(tabulate(rows, headers, tablefmt="grid"))
    except Exception as e:
        sys.exit(f"Error reading file: {e}")

if __name__ == "__main__":
    main()
