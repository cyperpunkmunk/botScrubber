
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
import time

import extractDataTransunion

from dateutil import parser
from datetime import datetime

import loanOffN4

import auto



# dataText 
dataText = []

# A date has day 'd', month 'm' and year 'y'
class Date:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y
 
# To store number of days in all months from
# January to Dec.
monthDays = [31, 28, 31, 30, 31, 30,
             31, 31, 30, 31, 30, 31]



             

#loginfunciton
def login(drive , homeUrl, username, password):
    
    #home webpage lgoin
    drive.get(homeUrl)
    drive.find_element_by_xpath('//*[@id="username"]').send_keys(username)
    drive.find_element_by_xpath('//*[@id="password"]').send_keys(password)
    drive.find_element_by_xpath('//*[@id="submit-button"]').click()
    print('login successful')
    
    drive.implicitly_wait(200)

    drive.find_element_by_xpath('//*[@id="dashboard-container"]/div/div[2]/a').click()




def getAppData(Url,drive):



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
    

    

    loanOffN4.fillLoData(drive, ppqVer, aprRate)
    
    
    
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


    # county list for spreadsheet function
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
    
    

   

    

try:
    def getBureauData(drive):

        drive.implicitly_wait(400)
        
        drive.find_element_by_xpath('//*[@id="bureau"]').click()

        drive.implicitly_wait(400)

        bureauData = drive.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div/div/div[3]/div[3]/span/div/pre').text


        global bankruptcyInfo


        # bankruptcy,Br includes car, br status, Last Listed Date 
        bankruptcyInfo = ['NO_BR','N/A', 'N/A', '']
        

        # Checks file for "PUBLIC RECORD" section, and extracts the RPTD date.
        # Input: string of whole file
        # Output: (boolean, string)
        def isBankruptcy(text):
            global isBankrupt
            global date
            isBankrupt = False
            date = ''

            
            def countLeapYears(d):
    
                years = d.y
        
                # Check if the current year needs to be considered
                # for the count of leap years or not
                if (d.m <= 2):
                    years -= 1
        
                # An year is a leap year if it is a multiple of 4,
                # multiple of 400 and not a multiple of 100.
                return int(years / 4) - int(years / 100) + int(years / 400)
            
                
            # This function returns number of days between two
            # given dates
            def getDifference(dt1, dt2):

                # COUNT TOTAL NUMBER OF DAYS BEFORE FIRST DATE 'dt1'   
                # initialize count using years and day
                n1 = dt1.y * 365 + dt1.d
        
                # Add days for months in given date
                for i in range(0, dt1.m - 1):
                    n1 += monthDays[i]
        
                # Since every leap year is of 366 days,
                # Add a day for every leap year
                n1 += countLeapYears(dt1)
        
                # SIMILARLY, COUNT TOTAL NUMBER OF DAYS BEFORE 'dt2'
            
                n2 = dt2.y * 365 + dt2.d
                for i in range(0, dt2.m - 1):
                    n2 += monthDays[i]
                n2 += countLeapYears(dt2)
            
                # return difference between two counts
                return (n2 - n1)
        
            
            def translatedData(originalLone):
                
                
                # returns a list [month, day, year]
                translatedDate = originalLone.split("/")
                
                #  setting todays dat to a variable to use later
                today = datetime.today()
                # formatting the data to mm/dd/YYYY 
                todayformated = today.strftime("%m/%d/%Y")
                #sliptting each number by the / to form a list to be able to fill for the dt1 variable
                currentDate = todayformated.split("/")
                
                # variables to see the dates we get back
                d1 = int(currentDate[0]),int(currentDate[1]),int(currentDate[2])
                d2 = int(translatedDate[1]), int(translatedDate[0]) ,int(translatedDate[2])

                # day, month, year
                dt1 = Date(int(translatedDate[1]), int(translatedDate[0]) ,int(translatedDate[2]))
                dt2 = Date(int(currentDate[0]),int(currentDate[1]),int(currentDate[2]))

                # difference of the two dates as a variable
                datesSubtracted = getDifference(dt1, dt2)

                # if the difference is greater than or equal to 4 years (1460 days) 
                if datesSubtracted >= 1460:
                    bankruptcyInfo[0] = "YES_4_plus_years_ago"
                #if its less than four years
                else:
                    bankruptcyInfo[0] = "YES_Recent"
                
                # updates the third parameter in the Br info
                bankruptcyInfo[2] = "Discharged"

                # fills in the last listed date in the br info 
                bankruptcyInfo[3] = originalLone



                
                
                print(translatedDate)
                print(d1)
                print(d2)
                print(datesSubtracted)


                
            
            
            
            
            # Equifax:
            eqRegex = re.compile(r'BKRPTCY-FILED:.*\n\s*RPTD:\s*([0-9,/]*)')
            eqPR = 'PUBLIC RECORD INFORMATION'

            if eqPR in text:
                
                isBankrupt = True
                match = eqRegex.search(text)
                date = match.group(1)
                
                # updates the first parameter in the loan info 
                translatedData(date)


                

            # Non Equifax:
            neqRegex = re.compile(r'PUBLIC RECORDS\s*-*\n(.*)\n')
            neqPR = 'PUBLIC RECORDS'

            if neqPR in text:
                isBankrupt = True
                match = neqRegex.search(text)
                date = match.group(1)[34:44].strip()

                print(date)
                

            # standardize date formatting to MM/DD/YYYY
            if len(date) > 0:
                
                date = parser.parse(date).strftime("%m/%d/%Y")
                
                translatedData(date)
                
                #searching to see if there is an auto loan in the br
                lum = re.search("BK7DISC" , text)
                
                # i f there is a auto loan included in the br
                if lum:
                    bankruptcyInfo[1] = "YES"
                else:
                    bankruptcyInfo[1] = 'NO'

            

        

            print(isBankrupt, date)



        # returns true and the date of the bankruptcy if there is one
        isBankruptcy(bureauData)


        




        x = re.search("THIS FORM PRODUCED BY EQUIFAX" , bureauData)
        y = re.search("TRANSUNION CREDIT REPORT" , bureauData)

        # if we get a locked at consumers request error
        s = re.search("FILE LOCKED AT CONSUMERS REQUEST", bureauData)

        # if we get a frozen file error
        q = re.search("FREEZE ON CREDIT REPORT" , bureauData)

        # if we get file frozen due to federal legislation error
        g = re.search("FILE FROZEN DUE TO FEDERAL LEGISLATION." , bureauData)
        
        ## transferable list for our spreadsheet to use when filling in data
        
        # the total count of the months on every auto loan 
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



        
        # bankruptcy var if there isint one
            

        
            
        if x:

            print('this was made with equifax')
            returnedData = auto.get_equifax_auto_data(bureauData)

            
            # variable to keep track of the total number of months
            equifaxTotalMonths = 0

            # variable to keep track of total open loans
            equifaxTotalOpenLoans = 0

            # variable to keep track of number of payments on current loan
            equifaxPaymentsOnCurrent = 0



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


                            try:
                                # checking the lists to see if they match without being reversed
                                if (int(translatedForEquifaxNumbers[0]) == int(currentLoanPayoffs[0])):

                                    # adding the months from ths loan to the total payments on current if they match this way
                                    equifaxPaymentsOnCurrent += int(cmd[1])

                                    print('this is the current loan matched without being reversed')
                                    
                                    break                        
                            
                            except:
                                print("not a match")

                            try:
                                if (int(translatedForEquifaxNumbers[1]) == int(currentLoanPayoffs[1])):

                                    equifaxPaymentsOnCurrent += int(cmd[1])

                                    print('this is the current loan matched without being reversed')

                                    break   
                            except:
                                print('not a match')
                            
                            try:
                                # checking to see if they match while being reversed
                                if (int(translatedForEquifaxNumbers[0]) == int(currentLoanPayoffs[1])):
                                    
                                    # adding the months from ths loan to the total payments on current if they match this way
                                    equifaxPaymentsOnCurrent += int(cmd[1])

                                    print('these numbers matched reversed')
                                    
                                    break
                            except:
                                print('not a match')
                            
                            try:
                                if(int(translatedForEquifaxNumbers[0]) == int(currentLoanPayoffs[0])):

                                    # adding the months from ths loan to the total payments on current if they match this way
                                    equifaxPaymentsOnCurrent += int(cmd[1])

                                    print('these numbers matched reversed')
                                    
                                    break
                            except:
                                print('not a match')
                                
                            else:
                                print('this isint a match')
                                    
                                

                            print(translatedForEquifaxNumbers)
                            
                            print(currentLoanPayoffs)



                        # if it isnt open this is what we do when its closed
                        else:
                            print('CLOSED LOAN')


                        
            print(equifaxTotalMonths)
            print(equifaxTotalOpenLoans)
            print(equifaxPaymentsOnCurrent)

            # totalPaymentHistory, paymentsOnCurrent, openAutoLines
            googleSheetNumberfilter(equifaxTotalMonths, equifaxPaymentsOnCurrent, equifaxTotalOpenLoans)

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

            print('credit bureau error')


            

        elif q:

            # the total count of the months on every auto loan 
            totalLoanCount.append('24+')
            
            # the total number of open loans
            totalOpenLoanCount.append("1")
            
            # The number of months on the current
            currentLoanMonths.append("12+")

            print('credit bureau error')
        
        
        # if we get file frozen due to federal legislation error
        elif g:

            # the total count of the months on every auto loan 
            totalLoanCount.append('24+')
            
            # the total number of open loans
            totalOpenLoanCount.append("1")
            
            # The number of months on the current
            currentLoanMonths.append("12+")

            print('credit bureau error')


        else: 
            
            
            print('not eqifax')
            returnedData = auto.get_nonequifax_auto_data(bureauData)
            
            

            
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

except:
    print('bureau data error')  
        

        


    
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

    bankruptcySelector = sheet.values().update(spreadsheetId = sheetId,
                            range="Sheet4!G3", valueInputOption="USER_ENTERED", body={"values": [[bankruptcyInfo[0]]]}).execute()
    
    brIncludesCar = sheet.values().update(spreadsheetId = sheetId,
                            range="Sheet4!G5", valueInputOption="USER_ENTERED", body={"values": [[bankruptcyInfo[1]]]}).execute()

    brStatus = sheet.values().update(spreadsheetId = sheetId,
                            range="Sheet4!H5", valueInputOption="USER_ENTERED", body={"values": [[bankruptcyInfo[2]]]}).execute()
    
    lastListedDate = sheet.values().update(spreadsheetId = sheetId,
                            range="Sheet4!I5", valueInputOption="USER_ENTERED", body={"values": [[bankruptcyInfo[3]]]}).execute()


   
    

    print(spreadSheetIdsTop)
    print(stateFill)

 
    






