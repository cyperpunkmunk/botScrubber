from __future__ import print_function
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import apphandler # file that reutuns our funcitons to get the data from our app
import os
from dotenv import load_dotenv
from selenium.webdriver.support.ui import Select
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


# 
cur3 = LOAN_URL + '94341518'

#gets everything from decision page
apphandler.getAppData(cur3,drive)



def fillLoData(drive):

    # thep list of ppq variables when its ok to do a hard pull request
    needPpList = []

    # use this to choose ppq depending on what it says
    drive.implicitly_wait(400)
    ppqButton = Select(drive.find_element_by_xpath('//*[@id="528582"]'))
    drive.implicitly_wait(400)
    ppqButton.select_by_value('YES')
    


fillLoData(drive)
  

  

    
   

    
        
  
        
   
        
        
        

