# worker.py
#
# This is a main routine file.
# Implment preference and run it with Python3.

from selenium import webdriver
from selenium.webdriver.common.by import By
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
	except:
		print('Exception occured while \
		trying to do somthing to an element at ' + xpath + '.')

def try_send_keys(driver, find_by_what, find_with, keys):
	try_element(driver, find_by_what, find_with, lambda element:element.send_keys(keys))

def try_click(driver, find_by_what, find_with):
	try_element(driver, find_by_what, find_with, lambda element:element.click())

def try_send_keys_by_xpath(driver, xpath, keys):
	try_send_keys(driver, By.XPATH, xpath, keys)

def try_click_by_xpath(driver, xpath):
	try_click(driver, By.XPATH, xpath)

def try_send_keys_by_id(driver, id, keys):
	try_send_keys(driver, By.ID, id, keys)

def try_click_by_id(driver, id):
	try_click(driver, By.ID, xpath)


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

# Login
def login(driver):
	try_send_keys_by_id(driver, pref.id_stuno_input(), pref.hakbun())
	try_send_keys_by_id(driver, pref.id_password_input(), pref.password())
	try_click_by_xpath(driver, pref.xpath_login_button())

# Type query
def search(driver):
	try_click_by_xpath(driver, pref.xpath_query_by_name_button())
	try_send_keys_by_id(driver, pref.id_query_input(), pref.target())

# Click search and submit forever.
def loop(driver):
	continuos_error_count = 0
	previus_error = False
	while True:
		try:
			# Click search button
			try_click_by_xpath(driver, pref.xpath_search_button())
			time.sleep(0.1)

			# Click submit button
			try_click_by_xpath(driver, pref.xpath_submit_button())
			time.sleep(0.1)

			# Leave a record.
			print('.', end='')
			sys.stdout.flush()

			# Mark it had no error last time.
			previus_error = False

		except KeyboardInterrupt:
			# Finish when keyboard KeyboardInterrupt raised.
			finish(driver)

		except:
			# Finish when encountered over 100 times of
			# continuos error.
			# It means there happened a big problem.
			if previus_error:
				continuos_error_count += 1
				if continuos_error_count > 100:
					# Kill condition
					print('Unrecoverable error occured.')
					finish(driver)
			else:
				# Reset count if error finished.
				continuos_error_count = 0

			print('Unexpected exception. Keep going.')
			sys.stdout.flush()

			# Mark it had error last time.
			previus_error = True

def finish(driver):
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
