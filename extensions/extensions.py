# extensions.py

def main():
    # Dictionnaire de mappage des extensions de fichiers aux types de médias
    media_types = {
        '.gif': 'image/gif',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.pdf': 'application/pdf',
        '.txt': 'text/plain',
        '.zip': 'application/zip'
    }

    # Demander à l'utilisateur de saisir le nom du fichier
    filename = input("Entrez le nom du fichier : ").strip().lower()

    # Extraire l'extension du fichier
    for ext in media_types:
        if filename.endswith(ext):
            print(media_types[ext])
            return

    # Si aucune correspondance trouvée, afficher la valeur par défaut
    print("application/octet-stream")

# Appeler la fonction main si ce fichier est exécuté en tant que script
if __name__ == "__main__":
    main()
