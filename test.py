import auto
import pprint

pp = pprint.PrettyPrinter(indent=4, width=250)

inputdata = """USER REF.49011F6C-75C2-401A-A  THIS FORM PRODUCED BY EQUIFAX                   
*******************************************************************************
IDENTITY SCAN WARNING:                                                         
** UNABLE TO PERFORM TELEPHONE VALIDATION DUE TO INSUFFICIENT TELEPHONE INPUT  
*------------------------------------------------------------------------------
     MILITARY LENDING COVERED BORROWER                                         
                                                                               
 DISCLAIMER: THE DEPARTMENT OF DEFENSE ("DOD") COVERED BORROWER DATA ("DATA")  
 IS FROM THE DEFENSE MANPOWER DATA CENTER ("DMDC") BY WAY OF CONTRACT BETWEEN  
 EQUIFAX INFORMATION SERVICES LLC ("EQUIFAX") AND DOD. ALL DOD DATA IS USED    
 AND STORED BY EQUIFAX IN ACCORDANCE WITH ITS LEGAL AND CONTRACTUAL            
 OBLIGATIONS. THE DOD DATA IS NOT PART OF EQUIFAX'S NATIONWIDE CREDIT DATABASE,
 AND EQUIFAX IS REQUIRED TO MAINTAIN THE DATA SEPARATE FROM AND NOT COMMINGLED 
 WITH ANY CREDIT DATA MAINTAINED BY EQUIFAX.                                   
                                                                               
 COVERED BORROWER STATUS:N                                                     
                                                                               
                                                                               
 REFERRAL CONTACT NUMBER  :888-279-8625                                        
                                                                               
*------------------------------------------------------------------------------
** ADDRESS DISCREPANCY- NO SUBSTANTIAL DIFFERENCE OCCURRED                     
                                                                               
                                                                               
                                                                               
                                                                               
                                                                               
*------------------------------------------------------------------------------
FICO SCORE 8-EFX-N                                                             
               00827   00030/00005/00012/00014                                 
TIME SINCE MOST RECENT ACCOUNT OPENING IS TOO SHORT                            
TOO MANY ACCOUNTS WITH BALANCES                                                
LENGTH OF TIME REVOLVING ACCOUNTS HAVE BEEN ESTABLISHED                        
LENGTH OF TIME ACCOUNTS HAVE BEEN ESTABLISHED                                  
                                                                               
*------------------------  IDENTIFICATION INFORMATION  ------------------------
 FILE SINCE-08/16/2006  FAD-08/24/2021   FN-029   IN-                          
                                                                               
 NAME:     PEREZ                                                               
           DANIEL A                                                            
 ADDRESS:  3868 BELLEZA DR                                       VER:          
           CERES, CA 95307                     VARIANCE:         STD:          
           FIRST RPTD:04/00/2016  LAST RPTD:08/17/2021  SOURCE:AUT             
           TELEPHONE:                  RPTD:            SOURCE:                
 FORMER :  1046 YELLOW BRICK RD                                  VER:          
           MODESTO, CA 95351                   VARIANCE:         STD:          
           FIRST RPTD:08/00/2006  LAST RPTD:12/03/2020  SOURCE:EFX             
           TELEPHONE:                  RPTD:            SOURCE:                
 FILE:SSN:608-05-7528  CFM-   MAT-   BDS:11/30/1987   DEATH NOTICE:            
 INQ: SSN:608-05-7528  SSN ISSUED:00/1987          STATE ISSUED:CA             
                            SSN DEATH:                STATE OF DEATH:          
                                                                               
*------------------------  REPORT SUMMARY  --------------------------          
                                                                               
SUM-12/00/2006-08/00/2021   PR-000 COLL-000 ACCTS-024 HC-$       65-$   280550 
    MOP RATES:24-ONES   00-TWOS    00-THREES  00-FOURS  00-FIVES               
              00-SIXES  00-SEVENS  00-EIGHTS  00-NINES  00-OTHER               
    RATE HIST:          00-TWOS    00-THREES  00-FOURS  00-FIVES               
              00-SIXES  00-SEVENS  00-EIGHTS  00-NINES                         
                                                                               
*------------------------  PAYMENT PRACTICE -------------------------          
                                                                               
 REPORTED  !   BALANCE! DFD/DLA  !DURATION  !   DEFER  !MR/ECOA   !MAJ DEL     
 OPENED    ! HIGH CRDT! LAST PYMT!FREQUENCY !   BALLOON!PAST DUE  !CLASS       
 CLOSED    !CRDT LIMIT!  ACT PYMT!SCH PYMT  !   BALLOON!CHARGE OFF!ACTIVITY DES
                                                                               
SYNCB/LA-Z-BOY      /404FF21397* R1            #-XXXXXXXXXXXX1944              
                                       CHARGE ACCT                             
 PYMT HST-1                                                   30-  /60-  /90-  
 08/15/2021!$000000000!08/00/2021!          !          !01/INDIVID!            
 07/09/2021!$000002660!08/00/2021!MONTHLY   !          !          !            
           !$000005000!$000002660!          !          !          !            
MOHELA/DEPT OF ED   /654FZ13214* I1            #-5632848724KM00002             
                                       EDUCATION LOAN                          
 PYMT HST-111111111111/111111111111                           30-  /60-  /90-  
 07/31/2021!$000005908!07/00/2021!120M      !          !70/INDIVID!            
 11/11/2010!$000010500!07/00/2021!MONTHLY   !          !          !            
           !          !          !          !          !          !            
 FIXED RATE                                                                    
MOHELA/DEPT OF ED   /654FZ13214* I1            #-5632848724KM00001             
                                       EDUCATION LOAN                          
 PYMT HST-111111111111/111111111111                           30-  /60-  /90-  
 07/31/2021!$000003337!07/00/2021!120M      !          !70/INDIVID!            
 05/12/2010!$000005500!07/00/2021!MONTHLY   !          !          !            
           !          !          !          !          !          !            
 FIXED RATE                                                                    
JPMCB - HOME LENDING/181FM01268* M1            #-XXXXXXXXX8704                 
                                       CONV RE MORTGAGE                        
 PYMT HST-111111111111/111*1*                                 30-  /60-  /90-  
 08/05/2021!$000278381!08/00/2021! 30Y      !          !17/JOINT  !            
 02/28/2020!$000280550!08/00/2021!MONTHLY   !          !          !            
           !          !$000001681!$000001681!          !          !            
PATELCO CREDIT UNION/162FC02062* I1            #-64493401                      
                                       AUTO                                    
 PYMT HST-111111111111/111111111111                           30-  /60-  /90-  
 07/31/2021!$000011505!07/00/2021! 84M      !          !52/JOINT  !            
 02/20/2017!$000029794!07/00/2021!MONTHLY   !          !          !            
           !          !$000000802!$000000400!          !          !            
 FIXED RATE                                                                    
SYNCB/ASHLEY HOME ST/404FF22868* R1            #-XXXXXXXXXXXX7507              
                                       CHARGE ACCT                             
 PYMT HST-111111111111/111111111111                           30-  /60-  /90-  
 08/03/2021!$000000000!08/00/2021!          !          !40/INDIVID!            
 04/16/2018!$000003997!08/00/2021!MONTHLY   !          !          !            
           !$000006000!$000001674!          !          !          !            
TD AUTO FINANCE     /168BB38713* I1            #-1103539936                    
                                       AUTO                                    
 PYMT HST-11111111                                            30-  /60-  /90-  
 07/31/2021!$000045872!07/00/2021! 84M      !          !08/JOINT  !            
 11/23/2020!$000055888!07/00/2021!MONTHLY   !          !          !            
           !          !$000000818!$000000818!          !          !            
 FIXED RATE                                                                    
THD/CBNA            /485FP00552* R1            #-XXXXXXXXXXXX4177              
                                       CHARGE ACCT                             
 PYMT HST-111111111111/111111EE                               30-  /60-  /90-  
 08/03/2021!$000000000!07/00/2021!          !          !20/INDIVID!            
 12/13/2019!$000005292!07/00/2021!MONTHLY   !          !          !            
           !$000008000!          !          !          !          !            
WELLS FARGO CARD SER/162BB10365* R1            #-XXXXXXXXXXXX8212              
                                       FLEX SPENDING CC                        
 PYMT HST-1111111EEEEE/EE1111111111                           30-  /60-  /90-  
 07/27/2021!$000001437!07/00/2021!          !          !86/INDIVID!            
 04/29/2014!$000007532!07/00/2021!MONTHLY   !          !          !            
           !$000008500!$000002901!$000000025!          !          !            
DISCOVER BANK       /155BB03747* R1            #-XXXXXXXXXXXX3799              
                                       CREDIT CARD                             
 PYMT HST-EEEEEEEEEEEE/EEE111111111                           30-  /60-  /90-  
 07/25/2021!$000000000!03/00/2020!          !          !28/INDIVID!            
 03/13/2019!$000007908!03/00/2020!MONTHLY   !          !          !            
           !$000012500!          !          !          !          !            
SYNCB/LOWES         /404LH00044* R1            #-798192705719                  
                                       CHARGE ACCT                             
 PYMT HST-11111111                                            30-  /60-  /90-  
 07/23/2021!$000000879!07/00/2021!          !          !08/INDIVID!            
 11/08/2020!$000001093!07/00/2021!MONTHLY   !          !          !            
           !$000009000!$000000040!$000000040!          !          !            
AMEX/DSNB           /636BB52112* R1            #-XXXXXXXXXXX8449               
                                       CREDIT CARD                             
 PYMT HST-EEEEEEEEEEEE/EEEEEEEEEEEE                           30-  /60-  /90-  
 12/18/2020!$000000000!01/00/2018!          !          !37/INDIVID!            
 11/02/2017!$000000344!01/00/2018!MONTHLY   !          !          !            
 08/00/2020!$000002000!          !          !          !          !PD/CLOSED   
 ACCOUNT CLOSED BY CREDIT GRANTOR                                              
LOANCARE SERVICING C/832FM09667* M1            #-XXXXXXXXX7661                 
                                       FHA REAL EST MTG MTGE-100185102016040544
 PYMT HST-111111111111/111111111111                           30-  /60-  /90-  
 04/07/2020!$000000000!03/00/2020! 30Y      !          !43/JOINT  !            
 07/14/2016!$000274928!03/00/2020!MONTHLY   !          !          !            
 03/00/2020!          !$000258782!          !          !          !PD/CLOSED   
 FIXED RATE                                                                    
MACY'S/DSNB         /636DC26977* R1            #-440511387640                  
                                       CHARGE ACCT                             
 PYMT HST-                                                    30-  /60-  /90-  
 10/18/2019!$000000000!11/00/2007!          !          !99/INDIVID!            
 10/13/2007!$000000065!11/00/2007!MONTHLY   !          !          !            
 08/00/2014!$000000100!          !          !          !          !PD/CLOSED   
SYNCB/SLEEP TRAIN   /404FF23108* R1            #-XXXXXXXXXXXX9619              
                                       CHARGE ACCT                             
 PYMT HST-                                                    30-  /60-  /90-  
 08/10/2017!$000000000!12/00/2015!          !          !22/INDIVID!            
 10/02/2015!$000001720!12/00/2015!MONTHLY   !          !          !            
 01/00/2016!$000003000!          !          !          !          !PD/CLOSED   
 ACCOUNT CLOSED AT CONSUMERS REQUEST                                           
DEPT OF ED/ASPIRE RE/612FZ19899* I1            #-5632848724KI00002             
                                       EDUCATION LOAN                          
 PYMT HST-                                                    30-  /60-  /90-  
 08/31/2015!$000000000!07/00/2015!131M      !          !27/INDIVID!            
 11/11/2010!$000010500!07/00/2015!MONTHLY   !          !          !            
 08/00/2015!          !          !          !          !          !TRSF/SOLD   
DEPT OF ED/ASPIRE RE/612FZ19899* I1            #-5632848724KI00001             
                                       EDUCATION LOAN                          
 PYMT HST-                                                    30-  /60-  /90-  
 08/31/2015!$000000000!07/00/2015!131M      !          !27/INDIVID!            
 05/12/2010!$000005500!07/00/2015!MONTHLY   !          !          !            
 08/00/2015!          !          !          !          !          !TRSF/SOLD   
CENTRAL STATE CREDIT/802FC00135* I1            #-29306840001                   
                                       AUTO                                    
 PYMT HST-                                                    30-  /60-  /90-  
 09/01/2015!$000000000!08/00/2015! 84M      !          !08/JOINT  !            
 12/09/2014!$000033120!08/00/2015!MONTHLY   !          !          !            
 08/00/2015!          !$000030369!          !          !          !PD/CLOSED   
CAPITAL ONE BANK USA/850BB01498* R1            #-XXXXXXXXXXXX1122              
                                       CREDIT CARD                             
 PYMT HST-                                                    30-  /60-  /90-  
 03/21/2015!$000000000!03/00/2015!          !          !49/INDIVID!            
 01/12/2011!$000000450!03/00/2015!MONTHLY   !          !          !            
 03/00/2015!$000000750!          !          !          !          !PD/CLOSED   
 ACCOUNT CLOSED AT CONSUMERS REQUEST                                           
CAPITAL ONE AUTO FIN/152FA10715* I1            #-XXXXXXXXXXXXX1001             
                                       AUTO                                    
 PYMT HST-                                                    30-  /60-  /90-  
 02/28/2015!$000000000!02/00/2015! 48M      !          !41/JOINT  !            
 09/06/2011!$000013983!02/00/2015!MONTHLY   !          !          !            
 02/00/2015!          !$000001730!$000000000!          !          !PD/CLOSED   
CAPITAL ONE BANK USA/850BB01498* R1            #-XXXXXXXXXXXX4919              
                                       CREDIT CARD                             
 PYMT HST-                                                    30-  /60-  /90-  
 06/28/2014!$000000000!04/00/2014!          !          !90/INDIVID!            
 12/16/2006!$000000416!04/00/2014!MONTHLY   !          !          !            
 06/00/2014!$000000300!          !          !          !          !PD/CLOSED   
 ACCOUNT CLOSED AT CONSUMERS REQUEST                                           
JPMCB - CARD SERVICE/458ON14989* R1            #-XXXXXXXXXXXX0186              
                                       CHARGE ACCT                             
 PYMT HST-                                                    30-  /60-  /90-  
 07/23/2013!$000000000!05/00/2013!          !          !43/INDIVID!            
 11/27/2009!$000000969!05/00/2013!MONTHLY   !          !          !            
 06/00/2011!$000001000!          !          !          !          !PD/CLOSED   
 ACCOUNT CLOSED BY CREDIT GRANTOR                                              
U S DEPARTMENT OF ED/438ZZ10480* I1            #-700002070882336               
                                       EDUCATION LOAN                          
 PYMT HST-                                                    30-  /60-  /90-  
 04/22/2013!$000000000!02/00/2013!120M      !          !18/INDIVID!            
 11/11/2010!$000010500!02/00/2013!MONTHLY   !          !          !            
 03/00/2013!          !$000000077!          !          !          !TRSF/SOLD   
U S DEPARTMENT OF ED/438ZZ10480* I1            #-700002070882236               
                                       EDUCATION LOAN                          
 PYMT HST-                                                    30-  /60-  /90-  
 04/22/2013!$000000000!02/00/2013!120M      !          !18/INDIVID!            
 05/12/2010!$000005500!02/00/2013!MONTHLY   !          !          !            
 03/00/2013!          !$000000042!          !          !          !TRSF/SOLD   
                                                                               
*------------------------  INQUIRY INFORMATION-----------------------          
                                                                               
08/24/2021 CR       655FC02138 ELEMENTS FINANCIAL F                            
11/23/2020 CR       990AN41513 FREMONT CHEVROLET FR                            
11/23/2020 CR       436FA00145 ALLY FINANCIAL                                  
02/05/2020 CR       181ZB17725 CREDCO                                          
02/03/2020 CR       496ZB00954 UNIVERSAL CREDIT SER                            
*029 EQUIFAX INFORMATION SERVICES LLC,           P O BOX 740241,               
    ,ATLANTA,GA,30374-0241,800/685-1111,WWW.EQUIFAX.COM/FCRA              &    
                                                                               
END OF REPORT EQUIFAX AND AFFILIATES - 08/24/2021                              """

inputdata2 = """TBD3 SSM 1994502    GUERRERO,RAYMUNDO 467775855;CA-136 SOUTHWOOD DR/BURLESON TX 
76028;Y-08281983,M-864547B2-FBBC-4A21-A0A2-09E03A8DD833,V-07/026/M91736,RR-BOTH,
VERIFY-RM/J3,T-3F,MLA,
 
 
PAGE 1   DATE  8-24-2021  TIME 13:57:05  VA01  TTX8
 
 RAYMUNDO L GUERRERO              SS: ***             E: STUDENT NTB
*BURLESON TX                      DOB: ***            PH-8174835256
 BURLESON TX 76028                                    RPTD: 8-04 I
 RPTD: 1-21 U 1X
 LAST SUB: 2880824                                    E: PIER 1 IMPORTS
                                                      INCOME IS 1836
 136 SOUTHWOOD DR                                     RPTD: 8-03 I
 BURLESON TX 760282830
 RPTD: 6-17 TO 3-19 U 6X
 
*12120 LONGSTONE DR
 BURLESON TX 760280262
 RPTD: 6-14 TO 4-16 U 2X
 
 RAYMUNDO L GUERRERO JR
 
 ------------------------------- SCORE SUMMARY --------------------------------
 
 FICO CLASSIC RISK 8                  =   732
 
 SCORE FACTORS: 
 18 NUMBER OF ACCOUNTS WITH DELINQUENCY
 10 RATIO OF BALANCE TO LIMIT ON BANK REVOLVING OR OTHER REV ACCTS TOO HIGH
 13 TIME SINCE DELINQUENCY IS TOO RECENT OR UNKNOWN
 14 LENGTH OF TIME ACCTS HAVE BEEN ESTABLISHED
 
 ----------------------------------- TRADES -----------------------------------
 SUBSCRIBER                 OPEN    AMT-TYP1    AMT-TYP2 ACCTCOND   PYMT STATUS
 SUB#   KOB TYP TRM ECOA BALDATE     BALANCE   PYMT LEVEL MOS REV  PYMT HISTORY
 ACCOUNT #               LAST PD   MONTH PAY    PAST DUE  MAXIMUM    BY MONTH
 
*FREEDOM MORTGAGE CORP      5-17  $384,750-O             TRANSFER     CURR ACCT
 2344320 FM R/C 30Y   2  2-28-19                  2-19       (16) BCCCCCCCCCCCC
 101729069                  1-19                                   CCC
 MIN: 100183355009081311
 ** TRANSFERRED TO ANOTHER LENDER **
 
*LOANCARE                   5-17  $384,750-O             TRANSFER     CURR ACCT
 1993102 FM R/C 30Y   2 11-03-17                 11-17       ( 4) BCCC
 6230027518604             10-17                      
 ** TRANSFERRED TO ANOTHER LENDER **
 
*SYNCB/ASHLEY HOMESTORE    11-13    $5,000-L    $2,449-H     PAID     CURR ACCT
 1620500 FF CHG REV   1  2-12-18                  2-18       (51) B000000000000
                            1-15                                   000000000000
 ** CLOSED DUE TO INACTIVITY **
 
 +++++ MORE
 
TBD3 SSM 1994502    GUERRERO,RAYMUNDO 467775855;CA-136 SOUTHWOOD DR/BURLESON TX 
 
 
PAGE 2   DATE  8-24-2021  TIME 13:57:05  VA01  TTX8
 
 SUBSCRIBER                 OPEN    AMT-TYP1    AMT-TYP2 ACCTCOND   PYMT STATUS
 SUB#   KOB TYP TRM ECOA BALDATE     BALANCE   PYMT LEVEL MOS REV  PYMT HISTORY
 ACCOUNT #               LAST PD   MONTH PAY    PAST DUE  MAXIMUM    BY MONTH
 
 JPMCB CARD                 7-04      $400-L    $3,025-H     PAID     CURR ACCT
 3182310 BC CRC REV   1  8-03-17                  8-17       (99) BCCCCCCCCCCCC
                            9-14                                   CCCCCCCCCCCC
 
 QUALTRUST CREDIT UNION    10-13   $12,835-O                 PAID     CURR ACCT
 0720169 FC AUT  48-B 1  2-28-17                  2-17       (41) BCCCCCCCCCCCC
 813424150                  2-17                                   CCCCCCCC-CCC
 
 WELLS FARGO BANK NV NA    12-12    $5,000-O                 PAID     CURR ACCT
 3137970 BB NTE  36   1  7-31-15                  7-15       (32) B--CCCCCCCCCC
 66166162333760001          5-15                                   CCCCCCCCCCCC
 
*AMEX                       2-05      $600-L      $645-H     PAID     CURR ACCT
 1229200 BC CRC REV   1  9-19-12                  9-12       (16) BCCCCCCCCCC0-
                                                                   000
 ** ACCOUNT CLOSED AT CREDIT GRANTOR'S REQUEST **
 
*SYNCB/LOWES                9-15    $1,500-L    $1,321-H     OPEN    CUR WAS 30
 1607340 LZ CHG REV   1  8-20-21        $0        5-20       (72) 0000000000000
                            6-20                                   0CC1CCCCCCCC
 
*WF CRD SVC                 8-04      $800-L    $3,642-H     OPEN    CUR WAS 30
 3270007 BC CRC REV   1  7-26-21        $9        1-21       (99) CCCCCCC1CCCCC
                            7-21       $40-A                       CCCCCCCCCCCC
 
 AMEX                       6-18    $7,137-H                 OPEN     CURR ACCT
 1229200 BC CRC   1   3  8-12-21        $3        8-21       (38) CCC0000000000
                                                                   CC00CCC0CCCC
 
 CITICARDS CBNA             7-14   $18,500-L   $14,204-H     OPEN     CURR ACCT
 1240000 BC FSC REV   1  8-12-21    $7,943        8-21       (86) CCCCCCCCCCCCC
                            8-21      $214                         CCCCCCCCCCCC
 
 FLAGSTAR BANK              5-17  $384,750-O                 OPEN     CURR ACCT
 2880824 BB R/C 30Y   2  8-06-21  $353,921        8-21       (30) CCCCCCCCCCCCC
 6460440413472              7-21    $3,046-A                       CCCCCCCCCCCC
 MIN: 100183355009081311
 
 NELNET LOANS               7-03    $2,625-O                 OPEN     CURR ACCT
 1907757 EL EDU 120   1  7-31-21    $1,182        7-21       (99) CCCC-CCCCCCC-
 00031943774                5-21       $33                         --CCCCCCCCCC
 
 +++++ MORE
 
TBD3 SSM 1994502    GUERRERO,RAYMUNDO 467775855;CA-136 SOUTHWOOD DR/BURLESON TX 
 
 
PAGE 3   DATE  8-24-2021  TIME 13:57:05  VA01  TTX8
 
 SUBSCRIBER                 OPEN    AMT-TYP1    AMT-TYP2 ACCTCOND   PYMT STATUS
 SUB#   KOB TYP TRM ECOA BALDATE     BALANCE   PYMT LEVEL MOS REV  PYMT HISTORY
 ACCOUNT #               LAST PD   MONTH PAY    PAST DUE  MAXIMUM    BY MONTH
 
 NELNET LOANS               4-04    $2,625-O                 OPEN     CURR ACCT
 1907757 EL EDU 120   1  7-31-21    $1,182        7-21       (99) CCCC-CCCCCCC-
 00031943874                5-21       $33                         --CCCCCCCCCC
 
 DEPT OF ED/NAVIENT         1-14    $2,750-O                 OPEN     CURR ACCT
 1997398 EL EDU  62   1  7-31-21      $293        7-21       (91) CCCCCCCCCCCCC
 94448933231E001201401>     7-21                                   CCCCCCCCCCCC
 >27
 
 WELLS FARGO DEALER SVC     5-19   $47,722-O                 OPEN     CURR ACCT
 3828796 FA AUT  76   1  6-30-21   $34,183        6-21       (25) CCCCCCCCCCCCC
 513810116066               6-21      $753                         CCCCCCCCCC-C
 
 --------------------------------- INQUIRIES ----------------------------------
 FACTUAL DATA            6-22-20  2698670 FR            R/E 
 ADVANTAGE/ADVANTAGE CR  6-03-20  1198181 FM            R/E 
 ADVANTAGE/ADVANTAGE CR  3-05-20  1198181 FM            R/E 
 FACTUAL DATA            3-01-20  2698670 FR            R/E 
 
 --------------------------------- MESSAGES -----------------------------------
 SSN MATCHES
 
 MLA NO RECORD FOUND
 
 END -- EXPERIAN"""

print("Equifax data extraction:\n")
autolines = auto.get_equifax_auto_data(inputdata)
pp.pprint(autolines)

print("\n\n")

print("Non-equifax data extraction:\n")
autolines2 = auto.get_nonequifax_auto_data(inputdata2)
pp.pprint(autolines2)


