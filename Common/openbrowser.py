from selenium import webdriver

def open_site(url):
    driver=webdriver.Chrome(executable_path="C:\\Users\mkottak\git\intermix\IMX\GAP_Intermix\\target\classes\webdriver\\chromedriver.exe")
    driver.get(url)
    return driver
