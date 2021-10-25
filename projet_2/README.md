## Projet OpenClassrooms
## projet 2 Utilisez les bases de Python pour l'analyse de marché

# Récupérer le projet :

```text
git clone https://github.com/ydjabela/Projet_OpenClassrooms/edit/main/projet_2
```

## Création de l'environnement virtuel

# Assurez-vous d'avoir installé python et de pouvoir y accéder via votre terminal, en ligne de commande.

# Si ce n'est pas le cas : https://www.python.org/downloads/

```
python -m venv Projet_2
```

## Activation de l'environnement virtuel du projet
```
Projet_2\Scripts\activate.bat
```
## Installation  des  packages necessaire pour ce projet
```
pip install -r requirements.txt
```

## Exécuter le scraper (à la racine du projet) :

```python
# pour exécuter le scraper complet
python P2_04_codesource_recuperation_donnees_categories_avec_image.py
# la premiere  fois  il faut choisir Y "yes" pour  mettre a  jour les  lien et creation des dossier et pour telecharger  les  images

# le  promier  process sert a chercher  les liens et les  pages de chaque categorie
# le deuxieme  process sert a obtenir toutes  les  informations necessaires pour chaque  livre 
# scraper correspondant à l'étape 1 du projet
python P2_01_codesource_test1.py

# scraper correspondant à l'étape 2 du projet
python P2_02_codesource_recupération_donnee_une_categorie.py

# scraper correspondant à l'étape 3 du projet

python P2_03_codesource_recuperation_donnee_toute_categorie.py
# scraper correspondant à l'étape 4 du projet
python P2_04_codesource_recuperation_donnees_categories_avec_image.py


# Cette commande sera obligatoire à chaque fois que vous voudrez travailler avec le cours. Dans le même terminal, tapez maintenant
pip install -r requirements.txt

## Contributeurs
# Yacine Djabela
# Stephane Didier
