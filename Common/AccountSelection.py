import time
from selenium.webdriver.support.ui import Select

def accountseclection(driver):
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

    try:
        driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys("00831")
        driver.find_element_by_id("go-button-zip-modal").click()
    except:
        pass

    savings_account = input("Do you want to add a savings account(Y/N):")
    if savings_account.upper() == 'Y':
        # driver.find_element_by_id("rb-rewards-savings-account").click()
        driver.find_element_by_xpath("//input[@type='radio']").click()
    else:
        driver.find_element_by_xpath("//input[@type='rb-savings-account-none']").click()

    driver.find_element_by_id("isBoaClient").click()
    driver.find_element_by_id("go-to-application-mediumup").click()
    driver.implicitly_wait(3)
    time.sleep(6)
    driver.find_element_by_name("Link_continue_guest").click()
    time.sleep(4)
    return driver