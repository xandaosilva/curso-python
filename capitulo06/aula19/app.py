import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVER_EXEC = ROOT_FOLDER / "drivers" / "chromedriver"
TIME_TO_WAIT = 5

chrome_options = webdriver.ChromeOptions()
chrome_service = Service(executable_path=str(CHROMEDRIVER_EXEC))
chrome_browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
chrome_browser.get("https://www.google.com")

search_input = WebDriverWait(chrome_browser, TIME_TO_WAIT).until(EC.presence_of_element_located((By.NAME, "q")))
search_input.send_keys("Hello world")
search_input.send_keys(Keys.ENTER)

results = chrome_browser.find_element(By.ID, "search")
links = results.find_elements(By.TAG_NAME, "a")
print(results)
links[0].click()

time.sleep(TIME_TO_WAIT)
