from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import logging
import time

USERNAME = 'USERNAME'
PASSWORD = 'PASSWORD'
URL = "https://communities.win/c/funny/new"
LOGIN_BUTTON_CSS = "#app > header > div > div.sc-1tg9jte-1.fsVFHt.desktop > div.sc-1tg9jte-31.iuSply > div > div.sc-1tg9jte-5.dGvpnF"
USERNAME_CSS = "#field-9"
PASSWORD_CSS = "#field-10"
SUBMIT_CSS = "#chakra-modal-8 > footer > button.chakra-button.css-za4or7"
DOWNVOTE_BUTTON_CSS_SELECTOR = 'div > div > div > div.sc-ct8gzq-1.dzTwau.vote > button.sc-1tigerj-0.sc-1tigerj-1.fQDdlK.fQWcKY.down.vote-delta'
SKIP_CSS = 'div > div > div > div.sc-ct8gzq-1.gwRACt.vote > button.sc-1tigerj-0.sc-1tigerj-1.fQDdlK.fQWcKY.down.vote-delta.animate.active' 
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("user-agent=Mozilla/5.0")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 15)

try:
    driver.get(URL)

    login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, LOGIN_BUTTON_CSS)))
    login_button.click()

    username_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, USERNAME_CSS)))
    password_input = driver.find_element(By.CSS_SELECTOR, PASSWORD_CSS)

    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)

    submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, SUBMIT_CSS)))
    submit.click()
    time.sleep(6)  

    downvote_buttons = driver.find_elements(By.CSS_SELECTOR, DOWNVOTE_BUTTON_CSS_SELECTOR)
    logging.info(f"Found {len(downvote_buttons)} downvote buttons.")

    for button in downvote_buttons:
        try:
            button.click()
            logging.info("Clicked a downvote button.")
            time.sleep(1)  
        except Exception as e:
            logging.warning(f"Could not click downvote button: {e}")

except Exception as e:
    logging.error("An error occurred: " + str(e))
finally:
    driver.quit()
