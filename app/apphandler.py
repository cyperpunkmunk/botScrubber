
from __future__ import print_function
from typing import Text
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import re
from selenium import webdriver
from googleapiclient.discovery import build
from selenium.webdriver.chrome.options import Options
from google.oauth2 import service_account
import auto

# dataText 
dataText = []


#loginfunciton
def login(drive , homeUrl, username, password):
    
    #home webpage lgoin
    drive.get(homeUrl)
    drive.find_element_by_xpath('//*[@id="username"]').send_keys(username)
    drive.find_element_by_xpath('//*[@id="password"]').send_keys(password)
    drive.find_element_by_xpath('//*[@id="submit-button"]').click()
    print('login successful')




def getAppData(Url,drive):

    drive.implicitly_wait(200)

    drive.find_element_by_xpath('//*[@id="dashboard-container"]/div/div[2]/a').click()


    drive.implicitly_wait(400)

    drive.get(Url)

    currentPage = drive.current_url

    drive.refresh()
    
    drive.implicitly_wait(400)

    print(currentPage)

    
    global dataText

    dataText = []

    data = drive.find_element_by_class_name('tableRow').text

    userCounty = drive.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[14]/div[2]/div/div[2]/table/tbody/tr[17]/td[2]').text
    state = drive.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[14]/div[2]/div/div[2]/table/tbody/tr[18]/td[2]').text
    ficoScore = drive.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[14]/div[2]/div/div[2]/table/tbody/tr[21]/td[2]').text
    vehicleYear = drive.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[14]/div[2]/div/div[2]/table/tbody/tr[31]/td[2]').text
    vehicleMake =  drive.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[14]/div[2]/div/div[2]/table/tbody/tr[32]/td[2]').text
    vehicleModel = drive.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[14]/div[2]/div/div[2]/table/tbody/tr[33]/td[2]').text
    vehicleMileage = drive.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[14]/div[2]/div/div[2]/table/tbody/tr[35]/td[2]').text
    estimatedPayoff = drive.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div/div/form/div[1]/table[1]/tbody/tr/td[3]/table[3]/tbody/tr[8]/td[2]/input').get_attribute('value')
    ppqVer = drive.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div/div/form/div[1]/table[1]/tbody/tr/td[1]/table[3]/tbody/tr[1]/td[1]/label').text
    aprRate = drive.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div/div/form/div[1]/table[1]/tbody/tr/td[1]/table[4]/tbody/tr[3]/td[2]/input').get_attribute('value')
    estimatedPayoff2 = drive.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div/div/form/div[1]/table[1]/tbody/tr/td[3]/table[1]/tbody/tr[1]/td[2]/input').get_attribute('value')
    originalLoanAmout = drive.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div/div/form/div[1]/table[1]/tbody/tr/td[3]/table[3]/tbody/tr[19]/td[2]/input').get_attribute('value')
    remainingbalance = drive.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div/div/form/div[1]/table[1]/tbody/tr/td[3]/table[3]/tbody/tr[20]/td[2]/input').get_attribute('value')


    dataText.append(state)
    dataText.append(ficoScore)
    dataText.append(estimatedPayoff)
    dataText.append(vehicleYear)
    dataText.append(vehicleMileage)
    dataText.append(userCounty)
    dataText.append(vehicleMake)
    dataText.append(vehicleModel)
    dataText.append(ppqVer)
    dataText.append(aprRate)
    dataText.append(originalLoanAmout)
    dataText.append(remainingbalance)
    
  
    
    # for when we need to translate our numbers
    def translateNums (loanAmount, remainingBal):
        
        global translatedNums
        translatedNums = []

        
                
        # how we translate it
        orgLoanTranslate = loanAmount.replace('.00','')
        remainingTranslate = remainingBal.replace('.00','')
        
        orgLoanTranslate = loanAmount
        remainingTranslate = remainingBal


        translatedNums.append(orgLoanTranslate)
        translatedNums.append(remainingTranslate)
        
        return

    translateNums(originalLoanAmout,remainingbalance)




  

    print(dataText)
    print(translatedNums)



    states = {
        "AL": "Alabama",
        "AK": "Alaska",
        "AZ": "Arizona",
        "AR": "Arkansas",
        "CA": "California",
        "CZ": "Canal Cone",
        "CO": "Colorado",
        "CT": "Connecticut",
        "DE": "Delaware",
        "DC": "District_of_Colombia",
        "FL": "Florida",
        "GA": "Georgia",
        "GU": "Guam",
        "HI": "Hawaii",
        "ID": "Idaho",
        "IL": "Illinois",
        "IN": "Indiana",
        "IA": "Iowa",
        "KS": "Kansas",
        "KY": "Kentucky",
        "LA": "Louisiana",
        "ME": "Maine",
        "MD": "Maryland",
        "MA": "Massachusetts",
        "MI": "Michigan",
        "MN": "Minnesota",
        "MS": "Mississippi",
        "MO": "Missouri",
        "MT": "Montana",
        "NE": "Nebraska",
        "NV": "Nevada",
        "NH": "New_Hampshire",
        "NJ": "New_Jersey",
        "NM": "New_Mexico",
        "NY": "New_York",
        "NC": "North_Carolina",
        "ND": "North_Dakota",
        "OH": "Ohio",
        "OK": "Oklahoma",
        "OR": "Oregon",
        "PA": "Pennsylvania",
        "PR": "Puerto_Rico",
        "RI": "Rhode_Island",
        "SC": "South_Carolina",
        "SD": "South_Dakota",
        "TN": "Tennessee",
        "TX": "Texas",
        "UT": "Utah",
        "VT": "Vermont",
        "VI": "Virgin_Islands",
        "VA": "Virginia",
        "WA": "Washington",
        "WV": "West_Virginia",
        "WI": "Wisconsin",
        "WY": "Wyoming"
    }


    




    global stateLong
    stateLong = states.get(dataText[0])
    print(stateLong)



def countyHandler():
    print('hi')



    

    



def getBureauData(drive):

    drive.implicitly_wait(400)
    
    drive.find_element_by_xpath('//*[@id="bureau"]').click()

    drive.implicitly_wait(400)

    bureauData = drive.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div/div/div[3]/div[3]/span/div/pre').text

    x = re.search("THIS FORM PRODUCED BY EQUIFAX" , bureauData)
    y = re.search("TRANSUNION CREDIT REPORT" , bureauData)
    
    #the variables we use for gettting loans and payoffs

    # need to set the number of total open loans to a list to use in our spreadsheet
    
    global openCount
    openCount = []

    global openCountStr
    openCountStr = 0

    global currentCount
    currentCount = 0
    
    global openList
    openList = []
    
    global currentApp
    
    
    global appMonths
    appMonths = []

    
        
    if x:

        print('this was made with equifax')
        returnedData = auto.get_equifax_auto_data(bureauData)

                #compare(translatedNums[0],loan)


      
        print('euifax translated list')
  
        print('translated nums')
        print(translatedNums)
        print(openCount)
        print(returnedData)
    

    elif y:
        print('this was made with the new lender')
        
    else: 
        
        print('not eqifax')
        returnedData = auto.get_nonequifax_auto_data(bureauData)
        
        
        currentAppLoan = []
        
        
        
        totalCount = 0
        
        appMonths = []
        
        for data in returnedData:
            
            cmd = data['status'], data['months'], data["prices"]
            cmdcurrPay = data['prices']
            cmdTotalMonths = data['months']

            #turning the total months into an int
            totalMonthsInt = int(cmdTotalMonths)
            
            totalCount += totalMonthsInt
            
            if data['status'] == 'N/A':
            
            
                continue
            
            elif data['status'] == 'OPEN':

                #if the first number in the current pay record matches the first payoff number of the current loan
                if cmdcurrPay[0:1] == translatedNums[0:1]:
                    
                    cmdCurrentMonths = int(data['months'])   
                        
                    currentAppLoan.append(cmd)
                    
                    currentCount += cmdCurrentMonths

                    print(currentAppLoan)
                
                else:
                    continue


                openCountStr += 1
                openList.append(cmd)
     
                continue

            else:    
                openList.append(cmd)

                continue
        
            
        
        
        openCount.append(str(openCountStr))
        
        
        if currentCount >= 12:
            currentCountTranslate = "12+"
            
        else: 
            currentCountTranslate = str(currentCount)

        if totalCount >= 24:
            totalCountTranslate =  "24+"
        
        else:
            totalCountTranslate = str(totalCount)
        
        
        appMonths.append(currentCountTranslate)
        appMonths.append(totalCountTranslate)
        
        
     
        print(appMonths)
        print(currentCountTranslate)
        print(totalCountTranslate)
        print(openList)
        print(openCount)
        



    
def googleSheetfill(scopesNew,jsonFile,sheetId):
  
    creds = None
    creds= service_account.Credentials.from_service_account_file(
        jsonFile, scopes=scopesNew)


    service = build('sheets', 'v4', credentials=creds)


    
    if dataText[2] == '$0.00':
           
        dataText[2] = translatedNums[1]
        
        if dataText[2] == "$0.00":
            
            dataText[2] = dataText[10]

            if dataText[2] == "$0.00":

                dataText[2] = translatedNums[1]
                print('hi')

            else:
                print("est is 0")
        else:
            pass
    else:
        pass

    

    # Call the Sheets API
    sheet = service.spreadsheets()
    spreadSheetIdsTop = sheet.values().get(spreadsheetId = sheetId,
                            range="Sheet4!A3").execute()


    stateFill = sheet.values().update(spreadsheetId = sheetId,
                            range="Sheet4!A3:B3", valueInputOption="USER_ENTERED", body={"values": [[stateLong]]}).execute()

    ficoFill = sheet.values().update(spreadsheetId = sheetId,
                            range="Sheet4!B3", valueInputOption="USER_ENTERED", body={"values": [[dataText[1]]]}).execute()

    estPayoffFill = sheet.values().update(spreadsheetId = sheetId,
                            range="Sheet4!C3", valueInputOption="USER_ENTERED", body={"values": [[dataText[2]]]}).execute()


    yearFill = sheet.values().update(spreadsheetId = sheetId,
                            range="Sheet4!D3", valueInputOption="USER_ENTERED", body={"values": [[dataText[3]]]}).execute()


    mileageFill = sheet.values().update(spreadsheetId = sheetId,
                            range="Sheet4!E3", valueInputOption="USER_ENTERED", body={"values": [[dataText[4]]]}).execute()
    

    openFill = sheet.values().update(spreadsheetId = sheetId,
                            range="Sheet4!J3", valueInputOption="USER_ENTERED", body={"values": [[openCount[0]]]}).execute()

    
    totalAutoPaymentMonthsFill = sheet.values().update(spreadsheetId = sheetId,
                            range="Sheet4!H3", valueInputOption="USER_ENTERED", body={"values": [[appMonths[1]]]}).execute()
    
    
    paymentsOnCurrentFill = sheet.values().update(spreadsheetId = sheetId,
                            range="Sheet4!I3", valueInputOption="USER_ENTERED", body={"values": [[appMonths[0]]]}).execute()
                            
    
    
    print(spreadSheetIdsTop)
    print(stateFill)
    






