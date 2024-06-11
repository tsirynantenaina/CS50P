import pytest
import csv
import os
from project import ajouter_matiere, ajouter_etudiant  # Ajoutez une virgule entre les noms des fonctions

def test_ajouter_matiere():
    # Chemin du fichier existant
    csv_file = "matieres.csv"

    # Vérifier si le fichier est vide
    is_empty = os.stat(csv_file).st_size == 0

    # Appel de la fonction ajouter_matiere avec le chemin du fichier existant
    ajouter_matiere('Math', 4)  # Correction : Supprimer le troisième argument

    # Lire le fichier pour vérifier que la nouvelle matière a été ajoutée
    with open(csv_file, 'r', newline='') as f:
        reader = csv.reader(f)
        rows = list(reader)

    # Si le fichier est vide, vérifier que l'en-tête est présent
    if is_empty:
        assert rows[0] == ['Matieres', 'Coeff']

    # Vérifier que la nouvelle ligne a été ajoutée
    assert rows[-1] == ['Math', '4']


def test_ajouter_etudiant():
    # Chemin du fichier existant
    csv_file = "etudiants.csv"

    # Vérifier si le fichier est vide
    is_empty = os.stat(csv_file).st_size == 0

    # Appel de la fonction ajouter_etudiant avec le chemin du fichier existant
    ajouter_etudiant('2', 'John Doe')

    # Lire le fichier pour vérifier que le nouvel étudiant a été ajouté
    with open(csv_file, 'r', newline='') as f:
        reader = csv.reader(f)
        rows = list(reader)

    # Si le fichier est vide, vérifier que l'en-tête est présent
    if is_empty:
        assert rows[0] == ['Matricule', 'Nom']

    # Vérifier que la nouvelle ligne a été ajoutée
    assert rows[-1] == ['2', 'John Doe']

if __name__ == "__main__":
    pytest.main()
