import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    # Utiliser une expression régulière pour trouver "um" en tant que mot indépendant
    matches = re.findall(r'\bum\b', s, re.IGNORECASE)
    return len(matches)

if __name__ == "__main__":
    main()
