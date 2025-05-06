# Adless YouTube Player

Adless YouTube Player est une application web simple qui permet de rechercher et de lire des vidéos YouTube sans publicités. Ce projet sert de proof of concept pour démontrer l'utilisation de bibliothèques Python telles que Flask, yt-dlp, et youtube-search.

## Fonctionnalités

- Recherche de vidéos YouTube via une interface utilisateur simple.
- Lecture de vidéos YouTube sans publicités.
- Extraction des URL des vidéos en utilisant `yt-dlp`.

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

- Python 3.11.9 ou une version ultérieure
- pip (gestionnaire de paquets Python)

## Installation

1. Clonez ce dépôt sur votre machine locale :

   ```bash
   git clone https://github.com/Wishrito/adless-youtube-player.git
   cd adless-youtube-player
   ```

2. Créez un environnement virtuel Python (optionnel mais recommandé) :

   ```bash
   python -m venv venv
   source venv/bin/activate # Sur Windows : venv\Scripts\activate
   ```

3. Installez les dépendances nécessaires :

   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

1. Lancez l'application Flask :

   ```bash
   python app.py
   ```

2. Ouvrez votre navigateur et accédez à l'URL suivante :

   ```
   http://127.0.0.1:5000/
   ```

3. Utilisez l'interface pour rechercher des vidéos YouTube, afficher les résultats, et lire les vidéos.

## Structure du Projet

- `app.py` : Fichier principal contenant la logique de l'application Flask.
- `requirements.txt` : Liste des dépendances Python nécessaires.
- `templates/` : Dossier contenant les fichiers HTML pour l'interface utilisateur.
- `src/` : Dossier contenant les fichiers statiques (CSS, JavaScript, etc.).

## Dépendances

Les principales bibliothèques utilisées dans ce projet sont :

- [Flask](https://flask.palletsprojects.com/) : Framework web léger pour Python.
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) : Outil pour extraire des informations sur les vidéos YouTube.
- [youtube-search](https://pypi.org/project/youtube-search/) : Bibliothèque pour effectuer des recherches sur YouTube.

## Contribution

Les contributions sont les bienvenues ! Si vous souhaitez améliorer ce projet, n'hésitez pas à ouvrir une issue ou à soumettre une pull request.

## Licence

Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus d'informations.

Ce fichier fournit une description claire du projet, des instructions pour l'installation et l'exécution, ainsi qu'une vue d'ensemble des fonctionnalités et de la structure du dépôt.
