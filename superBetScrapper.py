import requests as rq 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://superbet.ro/pariuri-sportive/tenis/atp/atp-winston-salem-sua/toate"


DRIVER_PATH = 'chromedriver_win32 (1)\chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(url)
time.sleep(5)
accept_bt = driver.find_element(By.ID, 'onetrust-accept-btn-handler').click();
time.sleep(5)
events = driver.find_element(By.CLASS_NAME, "event-row");
print(events)
time.sleep(5)