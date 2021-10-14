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



#ppq type variable 
ppqVer = drive.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div/div/form/div[1]/table[1]/tbody/tr/td[1]/table[3]/tbody/tr[1]/td[1]/label').text
    
# apr rate variable
aprRate = drive.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div/div/form/div[1]/table[1]/tbody/tr/td[1]/table[4]/tbody/tr[3]/td[2]/input').get_attribute('value')


def fillLoData(drive, ppqVer, aprRate):

    # thep list of ppq variables when its ok to do a hard pull request
    needPpList = ['LENTREE' , 'MYAL' , 'MYAL2' , 'V&D', 'MTG-LENDER']

    print(ppqVer)
    print(aprRate)

    # use this to choose ppq depending on what it says
    drive.implicitly_wait(400)
    ppqButton = Select(drive.find_element_by_xpath('//*[@id="528582"]'))
    drive.implicitly_wait(400)
    
    # variable to change the valu if it says 0.00%
    aprRateText = drive.find_element_by_xpath('//*[@id="522672"]')
    

    def ppqCheck( variable , listOfNeedPP, button ):
        
        if variable in listOfNeedPP:
            
            button.select_by_value('NEED PP')
            print('need pp')
        
        else:
            button.select_by_value('YES')
            print('yes')

    
    def aprCheck(aprVariable , textToSend):
        
        if aprVariable == '0.00%':

            textToSend.send_keys('0.09')
            
        
        else: 
            
            pass
    
    ppqCheck(ppqVer, needPpList, ppqButton)
    aprCheck(aprRate, aprRateText)
    


fillLoData(drive, ppqVer, aprRate)
  

  

    
   

    
        
  
        
   
        
        
        

