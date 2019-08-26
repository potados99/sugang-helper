#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

import time
import sys
import subprocess
import datetime

import extra

def element_or_false(element):
	if element:
		return element
	else:
		return false

def find_search_button(driver):
	return element_or_false(driver.find_element_by_xpath('//*[text()="조회"]'))
	
def find_submit_button(driver):
	xpath = '//table[@class="dataT"]/tbody/tr[' + str(extra.target_index() + 1) + ']'
	return element_or_false(driver.find_element_by_xpath(xpath))

# get driver and wait
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
	
# get driver ready
driver = webdriver.Chrome('./chromedriver', chrome_options=options)
driver.implicitly_wait(10)
print('driver ready')

# load page
driver.get('http://sugang.inu.ac.kr')
print('entered http://sugang.inu.ac.kr')

# switch frame
frame = driver.find_element_by_id('sukang')
driver.switch_to.frame(frame)
print('switch frame')

# log in
driver.find_element_by_id('stuno').send_keys('201701562')
driver.find_element_by_id('pwd').send_keys(extra.password())
driver.find_elements_by_class_name('btn_login')[0].click()
print('log in')

time.sleep(0.5)

# search for target
driver.find_element_by_xpath('//*[text()="과목명(코드)조회"]').click()
time.sleep(0.5)
driver.find_element_by_id('custom').send_keys(extra.target())
print('write query')

time.sleep(0.5)

# find search button
search_button = find_search_button(driver)

# start loop
print('start loop')
clickCount = 0
try:
	while True:
		search_button.click()
		time.sleep(0.1)
		WebDriverWait(driver, 120).until(find_submit_button).click()
		time.sleep(0.1)
	
		clickCount += 1
		if clickCount > 10:
			print('10 clicks')
			clickCount = 0
except KeyboardInterrupt:
	driver.quit()
	print('bye')
	sys.exit()
