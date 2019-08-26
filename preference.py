# preference.py
# 
# This is a perference file. 
# You can make your own implementation of private.py
# or implement functions below directly.

import private

# This script facilitates Selenium and ChromeDriver.
def chromedriver_path():
	return private.get_chromedriver_path()

# Student number
def hakbun():
	return private.get_id()

# Password
def password():
	return private.get_password()

# Target subject
def target():
	return private.get_target()

# Target index in search result
# The index starts from zero.
def target_index():
	return private.get_target_index()
