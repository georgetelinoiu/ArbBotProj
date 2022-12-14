from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from models import Match

def extractSuperbetData():
    url = "https://superbet.ro/pariuri-sportive/tenis/challenger/challenger-banja-luka-bih/toate"

    DRIVER_PATH = 'chromedriver.exe'
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(executable_path=DRIVER_PATH,options=op)
    driver.get(url)
    time.sleep(2)
    accept_bt = driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
    time.sleep(2)
    #Getting the lists of players
    team1 = driver.find_elements(By.CLASS_NAME,'event-summary__competitors-team1')
    team2 = driver.find_elements(By.CLASS_NAME,'event-summary__competitors-team2')

    #Getting the lists of odds
    cote1 = driver.find_elements(By.XPATH,"//span[@class='value new actionable']")
    listaCote = []
    for c in cote1:
        listaCote.append(c.text)
    #print(listaCote)

    listaCoteMeci = []
    for i in range (0,len(listaCote),2 ):
        listaCoteMeci.append([listaCote[i], listaCote[i+1]])
        #print([listaCote[i], listaCote[i+1]])
        
    listaMeciuri = []
    for t1,t2,c in zip(team1, team2, listaCoteMeci):
        meci = Match(t1.text,t2.text,c[0],c[1])
        listaMeciuri.append(meci)

    # for m in listaMeciuri:
    #     print(m)

    time.sleep(5)

    # for m in listaMeciuri:
    #     if (m.probabilitate < 100):
    #         print("Arbitrage found!")

    return listaMeciuri
