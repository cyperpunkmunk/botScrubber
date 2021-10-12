from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import re
import apphandler
import auto
driver = webdriver.Chrome("C:\\chromedriver.exe")
import pprint
homeUrl = "https://gravitylending.defisolutions.com/ui/login"

pp = pprint.PrettyPrinter(indent=4, width=250)

def login(url):
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="username"]').send_keys('kgibson')
    driver.find_element_by_xpath('//*[@id="password"]').send_keys('Kennethjr01+')
    driver.find_element_by_xpath('//*[@id="submit-button"]').click()
    print('login successful')

    
login(homeUrl)


driver.implicitly_wait(200)


#gets the apps data from he url
appUrl = "https://gravitylending.defisolutions.com/Funder/LoanApplications/Decisioning?loanApplicationID=91768847" #equifax
loanUrl = "https://gravitylending.defisolutions.com/Funder/LoanApplications/Decisioning?loanApplicationID=90435102" #notEquifax
apphandler.getAppData(loanUrl,driver)
    

    



def getbureauData():

    driver.implicitly_wait(400)
    
    driver.find_element_by_xpath('//*[@id="bureau"]').click()

    driver.implicitly_wait(400)

    bureauData = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div/div/div[3]/div[3]/span/div/pre').text


    reurnedLines = auto.get_nonequifax_auto_data(bureauData)

    print(reurnedLines)
    