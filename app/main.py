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
maintenence notes
need to update chromedriver and link to google sheet when its changed
'''


#webdriver options 
opts = Options()
opts.add_argument(" --headeless")
opts.add_experimental_option('excludeSwitches', ['enable-logging'])
drive = webdriver.Chrome(options=opts, executable_path=WEB_DRIVER_PATH)




#logs in to homepage
apphandler.login(drive, HOME_URL, USERNAME_ENV, PASSWORD_ENV)



#gets the apps data from he url
appUrl = "91768847" #equifax
loanUrl = "90435102" #notEquifax
currUrl2 ='92195948'
cur = '92197003' # banckruptcy example
bnk2 = '92784055' # banckruptycy non equifax
cur2 = '92198511' # equifax example2 
esta = '92812254' # est pay 0 ex 
equiopen = "92852575" # matching errors for non equifax
eqiuMix = '92885113'
payoffError1 = '93131657'
newOne = "94177038" # this one has a payments on current of 0
newlendor ='94245265'
bureauError = '94279712'# all 3 bureeauus give back and error
y = '94375737'
dd = '94398438' #bureau error
sd = '94406353' # bureau error consumer file locked
cur3 = LOAN_URL + '94764207'
cur4 = LOAN_URL + newlendor
#gets everything from decision page
apphandler.getAppData(cur4,drive)
 
# get the dta from the bureau section of the page
apphandler.getBureauData(drive)



#fills the data in for our spreadSheet

#how we decide how our program interacts with the spreeadsheet
sco = ['https://www.googleapis.com/auth/spreadsheets']

# refrence to our keys that allouw us to be able to acces the sheet with the google cloud account
jsfile = 'app/keys.json'

# Thwe id to get to our sheet, got from link of the spreadsheet
spreadid = SPREAD_SHEET_ID

apphandler.googleSheetfill(sco,jsfile,spreadid)




'''
values = result.get('values', [])

if not values:
   print('No data found.')
else:
   print('Name, Major:')
   for row in values:
      # Print columns A and E, which correspond to indices 0 and 4.
      print('%s, %s' % (row[0], row[4]))

'''