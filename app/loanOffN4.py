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
import time

'''

#getting our variables from the .env file
load_dotenv()
WEB_DRIVER_PATH = os.getenv('WEB_DRIVER_PATH')
LOAN_URL = os.getenv('LOAN_URL')
SPREAD_SHEET_ID = os.getenv('SPREAD_SHEET_ID')
HOME_URL = os.getenv('HOME_URL')
USERNAME_ENV = os.getenv('USERNAME_ENV')
PASSWORD_ENV = os.getenv('PASSWORD_ENV')


maintenence notes
need to update chromedriver and link to google sheet when its changed



# Webdriver options 
opts = Options()
opts.add_argument(" --headeless")
opts.add_experimental_option('excludeSwitches', ['enable-logging'])
drive = webdriver.Chrome(options=opts, executable_path=WEB_DRIVER_PATH)



#logs in to homepage
apphandler.login(drive, HOME_URL, USERNAME_ENV, PASSWORD_ENV)



cur3 = LOAN_URL + '95527725'


#gets everything from decision page
apphandler.getAppData(cur3,drive)


#ppq type variable 

ppqVer = drive.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div/div/div/div/div/form/div[1]/table[1]/tbody/tr/td[1]/table[3]/tbody/tr[1]/td[1]/label').text
   
   
# apr rate variable
aprRate = '6.25%'
'''


def fillLoData(drive, ppqVer, aprRate):

    # the list of ppq variables when its ok to do a hard pull request
    needPpList = ['LENTREE' , 'MYAL' , 'MYAL2' , 'V&D', 'MTG-LENDER']

    

    # use this to choose ppq depending on what it says
    drive.implicitly_wait(400)
    
    # how we get the button for the ppq table
    ppqButton = Select(drive.find_element(By.XPATH,'//*[@id="528582"]'))
    time.sleep(1)
    
    # variable to change the value if it says 0.00%
    aprRateText = drive.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div/div/div/div/div/form/div[1]/table[1]/tbody/tr/td[1]/table[4]/tbody/tr[3]/td[2]/input').text
    time.sleep(1)


    def ppqCheck( variable , listOfNeedPP, button ):
        
        # if our pp name is in the list of items that need pp
        if variable in listOfNeedPP:
            button.select_by_value('NEED PP')
            print('need pp')
        
        else:
            button.select_by_value('YES')
            print('yes')

    
    def aprCheck():

        # Variable to change the value if it says 0.00%
        aprRateText = drive.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div/div/div/div/div/form/div[1]/table[1]/tbody/tr/td[1]/table[4]/tbody/tr[3]/td[2]/input').get_attribute('value')
        
        drive.implicitly_wait(400)
        
        # Variable to change the number
     
        aprRateChangeVar = drive.find_element(By.ID,'522672')
 

        if aprRate == '0.00%':

          
      
         
            WebDriverWait(drive, 20).until(EC.element_to_be_clickable((By.ID, '522672'))).clear()
            time.sleep(.5)
            WebDriverWait(drive, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="522676"]' ))).send_keys('00.9')
            drive.find_element(By.XPATH, '//*[@id="btnSave"]')
            print('need apr')
            
        
        else:
            drive.implicitly_wait(400)

            print('no apr')

            

    

    

    # has to be in this format
    ## (Last ,First) 

    loName = 'Gibson, Kenneth'
    loname2 = 'Jones, Brian'



    def loSelect(name):

        # How we get our lo selector button for the pop-up menu
        loPopupButton = Select(drive.find_element(By.XPATH,'//*[@id="assignedOptions"]'))
        drive.implicitly_wait(400)
        ## Select assign option button
        loPopupButton.select_by_value("2")
        drive.implicitly_wait(400)


        # Button to select lo officer
        underwriterButtonVar = Select(drive.find_element(By.XPATH,'//*[@id="manageUserAssignment_modal"]/div/div[4]/div[2]/select'))
        underwriterButtonVar.select_by_visible_text(name)
        print('clicked on element')


        # Button to select CSA
        CSAbuttonVar = Select(drive.find_element(By.XPATH,'//*[@id="manageUserAssignment_modal"]/div/div[7]/div[2]/select'))
        CSAbuttonVar.select_by_visible_text(name)
        print('clicked on second element')


        # Button click to save the assigned user
        drive.find_element(By.XPATH,'//*[@id="btnSaveAssignments"]').click()

    
    # saving the data on our main page before we change pages
    def saveFilledDataMain():    
        
        # Button to save everything on the main page (except for the saved approved lenders)
        saveButton = drive.find_element(By.XPATH,'//*[@id="btnSave"]')
        saveButton.submit()
        print('saved page')
        


    


    # Filling the form in to choose our user
    loSelect(loName)
    time.sleep(1)
    
    # How we check the pp lender and fill the form depending on which one it is
    ppqCheck(ppqVer, needPpList, ppqButton)


    time.sleep(1)
    # Checking and filling in our apr rate
    aprCheck()
    

    time.sleep(1)

    # Saving the data again
    saveFilledDataMain()
    
    



  

  

    
   

    
        
  
        
   
        
        
        

