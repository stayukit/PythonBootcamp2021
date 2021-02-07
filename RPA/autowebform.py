# autowebform.py
# uncle-machine.com
from selenium import webdriver
import wikipedia
import time

login='http://www.uncle**.com/login/'
addpage = 'http://www.uncle**.com/addproduct/'

web=webdriver.Chrome()
web.get(login)

time.sleep(1)

email=web.find_element_by_id('username')
email.send_keys('@gmail.com')
time.sleep(1)
pw=web.find_element_by_id('password')
pw.send_keys('')

'''
use selenium to press enter:
from selenium.webdriver.common.keys import Keys
pw.send_keys(Keys.RETURN)
'''

bt=web.find_element_by_xpath('/html/body/div[2]/form/button')
bt.click()

time.sleep(1)

web.get(addpage)



