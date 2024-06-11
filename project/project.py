import csv
import pyfiglet
import tabulate
import os

# Afficher le titre du programme
def afficher_titre():
    titre = pyfiglet.figlet_format("BULLETIN DE NOTES", font="slant")
    print(titre)

# Afficher le menu principal
def afficher_menu():
    print("\nMENU PRINCIPAL :")
    print("1. Liste des matières")
    print("2. Créer une matière")
    print("3. Supprimer une matière")
    print("4. Liste des étudiants")
    print("5. Créer un étudiant")
    print("6. Créer un bulletin de note")
    print("7. Voir un bulletin de note")
    print("8. Rangs des etudians")
    print("9. Quitter")

# Afficher la liste des matières avec leurs coefficients
def afficher_matieres():
    with open('matieres.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        matieres = []
        for row in reader:
            if len(row) >= 2:  # Vérification de la longueur de la ligne
                matieres.append([row[0].strip(), row[1].strip()])
        print("\nListe des matières avec leurs coefficients :")
        print(tabulate.tabulate(matieres, headers=['Matière', 'Coefficient'], tablefmt='grid'))


# Creer matiere
def creer_matiere():
    nom_matiere = input("Entrez le nom de la nouvelle matière : ")
    coefficient = int(input("Entrez le coefficient de la nouvelle matière (entier) : "))
    ajouter_matiere(nom_matiere, coefficient)

# Ajouter une matière
def ajouter_matiere(nom_matiere, coefficient):
    with open('matieres.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([nom_matiere, coefficient])
    print(f"La matière '{nom_matiere}' avec le coefficient {coefficient} a été ajoutée avec succès.")

def supprimer_matiere():
    nom_matiere = input("Entrez le nom de la matière à supprimer : ")
    matiere_existante = False
    # Vérifier si la matière existe dans le fichier
    with open('matieres.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for line in reader:
            if line and line[0].strip() == nom_matiere:
                matiere_existante = True
                break
    if not matiere_existante:
        print(f"La matière '{nom_matiere}' n'existe pas.")
        return
    # Supprimer la matière du fichier
    with open('matieres.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        lines = [line for line in reader if line and line[0].strip() != nom_matiere]
    with open('matieres.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(lines)
    print(f"La matière '{nom_matiere}' a été supprimée avec succès.")
    afficher_matieres()

# Afficher la liste des étudiants
def afficher_etudiants():
    with open('etudiants.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        etudiants = []
        for row in reader:
            if len(row) >= 2:  # Vérification de la longueur de la ligne
                etudiants.append([row[0].strip(), row[1].strip()])
        print("\nListe des étudiants :")
        print(tabulate.tabulate(etudiants, headers=['Matricule', 'Nom'], tablefmt='grid'))

# Creer étudiant
def creer_etudiant():
    while True:
        try:
            matricule = int(input("Entrez le matricule de l'étudiant (entier) : "))
            break
        except ValueError:
            print("Erreur : le matricule doit être un nombre entier.")
    nom = input("Entrez le nom de l'étudiant : ")
    ajouter_etudiant(matricule, nom)

# Ajouter un étudiant
def ajouter_etudiant(matricule, nom):
    with open('etudiants.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([matricule, nom])
    print(f"L'étudiant '{nom}' avec le matricule {matricule} a été ajouté avec succès.")

# Créer un bulletin de note
def bulletin_de_note():

    # Demande le matricule de l'étudiant
    matricule = input("Entrez le matricule de l'étudiant : ")

    # Vérifie si l'étudiant existe dans la liste des étudiants
    with open('etudiants.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        etudiants = []
        nom_etudiant = None
        for row in reader:
            if len(row) >= 2:  # Vérification de la longueur de la ligne
                etudiants.append([row[0].strip(), row[1].strip()])
                if row[0].strip() == matricule:
                    nom_etudiant = row[1].strip()

    if nom_etudiant is None:
        print("Matricule inconnu. Veuillez saisir un matricule existant.")
        return

    # Demande confirmation de l'étudiant
    confirmation = input(f"Confirmez que vous voulez créer le bulletin pour l'étudiant {nom_etudiant} (oui/no) : ")
    if confirmation.lower() not in ['oui', 'o', 'y']:
        print("Annulation de la création du bulletin.")
        return

    # Crée le fichier CSV pour le bulletin
    nom_fichier = f"bulletin_etudiant_{matricule}.csv"
    with open(nom_fichier, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Nom', nom_etudiant])
        writer.writerow(['Matricule', matricule])
        writer.writerow(['Matière', 'Note'])

    # Demande les notes pour chaque matière
    with open('matieres.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)  # Skip the header
        matieres = []
        for row in reader:
            if len(row) >= 2:  # Vérification de la longueur de la ligne
                matieres.append([row[0].strip(), int(row[1].strip())])

    for matiere in matieres:
        note = float(input(f"Saisir la note de {matiere[0]} (sur {matiere[1]*20}) : "))
        while note < 0 or note > matiere[1]*20:
            print("Erreur : la note doit être comprise entre 0 et", matiere[1]*20)
            note = float(input(f"Saisir la note de {matiere[0]} (sur {matiere[1]*20}) : "))
        with open(nom_fichier, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([matiere[0], note])

    # Calcule la somme des notes et des coefficients
    somme_notes = 0
    somme_coefficients = 0
    with open(nom_fichier, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if row[0] == 'Matière':  # Skip header row
                continue
            if row[0] in [mat[0] for mat in matieres]:
                note = float(row[1])
                coefficient = next((mat[1] for mat in matieres if mat[0] == row[0]), None)
                if coefficient is not None:
                    somme_notes += note
                    somme_coefficients += coefficient

    if somme_coefficients > 0:
        moyenne = somme_notes / somme_coefficients
    else:
        moyenne = 0

    # Écrit les totaux et la moyenne dans le fichier
    with open(nom_fichier, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([])
        writer.writerow(['Total des Notes', somme_notes])
        writer.writerow(['Total des Coefficients', somme_coefficients])
        writer.writerow(['Moyenne', moyenne])

    print(f"Le bulletin de note pour l'étudiant {nom_etudiant} (Matricule : {matricule}) a été créé avec succès.")

    enregistrer_moyenne(matricule,nom_etudiant, moyenne)
    creer_rangs()
    ecrire_rangs()

    # Lire et afficher le contenu du bulletin sous forme de tableau
    with open(nom_fichier, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        contenu = list(reader)
        print("\nBulletin de notes :")
        print(tabulate.tabulate(contenu, headers='firstrow', tablefmt='grid'))





def enregistrer_moyenne(matricule, nom_etudiant, moyenne):
    lignes = []  # Liste pour stocker les lignes du fichier moyennes.csv
    # Vérifie si le fichier moyennes.csv existe
    if os.path.exists('moyennes.csv'):
        # Si le fichier existe, lit les données et supprime l'ancienne entrée pour le matricule s'il existe
        with open('moyennes.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] != matricule:  # Ajoute toutes les lignes sauf celle avec le même matricule
                    lignes.append(row)
    # Ajoute la nouvelle entrée
    lignes.append([matricule, nom_etudiant, moyenne])
    # Écrit toutes les lignes dans le fichier moyennes.csv
    with open('moyennes.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for ligne in lignes:
            writer.writerow(ligne)


def creer_rangs():
    # Vérifie si le fichier moyennes.csv existe
    if not os.path.exists('moyennes.csv'):
        print("Le fichier moyennes.csv n'existe pas.")
        return
    # Lit les données du fichier moyennes.csv
    etudiants = []
    with open('moyennes.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            etudiants.append({'Matricule': row[0], 'Nom': row[1], 'Moyenne': float(row[2])})  # Ajout du nom de l'étudiant

    # Trie les étudiants par moyenne
    etudiants_tries = sorted(etudiants, key=lambda x: x['Moyenne'], reverse=True)

    # Calcule les rangs
    for i, etudiant in enumerate(etudiants_tries, start=1):
        etudiant['Rang'] = i

    # Enregistre les rangs dans le fichier rangs.csv
    with open('rangs.csv', 'w', newline='') as csvfile:
        fieldnames = ['Matricule', 'Nom', 'Moyenne', 'Rang']  # Ajout du nom de l'étudiant
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for etudiant in etudiants_tries:
            writer.writerow(etudiant)
    print("Les rangs ont été enregistrés dans le fichier rangs.csv.")


def ecrire_rangs():
    # Vérifie si le fichier rangs.csv existe
    if not os.path.exists('rangs.csv'):
        print("Le fichier rangs.csv n'existe pas.")
        return
    # Lit les données du fichier rangs.csv
    rangs_etudiants = {}
    with open('rangs.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            rangs_etudiants[row[0]] = row[3]  # Dictionnaire de rangs: matricule -> rang

    # Parcours des fichiers de bulletin de notes des étudiants
    for fichier in os.listdir('.'):
        if fichier.startswith('bulletin_etudiant_') and fichier.endswith('.csv'):
            matricule_etudiant = fichier.split('_')[2].split('.')[0]  # Obtention du matricule depuis le nom du fichier
            # Vérifie si le matricule de l'étudiant a un rang associé
            if matricule_etudiant in rangs_etudiants:
                rang_etudiant = rangs_etudiants[matricule_etudiant]
                # Supprime l'ancien rang s'il existe
                with open(fichier, 'r', newline='') as bulletin:
                    lignes_bulletin = list(csv.reader(bulletin))
                if len(lignes_bulletin) > 0 and lignes_bulletin[-1][0] == 'Rang':
                    lignes_bulletin.pop()

                # Ajoute le nouveau rang à la fin du fichier de bulletin de notes
                with open(fichier, 'w', newline='') as bulletin:
                    writer = csv.writer(bulletin)
                    writer.writerows(lignes_bulletin)
                    writer.writerow(['Rang', rang_etudiant])



def voir_bulletin():
    # Demande le numéro de matricule de l'étudiant
    matricule = input("Entrez le numéro de matricule de l'étudiant : ")

    # Vérifie si le fichier du bulletin de l'étudiant existe
    fichier_bulletin = f"bulletin_etudiant_{matricule}.csv"
    if not os.path.exists(fichier_bulletin):
        print("Ce bulletin n'existe pas.")
        return

    # Demande la confirmation pour afficher le bulletin
    with open('etudiants.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        nom_etudiant = None
        for row in reader:
            if row and row[0] == matricule:
                nom_etudiant = row[1]
                break

    confirmation = input(f"Voulez-vous voir le bulletin de {nom_etudiant} (oui/non) : ")
    if confirmation.lower() not in ['oui', 'o', 'y']:
        print("Annulation.")
        return

    # Affiche le bulletin de l'étudiant
    with open(fichier_bulletin, 'r', newline='') as bulletin:
        reader = csv.reader(bulletin)
        contenu = list(reader)
        print(f"\nBulletin de notes de {nom_etudiant} (Matricule : {matricule}) :")
        print(tabulate.tabulate(contenu, headers='firstrow', tablefmt='grid'))


def afficher_rangs():
    # Vérifie si le fichier rangs.csv existe
    if not os.path.exists('rangs.csv'):
        print("Le fichier rangs.csv n'existe pas.")
        return

    # Lit les données du fichier rangs.csv
    rangs_etudiants = []
    with open('rangs.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            rangs_etudiants.append([row[3], row[1], row[2]])  # Récupère Rang, Nom, Moyenne

    # Affiche les rangs des étudiants
    print("\nRangs des étudiants :")
    print(tabulate.tabulate(rangs_etudiants, headers=['Rang', 'Nom Etudiant', 'Moyenne'], tablefmt='grid'))





# Fonction principale du programme
def main():
    afficher_titre()

    while True:
        afficher_menu()
        choix_principal = input("Choisissez une option : ")

        if choix_principal == "1":
            afficher_matieres()

        elif choix_principal == "2":
            creer_matiere()
            afficher_matieres()

        elif choix_principal == "3":
            supprimer_matiere()


        elif choix_principal == "4":
            afficher_etudiants()

        elif choix_principal == "5":
            creer_etudiant()
            afficher_etudiants()

        elif choix_principal == "6":
            bulletin_de_note()

        elif choix_principal == "7":
            voir_bulletin()

        elif choix_principal == "8":
            afficher_rangs()

        elif choix_principal == "9":
            print("Au revoir !")
            break

        else:
            print("Option invalide. Veuillez choisir une option valide.")

if __name__ == "__main__":
    main()
