from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException        
import time

driver = webdriver.Chrome()
# Uncomment the following line to use Firefox instead
# driver = webdriver.Firefox()

driver.implicitly_wait(30)


def begin_step(_1, _2):
	print('begin_step ' + _1)
	pass

def load_page(url):
	print('load_page ' + url)
	driver.get(url)

def verify_page_load_status():
	time.sleep(1)

def wait_for_page_to_load():
	time.sleep(1)

def click_element_by_id(id, _1, _2):
	print('click_element_by_id ' + id)
	element = driver.find_element_by_id(id)
	ActionChains(driver).click(element).perform()

def click_element_by_xpath(xpath, _1, _2):
	print('click_element_by_xpath ' + xpath)
	element = driver.find_element_by_xpath(xpath)
	ActionChains(driver).click(element).perform()

def select_window_by_index(index):
	print('select_window_by_index ' + index)
	driver.switch_to.window(driver.window_handles[int(index) - 1])

def set_password_by_id(id, value, _1, _2):
	print('set_password_by_id ' + value)
	type_keys_by_id(id, value, _1, _2)

def type_keys_by_id(id, value, _1, _2):
	print('type_keys_by_id ' + value)
	element = driver.find_element_by_id(id)
	element.send_keys(value)

def type_keys_by_xpath(xpath, value, _1, _2):
	print('type_keys_by_xpath ' + value)
	element = driver.find_element_by_xpath(xpath)
	element.send_keys(value)

def type_keys_by_css(css, value, _1, _2):
	print('type_keys_by_css ' + value)
	element = driver.find_element_by_css(css)
	element.send_keys(value)

def type_text_by_xpath(xpath, value, _1, _2):
	print('type_keys_by_xpath ' + value)
	element = driver.find_element_by_xpath(xpath)
	element.send_keys(value)

def click_element_by_name(name, _1, _2):
	print('click_element_by_name ' + name)
	element = driver.find_element_by_name(name)
	ActionChains(driver).click(element).perform()

def get_selector(selector_type_str):
	selector = None
	if selector_type_str == "id":
		selector = By.ID
	if selector_type_str == "xpath":
		selector = By.XPATH

	return selector

def wait_for_element_visibility(selector_type_str, locator, timeout):
	print('wait_for_element_visibility ' + locator)
	selector = get_selector(selector_type_str)

	element = WebDriverWait(driver, 400).until(
        EC.visibility_of_element_located((selector, locator))
    )

def is_element_present(selector_type_str, locator):
	print('is_element_present ' + locator)
	selector = get_selector(selector_type_str)
	try:
		element = driver.find_element(selector, locator)
	except NoSuchElementException as e:
		return False

	return True

def assert_element_check(selector_type_str, locator):
	print('assert_element_check ' + locator)
	selector = get_selector(selector_type_str)

	assert is_element_present(selector_type_str, locator) == True

def assert_location(url, _):
	print('assert_location ' + url)
	assert driver.current_url == url

def navigate_to(url):
	print('navigate_to ' + url)
	driver.get(url)

def assert_text_present(text, _):
	print('assert_text_present ' + text)
	assert text in driver.page_source
