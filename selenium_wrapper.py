# selenium_wrapper.py
#
# This file contains usefull ready-to-use functions
# about finding and interacting with element safely.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from util import printnow

# Find element with element_info, and try do_what.
#
# This function catches only StaleElementReferenceException,
# leaving other exceptions unhandled.
# So when you call it you MUST catch exceptions.
#
# @param driver			      The chromedriver.
# @param find_by_what	      Kind of element_info e.g. by.Xpath
# @param find_with            Information of element corresponding with find_by_what.
# @param do_what		      What to do to the element.
#
# @return True if successfully done, False if StaleElementReferenceException raised.
def try_do_element(driver, find_by_what, find_with, do_what, print_error=True):
	try:
		element = WebDriverWait(driver, 120).until( \
		EC.presence_of_element_located((find_by_what, find_with)))
		do_what(element)
		return True

	except StaleElementReferenceException:
		if (print_error):
			printnow('!', end='')
		return False

def try_send_keys(driver, find_by_what, find_with, keys, print_error=True):
	return try_do_element(driver, find_by_what, find_with, lambda element:element.send_keys(keys), print_error=print_error)

def try_click(driver, find_by_what, find_with, print_error=True):
	return try_do_element(driver, find_by_what, find_with, lambda element:element.click(), print_error=print_error)

def try_send_keys_by_xpath(driver, xpath, keys, print_error=True):
	return try_send_keys(driver, By.XPATH, xpath, keys, print_error=print_error)

def try_click_by_xpath(driver, xpath, print_error=True):
	return try_click(driver, By.XPATH, xpath, print_error=print_error)

def try_send_keys_by_id(driver, id, keys, print_error=True):
	return try_send_keys(driver, By.ID, id, keys, print_error=print_error)

def try_click_by_id(driver, id, print_error=True):
	return try_click(driver, By.ID, xpath, print_error=print_error)
