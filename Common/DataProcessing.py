import pandas as pd

def process_excel(df_address_details_all,userid):
    #Fname, Lname, Address1, City, State, Zip, Phone, Email, Confirm_email ='','','','','','','','',''
    Fname, Lname, Address1, City, State, Zip, Phone, Email, Confirm_email = None,None,None,None,None,None,None,None,None
    df_address_details = df_address_details_all.loc[df_address_details_all['User'] == userid]
    if df_address_details.empty:
        print("Result : We have no address details...User ID cannot be created")
        return Fname,Lname,Address1,City,State,Zip,Phone,Email,Confirm_email
    else:
        #print(df_address_details)

        df_address_details.reset_index(drop=True,inplace=True)
        #print(df_address_details)
        # Extracting information from excel
        Fname = df_address_details['Fname']
        Lname = df_address_details['Lname']
        Address1 = df_address_details['Address1']
        City = df_address_details['City']
        State = df_address_details['State']
        Zip = str(df_address_details['Zip'])
        Phone = df_address_details['Phone']
        Email = df_address_details['Email']
        Confirm_email = df_address_details['Confirm email']
        return Fname,Lname,Address1,City,State,Zip,Phone,Email,Confirm_email
