from Common.openbrowser import open_site
import datetime
import time
from utils.ExcelParse import excel_parse
from utils.db_connect import DB
from Common.login import login_user
from Common.AccountSelection import accountseclection
from Common.enterAccountDetails import enter_account_details
from Common.DataProcessing import process_excel

#DB connection
db=DB(10)
db.dbConnection()

#Extracting the user list
df_users = excel_parse("BOA_Logins.xlsx",0)

#Extracting thr Address details
df_address_details_all = excel_parse("BOA_Logins.xlsx",1)

print("==============Original set of users ==============")
print(df_users)

#Using Pandas module, we fetch oly applicable users for execution
df_users=df_users.loc[df_users['Execution']=='Yes']
df_users.reset_index(drop=True,inplace=True)

print("==============Eligible set of users ==============")
print(df_users)
print("==============Users Address details ==============")
print(df_address_details_all)

df_address_details_all['Zip'].apply(str)

#Navigate to Site
driver=open_site("https://www.bankofamerica.com/")

#Looping through list of users
counter=1
for pos, userid in df_users['User'].iteritems():
    #Data processing
    password = df_users['Password'][pos]
    print("User set ----> "+str(counter)+"\nuser ID : {}\nPassword :{}".format(userid,password))


    # fetch details from excel sheet
    Fname, Lname, Address1, City, State, Zip, Phone, Email, Confirm_email = process_excel(df_address_details_all=df_address_details_all,userid=userid)

    ##Bank Of America -- Functional flow
    #Login functionality

    driver = login_user(driver=driver, userid=userid, password=password)

    if Fname is not None:
        #Account selection and get started
        driver = accountseclection(driver=driver)

        #Enter details in webpage

        driver = enter_account_details(driver, Fname=Fname, Lname=Lname, Address1=Address1, City=City, State=State, Zip=Zip, Phone=Phone, Email=Email, Confirm_email=Confirm_email,userid=userid)
    counter=counter+1
driver.quit()