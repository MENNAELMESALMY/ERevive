import selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import timeit
import pickle

file = open('queries.txt', 'a')
keywords = {}
def getKeywords(dbName):
    #right queries
    time.sleep(2)
    tables = driver.find_elements(by=By.CLASS_NAME,value='db-table')
    if len(tables) == 0:
        return
    keywords[dbName] = {}
    for i,table in enumerate(tables):
        divs = table.find_elements(by = By.TAG_NAME,value = 'div')
        print()
        print("table num ",i)
        for idx,div in enumerate(divs):
            if idx==0:
                print("tableName",div.text)
                keywords[dbName][div.text] = []
                
            else:
                keywords[dbName][divs[0].text].append(div.text)



driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
wait = WebDriverWait(driver, 40)
# Open the website
driver.get('https://naturalsql.com/')
pencil = driver.find_elements(by=By.CLASS_NAME,value='fa-pencil-square-o')[0]

xpath = '//*[@id="database-edit"]/div/div/div[2]/div/div/ul/li[6]'
nextBtn = driver.find_elements(by = By.XPATH,value = xpath)

pencil.click()
page = 1

try:
    for i in range(8):
        print("page num",page)
        #db-name
        databases = driver.find_elements(by=By.CLASS_NAME,value='db-name')
        databases[0].click()

        start = timeit.default_timer()

        for db in databases:
            time.sleep(1)
            dbName = db.get_attribute('innerHTML')[6:-7]
            print("dbName",dbName)

            #navigate to database
            pencil.click()
            db.click()

            getKeywords(dbName)
        
        #got to next page 
        pencil.click()
        nextBtn[0].click()
        page += 1
except Exception as e:
    print(e)

stop = timeit.default_timer()
print("time",stop-start)
print(keywords)
file.close()

with open('/home/hager/college/GP/GP/src/SearchEngine/crawler/keyWords.pickle', 'wb') as handle:
    pickle.dump(keywords, handle, protocol=pickle.HIGHEST_PROTOCOL)