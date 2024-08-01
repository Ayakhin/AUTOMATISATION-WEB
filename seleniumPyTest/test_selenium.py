from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_form_authentication():
    chrome_options = Options()
    chrome_options.binary_location = r'C:\Users\rayan\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe'

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        driver.get("https://the-internet.herokuapp.com/")
        time.sleep(2)  

        driver.find_element(By.LINK_TEXT, "Form Authentication").click()
        time.sleep(2)  

        username_box = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "username"))
        )   
        time.sleep(2)  

        username_box.send_keys("tomsmith")
        time.sleep(2)  

        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        time.sleep(2)  

        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)  

        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".flash.success"))
        )
        time.sleep(2)  

        assert "You logged into a secure area!" in success_message.text, "Échec de la connexion"

        print("Test réussi : Connexion effectuée avec succès.")
    
    finally:
        driver.quit()

if __name__ == "__main__":
    test_form_authentication()
