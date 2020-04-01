import selenium
from selenium import webdriver

print(selenium.__version__)
driver = webdriver.Ie(r'C:\IEDriverServer.exe')

driver.get("http://dho.netmarble.net/main.asp")
driver.implicitly_wait(5)

inputElement = driver.find_element_by_xpath('//*[@id="login_id"]').send_keys('********')
inputElement = driver.find_element_by_xpath('//*[@id="login_pwd"]').send_keys('********')
inputElement = driver.find_element_by_xpath('//*[@id="_clf_submit_button"]').click()
driver.implicitly_wait(5)

# Game Start
inputElement = driver.find_element_by_xpath('//*[@id="divGameStart"]').click()
driver.implicitly_wait(10)

driver.quit()
