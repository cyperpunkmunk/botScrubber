from __future__ import print_function
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import apphandler # file that reutuns our funcitons to get the data from our app
import os
from dotenv import load_dotenv
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#getting our variables from the .env file
load_dotenv()
WEB_DRIVER_PATH = os.getenv('WEB_DRIVER_PATH')
LOAN_URL = os.getenv('LOAN_URL')
SPREAD_SHEET_ID = os.getenv('SPREAD_SHEET_ID')
HOME_URL = os.getenv('HOME_URL')
USERNAME_ENV = os.getenv('USERNAME_ENV')
PASSWORD_ENV = os.getenv('PASSWORD_ENV')

'''
maintenence notes
need to update chromedriver and link to google sheet when its changed
'''


# Webdriver options 
opts = Options()
opts.add_argument(" --headeless")
opts.add_experimental_option('excludeSwitches', ['enable-logging'])
drive = webdriver.Chrome(options=opts, executable_path=WEB_DRIVER_PATH)



#logs in to homepage
apphandler.login(drive, HOME_URL, USERNAME_ENV, PASSWORD_ENV)



cur3 = LOAN_URL + '94809157'

#gets everything from decision page
apphandler.getAppData(cur3,drive)


def experianSelect():
    bureauButton = Select(drive.find_element_by_xpath('//*[@id="551437"]'))
    bureauButton.select_by_value('Equifax')
    
    WebDriverWait(drive, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnSave"]'))).click()


experianSelect()
