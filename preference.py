# preference.py
#
# This is a perference file.
# You can make your own implementation of private.py
# or implement functions below directly.

import private

###########################################################
# Environments.
###########################################################

# This script facilitates Selenium and ChromeDriver.
def chromedriver_path():
	return private.get_chromedriver_path()

# Whether to go headless(no gui).
def headless():
	return True


###########################################################
# Your personal information.
###########################################################

# The URL of the sungang page.
def url():
	return private.get_url()

# Student number.
def hakbun():
	return private.get_id()

# Password.
def password():
	return private.get_password()

# Target subject.
def target():
	return private.get_target()

# Target index in search result.
# The index starts from zero.
def target_index():
	return private.get_target_index()


###########################################################
# Do not modify below unless you know what you are doing.
###########################################################

# Id of wrapper frame.
def id_frame():
	return 'sukang'

# Id of hakbun input.
def id_stuno_input():
	return 'stuno'

# Id of password input.
def id_password_input():
	return 'pwd'

# Id of custom query input.
def id_query_input():
	return 'custom'

# Xpath to login button
def xpath_login_button():
	return xpath_by_text("로그인")

# Xpath to 'query by name' button.
def xpath_query_by_name_button():
	return xpath_by_text("과목명(코드)조회")

# Xpath to search button.
def xpath_search_button():
	return xpath_by_text("조회")

# Xpath to submit button.
def xpath_submit_button():
	index_str = str(target_index() + 1)
	return '//table[@class="dataT"]/tbody/tr[' + index_str + ']/td[@class="last"]/a'

# Create xpath that describes element(s) where text is same as given parameter.
def xpath_by_text(text):
	return '//*[text()="' + str(text) + '"]'

# Delay between clicks
def click_delay():
	return 0.1
