
from __future__ import print_function
from inspect import _empty
from typing import Text
from httplib2 import Response
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import re
from googleapiclient.discovery import build
from selenium.webdriver.chrome.options import Options
from google.oauth2 import service_account


import extractDataTransunion
import isBankruptcy
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


    # county list for spreasheet function
    global countyTranslated
    countyTranslated = []

    # function to translate the county data we get from the app to be able to be used in the google sheet
    def countyHandler():

        # setting the county from our list to a variable that we can use later    
        countyFilter = dataText[5]
        
        # removing "county" from the text
        countyTranslate = countyFilter.replace(" County", "")

        countyTranslated.append(countyTranslate)

        


    countyHandler()
        

    



def getBureauData(drive):

    drive.implicitly_wait(400)
    
    drive.find_element_by_xpath('//*[@id="bureau"]').click()

    drive.implicitly_wait(400)

    bureauData = drive.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div/div/div[3]/div[3]/span/div/pre').text

    x = re.search("THIS FORM PRODUCED BY EQUIFAX" , bureauData)
    y = re.search("TRANSUNION CREDIT REPORT" , bureauData)

    # if we get a locked at consumers request error
    s = re.search("FILE LOCKED AT CONSUMERS REQUEST", bureauData)

    # if we get a frozen file error
    q = re.search("FREEZE ON CREDIT REPORT" , bureauData)
        
    
    ## transferable list for our spreadsheet to use when filling in data
    
    # the total count of the months on evry auto loan 
    global totalLoanCount
    totalLoanCount = []
    # the total number of open loans
    global totalOpenLoanCount
    totalOpenLoanCount = []
    # The number of months on the current
    global currentLoanMonths
    currentLoanMonths = []

    
    
    # function to scale the numbers down for the google sheet
    def googleSheetNumberfilter(totalPaymentHistory, paymentsOnCurrent, openAutoLines):
            
        # if our numbers are over or equal to 24
        if totalPaymentHistory >= 24:
                
            # change the total number to 24+ since thats the max the spreadsheet takes 
            totalPaymentHistory = '24+'
            totalLoanCount.append(totalPaymentHistory)
            
        else:
            # if its less than 12 we just turn it it to a readable string for the spreadsheet
            totalPaymentHistoryString = str(totalPaymentHistory)
            totalLoanCount.append(totalPaymentHistoryString)

            
            
        # if our numbers are over or equal to 12
        if paymentsOnCurrent >= 12:
                
            # change the total number to 12+ since thats the max the spreadsheet takes 
            paymentsOnCurrent = '12+'
            currentLoanMonths.append(paymentsOnCurrent)
            
        else:
            # if its less than 12 we just turn it it to a readable string for the spreadsheet
            paymentsOnCurrentString = str(paymentsOnCurrent)
            currentLoanMonths.append(paymentsOnCurrentString)
                
            
            
        # if our numbers are over or equal to 5
        if openAutoLines >= 5:
                
            # change the total number to 5+ since thats the max the spreadsheet takes 
            openAutoLines = '5+'
            totalOpenLoanCount.append(openAutoLines)
            
        else:
            # if its less than 12 we just turn it it to a readable string for the spreadsheet
            paymentsOnCurrentString = str(openAutoLines)
            totalOpenLoanCount.append(paymentsOnCurrentString)



    
        

    
        
    if x:

        print('this was made with equifax')
        returnedData = auto.get_equifax_auto_data(bureauData)

        isBankruptcy.isBankruptcy(bureauData)
        

        
        
        
        # variable to keep track of the total number of months
        equifaxTotalMonths = 0

        # variable to keep track of total open loans
        equifaxTotalOpenLoans = 0

        # variable to keep track of number of payments on current loan
        equifaxPaymentsOnCurent = 0

        # getting each loan
        for loan in returnedData:
            
            # giving each loan a variable to be able to store its data
            cmd = loan['status'], loan['months'], loan["prices"]
            
            if cmd[0] == "N/A":
                print('LOAN WITH INVALID STATUS')
            
            else:
                # if th staus is valid then it checks to see if the months are valid
                if cmd[1] == "N/A":
                    print('LOAN WITH INVALID MONTHS')
                
                else:
                    
                    # turning each months from loan into and intiger to use later 
                    equifaxMonthsStrToInt = int(cmd[1])
                    # adding each loan months to the total months loan 
                    equifaxTotalMonths += equifaxMonthsStrToInt

                    # checking to see if it is an open or closed loan
                    if cmd[0] == "OPEN":
                        
                        # if its an open loan we add it to the total amount of open loans
                        equifaxTotalOpenLoans += 1

                        # giving the loan payoff list a variable
                        equifaxLoanPayoff = (cmd[2])
                        
                        # checking each number in the list
                        currentLoanPayoffs = []
                        
                        #translating the numbers so we can compare them to the numbers the bureau gives us
                        translatedForEquifaxNumbers = []

                        # getting the number from this loan and putting them into a list to compare to the payoff numbers on the app 
                        for number in equifaxLoanPayoff:
                            
                            # if the loan gives back a special case of a value with 0
                            if number == '$':
                                
                                # filling the empty value with 0
                                numTranslated = number.replace('$', "0")

                                # appending to the list
                                currentLoanPayoffs.append(numTranslated)
                            
                            else:
                                # translating the numbers to match later
                                numTranslated = number.replace('$', "")
                                
                                # appending to the list
                                currentLoanPayoffs.append(numTranslated)
                        
                        # getting each number from the translated numbers var to compare them to the data in a new list with the numbers that are translated for equifax
                        for num in translatedNums:
                            

                            #getting rid of the comma in with the first variable
                            translatedNum = num.replace(",", "")

                            # getting rid of the $ s we can turn it into an int later
                            translatedNum1 = translatedNum.replace("$", "")
                            
                            # getting rid of the .00 with the second variable
                            translatedNum2 = translatedNum1.replace(".00", "") 
                            
                            # appending the numbers to the list to be compared later
                            translatedForEquifaxNumbers.append(translatedNum2)

                        # checking the lists to see if they match without being revesed
                        if (int(translatedForEquifaxNumbers[0]) == int(currentLoanPayoffs[0])) or (int(translatedForEquifaxNumbers[1]) == int(currentLoanPayoffs[1])):

                            # adding the months from ths loan to the total payments on current if they match this way
                            equifaxPaymentsOnCurent += int(cmd[1])

                            print('this is the current loan matched without being reversed')

                            
                        # checking to see if they match while being reversed
                        elif (int(translatedForEquifaxNumbers[0]) == int(currentLoanPayoffs[1])) or (int(translatedForEquifaxNumbers[0]) == int(currentLoanPayoffs[0])):
                            

                            # adding the months from ths loan to the total payments on current if they match this way
                            equifaxPaymentsOnCurent += int(cmd[1])

                            print('these numbers matched reversed')
                            
                            
                        else:
                            
                            print('this isint a match')
                                
                               

                        print(translatedForEquifaxNumbers)
                        
                        print(currentLoanPayoffs)



                    # if it isnt open this is what we do when its closed
                    else:
                        print('CLOSED LOAN')


                    
        print(equifaxTotalMonths)
        print(equifaxTotalOpenLoans)
        print(equifaxPaymentsOnCurent)

        # totalPaymentHistory, paymentsOnCurrent, openAutoLines
        googleSheetNumberfilter(equifaxTotalMonths, equifaxPaymentsOnCurent, equifaxTotalOpenLoans)

        print('new data')

        print(totalLoanCount)
        print(currentLoanMonths)
        print(totalOpenLoanCount)






    
    

    
    elif y:
        print('this was made with the new lender')

        # variable to keep track of the total number of months
        transUnionTotalMonths = 0

        # variable to keep track of total open loans
        transUnionTotalOpenLoans = 0

        # variable to keep track of number of payments on current loan
        transUnionPaymentsOnCurent = 0

        
        transUnionData = extractDataTransunion.extractAllData(bureauData)

        # getting each loan
        for loan in transUnionData:
            
            # setting the loans string to an intiger variable to add to the total months 
            transUnionTotalMonthsInt = int(loan[1])

            # Adding the total months intiger to the total months
            transUnionTotalMonths += transUnionTotalMonthsInt

            # if the loan is open
            if loan[0] == 'OPEN':
                
                print(loan)

                # if its an open loan we add it to the total amount of open loans
                transUnionTotalOpenLoans += 1

                # giving the loan payoff list a variable ['20300.0', '10800.0']
                transUnionLoanPayoffList = loan[2]
                

                # checking each number in the list
                currentLoanPayoffs = []
                        
                #translating the numbers so we can compare them to the numbers the bureau gives us
                translatedForTransUnionNumbers = []

                
                for number in transUnionLoanPayoffList:
                    
                    #getting rid of the comma in with the first variable
                    translatedLoanPayoff = number.replace(".0", "")

                    #  comparing the first three numbers siince the rest are zeros
                    translatedLoanPayoff1 = translatedLoanPayoff[0:3]

                    #appending the translated numbers to the list
                    currentLoanPayoffs.append(translatedLoanPayoff1)

                
                print(currentLoanPayoffs)
                
                
                for num in translatedNums:

                    # getting rid of the comma in with the first variable
                    translatedNum = num.replace(",", "")

                    # getting rid of the $ s we can turn it into an int later
                    translatedNum1 = translatedNum.replace("$", "")
                            
                    # getting rid of the .00 with the second variable
                    translatedNum2 = translatedNum1.replace(".00", "") 

                    #  comparing the first three numbers since the rest are zeros
                    translatedNum3 = translatedNum2[0:3]
                            
                    # appending the numbers to the list to be compared later
                    translatedForTransUnionNumbers.append(translatedNum3)
                
                print(translatedForTransUnionNumbers)

                
                # checking the lists to see if they match without being revesed
                if (int(translatedForTransUnionNumbers[0]) == int(currentLoanPayoffs[0])) or (int(translatedForTransUnionNumbers[1]) == int(currentLoanPayoffs[1])):

                    # adding the months from ths loan to the total payments on current if they match this way
                    currentLoanMonthsInt = loan[1]
                    
                    transUnionPaymentsOnCurent += int(currentLoanMonthsInt)

                    print('this is the current loan matched without being reversed')
 
                else:
                                
                    print('this isint a match')

            

            print(loan)
        
        print(transUnionTotalMonths)
        print(transUnionTotalOpenLoans)
        print(transUnionPaymentsOnCurent)
        
        # totalPaymentHistory, paymentsOnCurrent, openAutoLines
        googleSheetNumberfilter(transUnionTotalMonths, transUnionPaymentsOnCurent, transUnionTotalOpenLoans)

        
    
    
    elif s:

        # the total count of the months on every auto loan 
        totalLoanCount.append('24+')
        
        # the total number of open loans
        totalOpenLoanCount.append("1")
        
        # The number of months on the current
        currentLoanMonths.append("12+")


        

    elif q:


        # the total count of the months on every auto loan 
        totalLoanCount.append('24+')
        
        # the total number of open loans
        totalOpenLoanCount.append("1")
        
        # The number of months on the current
        currentLoanMonths.append("12+")
        




    else: 
        
        
        print('not eqifax')
        returnedData = auto.get_nonequifax_auto_data(bureauData)
        
        isBankruptcy.isBankruptcy(bureauData)

        
        # variable to keep track of the total number of months
        nonEquifaxTotalMonths = 0

        # variable to keep track of total open loans
        nonEquifaxTotalOpenLoans = 0

        # variable to keep track of number of payments on current loan
        nonEquifaxPaymentsOnCurent = 0
        
        for data in returnedData:
            
            # giving each loan a variable to be able to store its data
            cmd = data['status'], data['months'], data["prices"]
            
            print(cmd)

            if cmd[0] == "N/A":
                
                print('INVALID LOAN')
            
            else:

                # turning each months from loan into and intiger to use later 
                nonEquifaxMonthsStrToInt = int(cmd[1])
                
                # adding each loan months to the total months loan 
                nonEquifaxTotalMonths += nonEquifaxMonthsStrToInt

                # checking to see if it is an open or closed loan
                if cmd[0] == "OPEN":
                    
                    # if its an open loan we add it to the total amount of open loans
                    nonEquifaxTotalOpenLoans += 1

                    # giving the loan payoff list a variable
                    nonEquifaxLoanPayoff = (cmd[2])
                        
                    # checking each number in the list
                    currentLoanPayoffs = []
                        
                    #translating the numbers so we can compare them to the numbers the bureau gives us
                    translatedForNonEquifaxNumbers = []

                    for num in nonEquifaxLoanPayoff:
                        
                        # getting rid of the $ with the second variable
                        translatedN = num.replace("$", "")

                        translatedN1 = translatedN.replace(",", "") 
                                
                        # appending the numbers to the list to be compared later
                        currentLoanPayoffs.append(translatedN1)
                        

                    # getting each number from the translated numbers var to compare them to the data in a new list with the numbers that are translated for equifax
                    for num in translatedNums:

                        #getting rid of the comma in with the first variable
                        translatedNum = num.replace(",", "")

                        # getting rid of the $ s we can turn it into an int later
                        translatedNum1 = translatedNum.replace("$", "")
                            
                        # getting rid of the .00 with the second variable
                        translatedNum2 = translatedNum1.replace(".00", "") 
                            
                        # appending the numbers to the list to be compared later
                        translatedForNonEquifaxNumbers.append(translatedNum2)


                    # checking the lists to see if they match without being revesed
                    if (int(translatedForNonEquifaxNumbers[0]) == int(currentLoanPayoffs[0])) or (int(translatedForNonEquifaxNumbers[1]) == int(currentLoanPayoffs[1])):

                        # adding the months from ths loan to the total payments on current if they match this way
                        nonEquifaxPaymentsOnCurent += int(cmd[1])

                        print('this is the current loan matched without being reversed')
                    
                    # checking to see if they match while being reversed
                    elif (int(translatedForNonEquifaxNumbers[0]) == int(currentLoanPayoffs[1])) or (int(translatedForNonEquifaxNumbers[0]) == int(currentLoanPayoffs[0])):
                            

                        # adding the months from ths loan to the total payments on current if they match this way
                        nonEquifaxPaymentsOnCurent += int(cmd[1])

                        print('these numbers matched reversed')
                            
                            
                    else:
                            
                        print('this isint a match')

                    

                    print(currentLoanPayoffs)
                    print(translatedForNonEquifaxNumbers)  

                
                else:
                    print('CLOSED LOAN')
                
                
        
        print(nonEquifaxTotalMonths)
        print(nonEquifaxTotalOpenLoans)
        print(nonEquifaxPaymentsOnCurent)

        # totalPaymentHistory, paymentsOnCurrent, openAutoLines
        googleSheetNumberfilter(nonEquifaxTotalMonths, nonEquifaxPaymentsOnCurent, nonEquifaxTotalOpenLoans)        

        print('new data')

        print(totalLoanCount)
        print(totalOpenLoanCount)
        print(currentLoanMonths)

        


    
        

                
        
        







        



    
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
                            range="Sheet4!J3", valueInputOption="USER_ENTERED", body={"values": [[totalOpenLoanCount[0]]]}).execute()

    
    totalAutoPaymentMonthsFill = sheet.values().update(spreadsheetId = sheetId,
                            range="Sheet4!H3", valueInputOption="USER_ENTERED", body={"values": [[totalLoanCount[0]]]}).execute()
    
    
    paymentsOnCurrentFill = sheet.values().update(spreadsheetId = sheetId,
                            range="Sheet4!I3", valueInputOption="USER_ENTERED", body={"values": [[currentLoanMonths[0]]]}).execute()
    
    
    countyFill = sheet.values().update(spreadsheetId = sheetId,
                            range="Sheet4!A4", valueInputOption="USER_ENTERED", body={"values": [[countyTranslated[0]]]}).execute()


   
    

    print(spreadSheetIdsTop)
    print(stateFill)

 
    






