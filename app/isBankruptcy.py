import re
from dateutil import parser

# Checks file for "PUBLIC RECORD" section, and extracts the RPTD date.
# Input: string of whole file
# Output: (boolean, string)
def isBankruptcy(text):
    
    isBankrupt = False
    date = ''

    # Equifax:
    eqRegex = re.compile(r'BKRPTCY-FILED:.*\n\s*RPTD:\s*([0-9,/]*)')
    eqPR = 'PUBLIC RECORD INFORMATION'

    if eqPR in text:
        isBankrupt = True
        match = eqRegex.search(text)
        date = match.group(1)

    # Non Equifax:
    neqRegex = re.compile(r'PUBLIC RECORDS\s*-*\n(.*)\n')
    neqPR = 'PUBLIC RECORDS'

    if neqPR in text:
        isBankrupt = True
        match = neqRegex.search(text)
        date = match.group(1)[34:44].strip()
    
    # standardize date formatting to MM/DD/YYYY
    if len(date) > 0:
        date = parser.parse(date).strftime("%m/%d/%Y")
    
    print(isBankrupt, date)
    return(isBankrupt, date)