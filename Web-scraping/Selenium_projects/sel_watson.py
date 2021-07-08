from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# path
PATH = ("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(PATH)

url = "http://the-internet.herokuapp.com/login"


# driver.find_element_by_xpath('//*[@id="username"]')
# driver.find_element_by_xpath('//*[@id="password"]').send_keys("SupersecretPassword")
# driver.find_element_by_xpath('//*[@id="login"]/button/i').click()


driver.get(url)