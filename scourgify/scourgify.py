import sys
import csv

def main():
    # Vérifier le nombre d'arguments de ligne de commande
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py input.csv output.csv")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, mode='r') as infile:
            reader = csv.DictReader(infile)
            data = []
            for row in reader:
                last, first = row['name'].split(", ")
                house = row['house']
                data.append({'first': first, 'last': last, 'house': house})

        with open(output_file, mode='w') as outfile:
            fieldnames = ['first', 'last', 'house']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)

    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

if __name__ == "__main__":
    main()
