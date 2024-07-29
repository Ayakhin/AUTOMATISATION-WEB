from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_google_search():
    # Configurer les options pour Brave
    chrome_options = Options()
    chrome_options.binary_location = r'C:\Users\rayan\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe'  # Chemin vers l'exécutable Brave

    # Créer une instance du navigateur avec les options pour Brave
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        # Ouvrir Google
        driver.get("https://www.google.com")
        
        # Attendre et accepter les conditions d'utilisation si le bouton est présent
        try:
            # Essayer divers sélecteurs pour le bouton d'acceptation
            accept_button = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"J\'accepte")]'))
            )
            accept_button.click()
        except Exception as e:
            print("Le bouton d'acceptation des conditions d'utilisation n'a pas été trouvé ou ne pouvait pas être cliqué :", e)
        
        # Attendre que le champ de recherche soit visible
        search_box = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.NAME, "q"))
        )
        
        # Ajouter une pause pour s'assurer que l'élément est prêt
        time.sleep(1)
        
        # Assurer que le champ est cliquable
        search_box = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.NAME, "q"))
        )

        # Effectuer une recherche
        search_box.send_keys("OpenAI")
        search_box.submit()
        
        # Attendre que les résultats de recherche soient chargés
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "search"))
        )
        
        # Ajouter des assertions pour vérifier le contenu
        assert "OpenAI" in driver.page_source, "Le terme de recherche n'a pas été trouvé dans les résultats"
    
    finally:
        # Fermer le navigateur
        driver.quit()
