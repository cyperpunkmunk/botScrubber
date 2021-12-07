# for when we need to uncheck for numbers on the expenses page

from __future__ import print_function
from selenium import webdriver
from googleapiclient.discovery import build
from selenium.webdriver.chrome.options import Options
from google.oauth2 import service_account
import apphandler # file that reutuns our funcitons to get the data from our app
import os
from dotenv import load_dotenv


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import apphandler # file that reutuns our funcitons to get the data from our app
import os
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


#getting our variables from the .env file
load_dotenv()
WEB_DRIVER_PATH = os.getenv('WEB_DRIVER_PATH')
LOAN_URL = os.getenv('LOAN_URL')
SPREAD_SHEET_ID = os.getenv('SPREAD_SHEET_ID')
HOME_URL = os.getenv('HOME_URL')
USERNAME_ENV = os.getenv('USERNAME_ENV')
PASSWORD_ENV = os.getenv('PASSWORD_ENV')

'''
maintenance notes
need to update chromedriver and link to google sheet when its changed
'''


#webdriver options 
opts = Options()
opts.add_argument(" --headeless")
opts.add_experimental_option('excludeSwitches', ['enable-logging'])
drive = webdriver.Chrome(options=opts, executable_path=WEB_DRIVER_PATH)




#logs in to homepage
apphandler.login(drive, HOME_URL, USERNAME_ENV, PASSWORD_ENV)

cur3 = LOAN_URL + '96919945'

#gets everything from decision page
apphandler.getAppData(cur3,drive)
 
# get the dta from the bureau section of the page
apphandler.getBureauData(drive)



#fills the data in for our spreadSheet

#how we decide how our program interacts with the spreadsheet
sco = ['https://www.googleapis.com/auth/spreadsheets']

# refrence to our keys that allows us to be able to acccess the sheet with the google cloud account
jsfile = 'app/keys.json'

# Thwe id to get to our sheet, got from link of the spreadsheet
spreadid = SPREAD_SHEET_ID

apphandler.googleSheetfill(sco,jsfile,spreadid)




def expenseChecks():

    # clicking on the expenses tab
    expensesTab = drive.find_element(By.XPATH,'//*[@id="expenses"]')
    expensesTab.click()
    
    print('ar')

    
    wholeTable = drive.find_elements(By.XPATH ,'//table[@id="expensesGrid"]/tr')
    if wholeTable:
        print('good')
    else:
        print('bad')
        
    lastRow = len(wholeTable)
    for row in wholeTable:
        balanceValue = drive.find_element(By.XPATH, '//td[@aria-describedby="expensesGrid_Balance"]').text
        balanceValue = balanceValue.replace('$', '')
        balanceValue = float(balanceValue)
        print(balanceValue)
        firstClicked = False
        lastClicked = False
        if balanceValue > 80000 and lastClicked == False:
            #uncheck last box
            lastIncludeBox = drive.find_element_by_xpath(f'//tr[@id="{lastRow}"]/td[@aria-describedby="expensesGrid_Include"]/input')
            lastIncludeBox.click()
            lastClicked = True
            
            firstIncludeBox = drive.find_element(By.XPATH, '//tr[@id="1"]/td[@aria-describedby="expensesGrid_Include"]/input')
            firstIncludeBox.click()
            firstClicked = True
            print("hi")      
        
        elif balanceValue > 10000 and firstClicked == False:
            #uncheck first box
            firstIncludeBox = drive.find_element(By.XPATH, '//tr[@id="1"]/td[@aria-describedby="expensesGrid_Include"]/input')
            firstIncludeBox.click()
            firstClicked = True
            print('hi')

        
    





    saveButton = drive.find_element(By.XPATH,'//*[@id="saveExpenses"]')
    #saveButton.submit()




    
expenseChecks()

