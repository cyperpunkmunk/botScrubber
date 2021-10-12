from __future__ import print_function
from selenium import webdriver
from googleapiclient.discovery import build
from selenium.webdriver.chrome.options import Options
from google.oauth2 import service_account
import apphandler # file that reutuns our funcitons to get the data from our app

#maintenence notes

#need to update chromedriver and link to google sheet when its changed



#webdriver options 
opts = Options()
opts.add_argument(" --headeless")
opts.add_experimental_option('excludeSwitches', ['enable-logging'])
drive = webdriver.Chrome(options=opts, executable_path="C:\\chromedriver.exe")




#logs in to homepage
apphandler.login(drive)



#gets the apps data from he url
appUrl = "https://gravitylending.defisolutions.com/Funder/LoanApplications/Decisioning?loanApplicationID=91768847" #equifax
loanUrl = "https://gravitylending.defisolutions.com/Funder/LoanApplications/Decisioning?loanApplicationID=90435102" #notEquifax
#currUrlId = input('User Url Id:')
#currUrl ='https://gravitylending.defisolutions.com/Funder/LoanApplications/Decisioning?loanApplicationID='+currUrlId 
currUrl2 ='https://gravitylending.defisolutions.com/Funder/LoanApplications/Decisioning?loanApplicationID=92195948'
cur = 'https://gravitylending.defisolutions.com/Funder/LoanApplications/Decisioning?loanApplicationID=92197003' # banckruptcy example
bnk2 = 'https://gravitylending.defisolutions.com/Funder/LoanApplications/Decisioning?loanApplicationID=92784055' # banckruptycy non equifax
cur2 = 'https://gravitylending.defisolutions.com/Funder/LoanApplications/Decisioning?loanApplicationID=92198511' # equifax example2 
esta = '92812254' # est pay 0 ex 
equiopen = "92852575" # matching errors for non equifax
eqiuMix = '92885113'
payoffError1 = '93131657'

newOne = "94177038" # this one has a payments on current of 0

cur3 = 'https://gravitylending.defisolutions.com/Funder/LoanApplications/Decisioning?loanApplicationID=94213585'

apphandler.getAppData(cur3,drive)
 
# get the dta from the bureau section of the page
apphandler.getBureauData(drive)



#fills the data in for our spreadSheet

#how we decide how our program interacts with the spreeadsheet
sco = ['https://www.googleapis.com/auth/spreadsheets']

# refrence to our keys that allouw us to be able to acces the sheet with the google cloud account
jsfile = 'keys.json'

# Thwe id to get to our sheet, got from link of the spreadsheet
spreadid = '18VvlYUs3BM8mMDdltrGY9wA-3ebz4nKH8c_OL1KxFhI'

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