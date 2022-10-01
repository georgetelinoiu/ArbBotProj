from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from models import Match

def extractUniBetData():
    url = "https://www.unibet.ro/betting/sports/filter/tennis/challenger/banja_luka/all/matches"

    DRIVER_PATH = 'chromedriver.exe'
    # op = webdriver.ChromeOptions()
    # op.add_argument('headless')
    driver = webdriver.Chrome(executable_path=DRIVER_PATH) #options=op
    driver.get(url)
    time.sleep(2)
    accept_bt = driver.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll').click()

    time.sleep(2)

    #Getting the lists of players
    players = driver.find_elements(By.CLASS_NAME,'c539a')
    odds = driver.find_elements(By.CLASS_NAME, '_8e013')

    matchingPlayOdd = []
    for p,o in zip(players,odds):
        playerName = p.text
        playerName = playerName.replace(",", "")
        playerName = playerName.split(" ")
        finalPlayerName = playerName[1] + " " + playerName[0]
        matchingPlayOdd.append([finalPlayerName,o.text])

    #print(matchingPlayOdd)

    matchList = []
    listSize = len(matchingPlayOdd)
    for i in range(0,listSize,2) :
        # print(matchingPlayOdd[i])
        # print(matchingPlayOdd[i+1])
        match = Match(matchingPlayOdd[i][0], matchingPlayOdd[i+1][0], matchingPlayOdd[i][1],  matchingPlayOdd[i+1][1])
        matchList.append(match)

    # for m in matchList:
    #     print(m)
    
    return matchList
