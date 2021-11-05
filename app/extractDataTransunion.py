import re

# Formats string dollar values from '$123.5K' to '123000.00'
def formatDollars(dol):
    dol = dol.strip().replace('$', '')
    if len(dol) == 0:
        return '0.00'
    if 'K' in dol:
        dol = dol.replace('K', '')
        dol = float(dol) * 1000
    else:
        dol = float(dol)
    return str(dol)



# Extracts data from a single three-row set, passed in as a string, and outputs to this format:
# ('OPEN', '4', ['35,967.0', '36,058.0', '800.0'])
def extractSingleData(text):
    fieldSizes = [13, 10, 8, 9, 10, 9, 13, 5, 23, 8, 9, 10, 9, 18, 5, 18, 8, 9, 22, 3, 13]

    loc = 0
    fields = []
    for f in fieldSizes:
        fields.append(text[loc: loc+f].strip())
        loc += f
    open = fields[18]
    if len(open) == 0:
        open = "OPEN"
    months = fields[19]
    p1 = formatDollars(fields[3])
    p2 = formatDollars(fields[17])
    loanType = fields[15].strip()

    result = (open, months, [p1, p2])
    return [result, loanType]



# Extracts data from the whole file, passed in as a string, and outputs to this format: 
# [('OPEN', '4', ['35,967.0', '36,058.0', '800.0']),
# ('OPEN', '4', ['35,967.0', '36,058.0', '800.0']),
# ('OPEN', '4', ['35,967.0', '36,058.0', '800.0'])]
def extractAllData(text):

    header = """T R A D E S                                                                 
SUBNAME      SUBCODE   OPENED  HIGHCRED TERMS     MAXDELQ  PAYPAT  1-12 MOP 
ACCOUNT#               VERFIED CREDLIM  PASTDUE   AMT-MOP  PAYPAT 13-24     
ECOA COLLATRL/LOANTYPE CLSD/PD BALANCE  REMARKS                MO 30/60/90  
"""
    footer = """
----------------------------------------------------------------------------
I N Q U I R I E S  """

    # remove all but table section
    start = text.index(header) + len(header)
    end=text.index(footer)
    trimmed = text[start:end]



    results = []
    divider = r"\n\s+\n"


    for row in re.split(divider, trimmed):
        r = extractSingleData(row)
        if "AUTO" in r[1]:
            results.append(r[0])

    return results