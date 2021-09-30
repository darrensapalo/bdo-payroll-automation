from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from config import GetConfig

config = GetConfig()

selectedBank = config['bank'][0]
print(selectedBank)

baseURL = selectedBank['baseURL']
print(baseURL)

driver = webdriver.Chrome()
driver.get(baseURL)

assert selectedBank['name'] in driver.title

username = selectedBank['username']
elem = driver.find_element_by_name("channelUserID")
elem.clear()
elem.send_keys(username)

print("I've displayed your username, but you have to be the one to write the password.")
try:
    WebDriverWait(driver, 30).until(lambda x: 'Google' in driver.title or 'Facebook' in driver.title)

    print("Oh wow, you're in google or facebook!")
except TimeoutException as e:
    driver.close()
    print("You need to enter your password within 30 seconds.")
    pass
except: 
    print("Something went wrong")
    driver.close()

print("Redirecting you back to BDO.")
driver.get(baseURL)

driver.close()

#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
# driver.close()
