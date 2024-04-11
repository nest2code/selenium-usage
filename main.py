from selenium import webdriver
import time
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='/home/umar/Desktop/Intermediate '
                                  'Coding/pythonProject/Selenium_web_development/chromedriver_linux64/chromedriver')
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)

# Here i have added the wikipedia url
driver.get('https://www.wikipedia.org/')
# Here iam trying to get the search bar
data_entry = driver.find_element(By.NAME, 'search')
# Here i enter python word through my script to the search bar
data_entry.send_keys('python')

# I do send the enter key
data_entry.send_keys(Keys.ENTER)

# since my Google Chrome is not compatible with my Google Chrome i decide to use the time module
time.sleep(100)

