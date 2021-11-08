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



#gets the apps data from the url
appUrl = "91768847" #equifax
loanUrl = "90435102" #notEquifax
currUrl2 ='92195948'
cur = '92197003' # banckruptcy example
bnk2 = '92784055' # banckruptycy non equifax
cur2 = '92198511' # equifax example2 
esta = '92812254' # est pay 0 ex 
equiopen = "92852575" # matching errors for non equifax
eqiuMix = '92885113'
payoffError1 = '93131657' ## DONE
newOne = "94177038" # this one has a payments on current of 0 # URGENT!!!
newlendor ='94245265' ## DONE
bureauError = '94279712'# all 3 bureaus give back and error
y = '94375737'
dd = '94398438' #bureau error
sd = '94406353' # bureau error consumer file locked

dub = '94878395' # equifax loan on sum dumb
dub2 = '94916333' # equifax loan on sum dumb 

sd = '94993084' # equifax file freeze
ssa = '94997723' # equifax banckruptcy
ssawe3 = '95111726' #nonequifax banckruptcy2
fk = '95053557' # nonequifax banckuptcy
fgb = '95218758' # non equifax banckruptcy 
ch  = '95107790'# customer with duplicate application
ewgfe = '95221261' # file locked t consumers request ##DONE
egrc = '95239642' # credit bureau error ## IFFY
rurhr = '95266936' # new lendor 2
rtgrt = '95308158'# new lendor 3
hiheiuru = '95366045' # new lendor 4
efeguv = '95420633'# FILE FROZEN DUE TO FEDERAL LEGISLATION.
oiwef = '95417554' # new lendor banckrupcty

sasa = '95433188' # bug with '0' payment for one spot
asc = '95434300' # same bug ^


cur3 = LOAN_URL + '95527725'

cur4 = LOAN_URL + fgb
#gets everything from decision page
apphandler.getAppData(cur3,drive)
 
# get the dta from the bureau section of the page
apphandler.getBureauData(drive)



#fills the data in for our spreadSheet

#how we decide how our program interacts with the spreadsheet
sco = ['https://www.googleapis.com/auth/spreadsheets']

# refrence to our keys that allouw us to be able to acces the sheet with the google cloud account
jsfile = 'app/keys.json'

# Thwe id to get to our sheet, got from link of the spreadsheet
spreadid = SPREAD_SHEET_ID

apphandler.googleSheetfill(sco,jsfile,spreadid)


