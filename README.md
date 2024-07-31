# AUTOMATISATION-WEB

Test d'authentification avec Selenium et Brave
Ce projet contient un test automatisé pour vérifier l'authentification sur le site The Internet en utilisant Selenium et le navigateur Brave.

Prérequis
Avant de pouvoir exécuter ce test, vous devez installer les outils et bibliothèques suivants :

Python 3.7+
pip
Google Chrome (Brave est basé sur Chromium)
Brave Browser

Installation

Cloner le dépôt
git clone https://github.com/Ayakhin/AUTOMATISATION-WEB.git
cd votre-repo
Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Pour Windows, utilisez `venv\Scripts\activate`
Installer les dépendances

pip install -r requirements.txt
Configuration
Assurez-vous que Brave est installé sur votre machine. Ensuite, mettez à jour le chemin vers l'exécutable Brave dans le script de test si nécessaire :

Copier le code
chrome_options.binary_location = r'C:\Users\votre-utilisateur\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe'
Exécution du test
Pour exécuter le test, utilisez la commande suivante :

pytest test_selenium.py
Structure du projet
test_selenium.py: Contient le test d'authentification automatisé.
requirements.txt: Liste des dépendances Python nécessaires pour exécuter le test.
