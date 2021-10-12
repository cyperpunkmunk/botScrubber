import re
import os

def get_equifax_auto_data(inputdata):

    #open data file
    """
    try:
        f = open(inputdata, "rt")
        #print("opened succesfully")

        d = f.readlines()

        f.close()
    except:
        #print("did not open")
        raise Exception('Could not open file.')
    """

    d = inputdata.split('\n')

    #find AUTO
    linenum = 0
    output = []
    for l in d:
        #regex to find "AUTO"
        #if re.match(r"                                       AUTO", l):
        if re.match(r"^\s*AUTO", l):
            auto_details = {}
            #print("found")
            #print(linenum)
            autostr = d[linenum-1] + d[linenum] + d[linenum+1] + d[linenum+2] + d[linenum+3] + d[linenum+4]
            #auto_details["raw_data"] = autostr

            #Check whether auto loan is closed or open
            if "PD/CLOSED" in d[linenum+4]:
                auto_details["status"] = "CLOSED"
            else:
                auto_details["status"] = "OPEN"

            #Check number of months
            """
            reg = re.compile(r"\d{2}M")
            m = re.search(r"\d{2}M", d[linenum+2])
            if m:
                auto_details["months"] = m.group(0)
            else:
                auto_details["months"] = 'N/A'
            """
            m = re.search(r"\s!(\d+)/", d[linenum+2]) #added space regex to reject date and get correct months.
            if m:
                auto_details["months"] = m.group(0)[2:-1]
            else:
                auto_details["months"] = 'N/A'

            # Get prices
            price1 = re.search(r'\$\d{9}', d[linenum+2])
            price2 = re.search(r'\$\d{9}', d[linenum+3])
            auto_details["prices"] = []
            if price1:
                auto_details["prices"].append('$'+price1.group(0)[1:].lstrip('0'))
            if price2:
                auto_details["prices"].append('$'+price2.group(0)[1:].lstrip('0'))

            output.append(auto_details)
        linenum = linenum + 1

    return output


def get_nonequifax_auto_data(inputdata):

    #open data file
    """
    try:
        f = open(inputdata, "rt")
        #print("opened succesfully")

        d = f.readlines()

        f.close()
    except:
        #print("did not open")
        return
    """

    d = inputdata.split('\n')

    #find AUT
    linenum = 0
    output = []
    for l in d:
        #find "AUT"
        if "AUT" in l[12:15]:
            auto_details = {}
            #print("found")
            #print(linenum)
            autostr = d[linenum-1] + d[linenum] + d[linenum+1]
            #auto_details["raw_data"] = autostr

            #Check whether loan is closed or open
            if "PAID" in d[linenum-1]:
                auto_details["status"] = "CLOSED"
            elif "OPEN" in d[linenum-1]:
                auto_details["status"] = "OPEN"
            else:
                auto_details["status"] = "N/A"

            #Get months
            #months = re.search(r"\((\d+)\)", d[linenum])
            months = re.search(r"\(\s?\d+\)", d[linenum])
            if months:
                if months.group(0)[1].isspace():
                    auto_details["months"] = months.group(0)[2:-1]
                else:
                    auto_details["months"] = months.group(0)[1:-1]
            else:
                auto_details["months"] = "N/A"

            #Get prices
            auto_details["prices"] = []
            price1 = d[linenum-1][35:42].strip()
            price2 = d[linenum][35:42].strip()
            price3 = d[linenum+1][35:42].strip()
            if price1:
                auto_details["prices"].append(price1)
            if price2:
                auto_details["prices"].append(price2)
            if price3:
                auto_details["prices"].append(price3)           
                
            output.append(auto_details)
        linenum = linenum + 1

    return output
