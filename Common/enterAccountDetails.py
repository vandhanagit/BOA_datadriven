from selenium.webdriver.support.ui import Select
import time
import datetime

def enter_account_details(driver,userid,Fname,Lname,Address1,City,Zip,Email,Confirm_email,State,Phone,):
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
