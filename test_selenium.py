from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_form_authentication():
    # Configurer les options pour Brave
    chrome_options = Options()
    chrome_options.binary_location = r'C:\Users\rayan\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe'  # Chemin vers l'exécutable Brave

    # Créer une instance du navigateur avec les options pour Brave
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        # Ouvrir le site
        driver.get("https://the-internet.herokuapp.com/")
        time.sleep(2)  # Pause pour voir le site

        # Naviguer vers la page "Form Authentication"
        driver.find_element(By.LINK_TEXT, "Form Authentication").click()
        time.sleep(2)  # Pause pour voir la navigation

        # Attendre que le champ de nom d'utilisateur soit visible
        username_box = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "username"))
        )
        time.sleep(2)  # Pause pour voir le champ

        # Saisir le nom d'utilisateur
        username_box.send_keys("tomsmith")
        time.sleep(2)  # Pause pour voir la saisie du nom d'utilisateur

        # Saisir le mot de passe
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        time.sleep(2)  # Pause pour voir la saisie du mot de passe

        # Cliquer sur le bouton de connexion
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)  # Pause pour voir le clic

        # Attendre que le message de succès soit visible
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".flash.success"))
        )
        time.sleep(2)  # Pause pour voir le message de succès

        # Vérifier que la connexion a réussi
        assert "You logged into a secure area!" in success_message.text, "Échec de la connexion"

        print("Test réussi : Connexion effectuée avec succès.")
    
    finally:
        # Fermer le navigateur
        driver.quit()

# Exécuter le test
if __name__ == "__main__":
    test_form_authentication()
