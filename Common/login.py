import datetime
def login_user(driver,userid,password):
    driver.find_element_by_name("onlineId1").clear()
    driver.find_element_by_name("onlineId1").send_keys(userid)
    driver.find_element_by_name("passcode1").clear()
    driver.find_element_by_name("passcode1").send_keys(password)

    driver.find_element_by_id("saveOnlineId").click()
    driver.save_screenshot("LoginPage " + str(userid) + str(datetime.datetime.now())[:10] + ".png")
    # driver.save_screenshot("LoginPage.png")

    driver.maximize_window()
    return driver

