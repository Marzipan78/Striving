from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# path
PATH = ("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(PATH)

url = "https://weather.com/weather/tenday/l/San+Francisco+CA?canonicalCityId=dfdaba8cbe3a4d12a8796e1f7b1ccc7174b4b0a2d5ddb1c8566ae9f154fa638c"

driver.get(url)
desc= []

print(driver.find_element_by_xpath('//*[@id="titleIndex2"]/div[2]/span'))


