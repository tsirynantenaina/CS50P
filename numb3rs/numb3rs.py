import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Vérifier si l'adresse est dans le bon format avec une expression régulière
    pattern = r'^\d+\.\d+\.\d+\.\d+$'
    if not re.match(pattern, ip):
        return False

    # Diviser l'adresse en segments
    segments = ip.split('.')

    # Vérifier chaque segment pour s'assurer qu'il est entre 0 et 255
    for segment in segments:
        if not segment.isdigit():
            return False
        if not 0 <= int(segment) <= 255:
            return False

    return True

if __name__ == "__main__":
    main()
