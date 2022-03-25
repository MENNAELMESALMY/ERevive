import selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import timeit
file = open('queries.txt', 'a')

def getSQL(questions):
    #right queries
    dumpEvery = 10
    chat_input = driver.find_elements(by=By.CLASS_NAME,value='chat-message')[0]
    for i,q in enumerate(questions):
        time.sleep(2)
        chat_input.send_keys(q) #write question
        chat_input.send_keys(Keys.RETURN) #press enter
        
        yes_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'y')))
        yes_button.click()
        if (i!= 0 and i%dumpEvery == 0) or (i == len(questions)-1 and i%dumpEvery != 0):
            dumpEvery = (i%dumpEvery)+1 if i%dumpEvery != 0 else dumpEvery
            queries = driver.find_elements(by=By.CLASS_NAME,value='query')[-dumpEvery:]
            sqlQuery = ""
            for q in queries:
                q = q.get_attribute('innerHTML')[6:-7] + '\n'
                print("query",q)
                sqlQuery += q
            print("dumbing questions",dumpEvery)
            file.write(sqlQuery)


questions = [
            'what is the nationality of the architect?',
            'what is the description of the architect?',
            'what is the nationality of the architect?',
            'what is the description of the architect?',
            'what is the nationality of the architect?',
            'what is the description of the architect?',
            'what is the nationality of the architect?',
            'what is the description of the architect?',
            'what is the nationality of the architect?',
            'what is the description of the architect?',
            #'what is the nationality of the architect?',
            #'what is the country of the architect?'
            ]
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
wait = WebDriverWait(driver, 40)
# Open the website
driver.get('https://naturalsql.com/')

# choose dataset
pencil = driver.find_elements(by=By.CLASS_NAME,value='fa-pencil-square-o')[0]
pencil.click()
#db-name
databases = driver.find_elements(by=By.CLASS_NAME,value='db-name')
databases[0].click()

start = timeit.default_timer()
getSQL(questions)
stop = timeit.default_timer()
print("time",stop-start)

# for db in databases:
#     print("db",db.get_attribute('innerHTML'))

file.close()