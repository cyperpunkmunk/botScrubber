# for when we need to uncheck for numbers on the expenses page

from __future__ import print_function
from selenium import webdriver
from googleapiclient.discovery import build
from selenium.webdriver.chrome.options import Options
from google.oauth2 import service_account
import apphandler # file that reutuns our funcitons to get the data from our app
import os
from dotenv import load_dotenv

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

cur3 = LOAN_URL + '95527725'

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
