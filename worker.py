# worker.py
#
# This is a main routine file.
# Implment preference and run it with Python3.

import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium_wrapper import try_send_keys_by_xpath
from selenium_wrapper import try_click_by_xpath
from selenium_wrapper import try_send_keys_by_id
from selenium_wrapper import try_click_by_id
from selenium_wrapper import try_do_element

from util import printnow
from util import print_time

import preference as pref


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
	try_do_element(driver, By.XPATH, pref.xpath_login_button(), lambda element:printnow(element.text))
	try_click_by_xpath(driver, pref.xpath_login_button())

# Type query
def search(driver):
	try_click_by_xpath(driver, pref.xpath_query_by_name_button())
	try_do_element(driver, By.XPATH, pref.xpath_query_by_name_button(), lambda element:printnow(element.text))
	try_send_keys_by_id(driver, pref.id_query_input(), pref.target())

# Click search and submit forever.
def loop(driver):
	continuous_error_count = 0
	previous_error = False
	print_dot_count = 0
	print_time_count = 200 # Print it at start
	one_time_task_done = False

	while True:
		try:
			# Click search button
			success_search = try_click_by_xpath(driver, pref.xpath_search_button(), print_error=False)
			time.sleep(pref.click_delay())

			# Click submit button
			success_submit = try_click_by_xpath(driver, pref.xpath_submit_button(), print_error=False)
			time.sleep(pref.click_delay())

			# Dot should be display onley when 10 successes past.
			if success_search and success_submit:
				print_dot_count += 1

				# To test we've got the right element.
				if not one_time_task_done:
					# Print search button text.
					try_do_element(driver, By.XPATH, pref.xpath_search_button(), \
					lambda element:printnow(element.text))

					# Print submit button text.
					try_do_element(driver, By.XPATH, pref.xpath_submit_button(), \
					lambda element:printnow(element.text))
					one_time_task_done = True
			else:
				# Reset count. The dot is replaced by [!].
				print_dot_count = 0

				# Print error here because we gave False to [print_error]
				printnow('!', end='')

			previous_error = False

		except KeyboardInterrupt:
			# Finish when keyboard KeyboardInterrupt raised.
			finish(driver)

		except:
			# On unexpected exception, the normal countings no longer work.
			if previous_error:
				continuous_error_count += 1
				printnow('?(' + str(continuous_error_count) + ')', end='')
			else:
				continuous_error_count = 0
				printnow('?', end='')

			previous_error = True

		finally:
			# Time should be display wheather clicks are succeeded or failed.
			print_time_count += 1

			# Print dot once a 10 successes
			if print_dot_count >= 10:
				printnow('.', end='')
				print_dot_count = 0

			# Print time once a 200 successes
			if print_time_count >= 200:
				print_time()
				print_time_count = 0

			# Finish when encountered over 100 times of
			# continuos unknown error.
			# It means there happened a big problem.
			if continuous_error_count > 100:
				print_time()
				printnow('Unrecoverable error occured.')
				finish(driver)

def finish(driver):
		driver.quit()
		printnow('\nBye.')
		sys.exit()


###########################################################
# Execution
###########################################################

driver = init()
printnow('Driver initialized.')

login(driver)
printnow('Logged in.')

search(driver)
printnow('Query typed.')

printnow('Starting loop.')
loop(driver)
