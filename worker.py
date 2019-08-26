# worker.py
#
# This is a main routine file.
# Implment preference and run it with Python3.

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

import preference as pref

# Find element with element_info, and try to click it.
#
# @param driver			The chromedriver.
# @param find_by_what	Kind of element_info e.g. by.Xpath
# @param find_with		Information of element corresponding with find_by_what.
# @param do_what		What to do to the element.
def try_element(driver, find_by_what, find_with, do_what):
	try:
		element = WebDriverWait(driver, 120).until( \
		EC.presence_of_element_located((find_by_what, find_with)))
		do_what(element)
	except StaleElementReferenceException as e:
		print('StaleElementReferenceException occured while \
		trying to do somthing to an element at ' + xpath + '.')

def try_send_keys(driver, find_by_what, find_with, keys):
	try_element(driver, find_by_what, find_with, lambda element:element.send_keys(keys))

def try_click(driver, find_by_what, find_with):
	try_element(driver, find_by_what, find_with, lambda element:element.click())

def try_send_keys_by_xpath(driver, xpath, keys):
	try_send_keys(driver, by.XPATH, xpath, keys)

def try_click_by_xpath(driver, xpath):
	try_click(driver, by.XPATH, xpath)

def try_send_keys_by_id(driver, id, keys):
	try_send_keys(driver, by.ID, id, keys)

def try_click_by_id(driver, id):
	try_click(driver, by.ID, xpath)


###########################################################
# Subroutines
###########################################################

# Initialize options
def get_options():
	options = webdriver.ChromeOptions()
	if pref.headless():
		options.add_argument('headless')
		options.add_argument('window-size=1920x1080')
		options.add_argument("disable-gpu")
	return options

# Initialize driver with options.
def get_driver():
	driver = webdriver.Chrome(pref.chromedriver_path(), chrome_options=get_options())
	driver.implicitly_wait(10)
	return driver

# Switch to frame of id.
def switch_frame_by_id(driver, id):
	driver.get(pref.url())
	frame = driver.find_element_by_id(id)
	driver.switch_to.frame(frame)


###########################################################
# Routines
###########################################################

# Do initial things.
# This webpage is wrapped in a frame. So we need to switch to the fram.
def init():
	driver = get_driver()
	switch_frame_by_id(driver, pref.id_frame())
	return driver

def login(driver):
	try_send_keys_by_id(driver, pref.id_stuno_input(), pref.hakbun())
	try_send_keys_by_id(driver, pref.id_password_input(), pref.password())
	try_click_by_xpath(driver, pref.xpath_login_button())

def search(driver):
	try_click_by_xpath(driver, pref.xpath_query_by_name_button())
	try_send_keys_by_id(driver, pref.id_query_input(), pref.target())

def loop(driver):
	try:
		while True:
			try_click_by_xpath(driver, pref.xpath_search_button())
			time.sleep(0.1)
			try_click_by_xpath(driver, pref.xpath_submit_button())
			time.sleep(0.1)

			print('.', end='')

	except KeyboardInterrupt:
		driver.quit()
		print('\nBye.')
		sys.exit()


###########################################################
# Execution
###########################################################

driver = init()
print('Driver initialized.')

login(driver)
print('Logged in.')

search(driver)
print('Query typed.')

print('Starting loop.')
loop(driver)
