from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

bdo_personal_login = "https://online.bdo.com.ph/sso/login";

driver = webdriver.Chrome()
driver.get(bdo_personal_login)

assert "Banco De Oro" in driver.title

elem = driver.find_element_by_name("channelUserID")
elem.clear()
elem.send_keys("darrensapalo")
print("I've displayed your username, but you have to be the one to write the password.")
try:
    WebDriverWait(driver, 30).until(lambda x: 'Google' in driver.title or 'Facebook' in driver.title)

    print("Oh wow, you're in google or facebook!")
except TimeoutException as e:
    print("You need to enter your password within 30 seconds.")
    pass

print("Redirecting you back to BDO.")
driver.get(bdo_personal_login)

#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
# driver.close()
