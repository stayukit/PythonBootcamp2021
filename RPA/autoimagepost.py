# autoimagepost.py
# input text and upload picture to post on web

import os
import wikipedia
from selenium import webdriver
import time

wikipedia.set_lang('th')

imgfile = os.listdir()
mainpath = os.getcwd()
print(imgfile)
print(mainpath)
print('++++++++++++')

wordlist = []
pathlist = []

for img in imgfile:
	if img[-3:] == 'jpg' or img[-3:] == 'png':
		fn = img.split('.')[0]
		# split orange.jpg to ['orange','jpg'] and select [0]
		wordlist.append(fn)
		# autosetpath for image uploading process
		path = os.path.join(mainpath,img)
		print(path)
		pathlist.append(path)


alltitle = []
alldata = []
allprice = [33339000, 450 , 800, 6300, 350]

for wl in wordlist:
	try:
		data = wikipedia.summary(wl)
		page = wikipedia.page(wl)
		title = page.title

	except:
		title = wl
		data = 'No data'

	alltitle.append(title)
	alldata.append(data[:200])
	print('Topic: {}'.format(title))
	print(data)
	print(page.content)
	print('++++++++++++')

######################################

login='http://www.uncle***.com/login/'
addpage = 'http://www.uncle***.com/addproduct/'

web=webdriver.Chrome()
web.get(login)

time.sleep(1)

email=web.find_element_by_id('username')
email.send_keys('***@gmail.com')
time.sleep(1)
pw=web.find_element_by_id('password')
pw.send_keys('1234')

'''
to use selenium package to press enter:
from selenium.webdriver.common.keys import Keys
pw.send_keys(Keys.RETURN)
'''

bt=web.find_element_by_xpath('/html/body/div[2]/form/button')
bt.click()
time.sleep(1)

# Add products
web.get(addpage)
time.sleep(2)

for n,p,d,i in zip(alltitle,allprice,alldata,pathlist):

	addname=web.find_element_by_id('name')
	addname.send_keys(n)
	time.sleep(1)
	addprice=web.find_element_by_id('price')
	addprice.send_keys(p)
	time.sleep(1)
	adddetail=web.find_element_by_id('detail')
	adddetail.send_keys(d)
	time.sleep(5)
	addimg=web.find_element_by_id('photo')
	addimg.send_keys(i)
	time.sleep(5)
	bt=web.find_element_by_xpath('/html/body/div[2]/form/button')
	bt.click()
	time.sleep(1)
