
from selenium.webdriver.support.ui import Select
from Common.openbrowser import open_site
import datetime
import time
from utils.ExcelParse import excel_parse
from utils.db_connect import dbConnection
from Common.login import login_user

#DB connection
dbConnection()

#Extracting the user list
df_users = excel_parse("BOA_Logins.xlsx",0)

#Extracting thr Address details
df_address_details_all = excel_parse("BOA_Logins.xlsx",1)
print(df_address_details_all)
df_address_details_all['Zip'].apply(str)

#Navigate to Site

driver=open_site("https://www.bankofamerica.com/")

for pos, userid in df_users['User'].iteritems():
    password = df_users['Password'][pos]
    print("user ID : {}\nPassword :{}".format(userid,password))

    driver=login_user(driver=driver,userid=userid,password=password)

    df_address_details = df_address_details_all.loc[df_address_details_all['User'] == userid]
    df_address_details = df_address_details.reset_index()
    print(df_address_details)

    #Extracting information from excel
    Fname = df_address_details['Fname']
    Lname = df_address_details['Lname']
    Address1 = df_address_details['Address1']
    City = df_address_details['City']
    State = df_address_details['State']
    Zip = str(df_address_details['Zip'])
    Phone = df_address_details['Phone']
    Email = df_address_details['Email']
    Confirm_email = df_address_details['Confirm email']



    p="//div[@class='products-container']//span[@class='show-for-large-up']"
    #print(driver.find_element_by_xpath(p).text)

    driver.find_element_by_class_name("open-account").click()
    no_of_products=driver.find_elements_by_xpath("//div[contains(text(),'started')]")
    print("No of services available are " + str(len(no_of_products)))

    products_available=driver.find_elements_by_xpath("//div[@class='title-container']/h4")

    for pro in products_available:
        print(pro.text)

    driver.find_element_by_xpath("//div[contains(text(),'started')]").click()
    driver.implicitly_wait(4)
    driver.find_element_by_xpath("//a[@class='open-cta']").click()
    driver.switch_to.window((driver.window_handles[1]))

    pin_code=driver.find_element_by_xpath("(//input[@type='text'])[3]")

    try:
        driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys("00831")
        driver.find_element_by_id("go-button-zip-modal").click()
    except:
        pass


    savings_account=input("Do you want to add a savings account(Y/N):")
    if savings_account.upper()=='Y':
        #driver.find_element_by_id("rb-rewards-savings-account").click()
        driver.find_element_by_xpath("//input[@type='radio']").click()
    else:
        driver.find_element_by_xpath("//input[@type='rb-savings-account-none']").click()

    driver.find_element_by_id("isBoaClient").click()

    driver.find_element_by_id("go-to-application-mediumup").click()
    driver.implicitly_wait(3)
    time.sleep(6)
    driver.find_element_by_name("Link_continue_guest").click()

    time.sleep(4)

    driver.find_element_by_xpath("//input[@id='zz_name_tb_fnm_v_1']").send_keys(Fname)
    driver.find_element_by_id("zz_name_tb_lnm_v_1").send_keys(Lname)
    driver.find_element_by_id("zz_addr_tb_line1_v_1").send_keys(Address1)
    driver.find_element_by_id("zz_addr_tb_city_v_1").send_keys(City)
    sel=Select(driver.find_element_by_id("zz_addr_lb_state_v_1"))

    sel.select_by_visible_text("Maine")
    time.sleep(3)
    driver.implicitly_wait(3)
    driver.find_element_by_id("zz_addr_tb_zip_v_1").clear()
    driver.implicitly_wait(3)
    driver.find_element_by_id("zz_addr_tb_zip_v_1").send_keys(Zip)
    driver.find_element_by_id("zz_phn_tb_ppno_v_1").send_keys("9885679707")
    driver.find_element_by_id("zz_email_tb_addr_v_1").send_keys(Email)
    driver.find_element_by_id("zz_email_tb_readdr_v_1").send_keys(Confirm_email)
    driver.find_element_by_xpath("//label[@for='zz_citz_lb_uscit_no_v_1-real']/input").click()
    driver.save_screenshot("new account"+str(userid)+str(datetime.datetime.now())[:10]+".png")
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.back()
    driver.back()


driver.quit()