from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Logs import logs_file
from selenium.webdriver import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotVisibleException, TimeoutException, NoSuchElementException, ElementNotInteractableException, InvalidElementStateException, InvalidSelectorException as EX

"""This class is the parent of all the page classes"""
"""It contains all the common action methods and utilities for all the pages"""

log = logs_file.get_logs()

class SeleniumHelper:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, page_url):
        self.driver.get(page_url)

    def click(self, locator):
        try:
            self.driver.find_element(list(locator.keys())[0], list(locator.values())[0]).click()
        except EX as e:
            print("Exception! Can't click on the element")

    def send_keys(self, locator):
        try:
            self.driver.find_element(list(locator.keys())[0], list(locator.values())[0]).send_keys()
        except EX as e:
            print("Exception! Can't click on the element")

    def insert_text_in_input_field(self, locator, input_text):
        try:
            self.driver.find_element(list(locator.keys())[0], list(locator.values())[0]).send_keys(input_text)
        except EX as e:
            print("Exception! Can't click on the element")

    def wait_till_element_is_present(self, locator, timeout=10):
        flag = False
        try:
            log.info(f"Waiting {timeout} seconds for element {list(locator.values())[0]} presence")
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((list(locator.keys())[0], list(locator.values())[0])))
            log.info(f"Element found")
            flag = True
        except Exception as e:
            log.error(
                f"Element {list(locator.values())[0]} not found after waiting {timeout} seconds")
        return flag
    
    def click_elements(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            self.driver.execute_script("arguments[0].click();", element)
        except EX as e:
            print("Exception! Can't click on the element")
    
    def input_element(self, locator, text):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)
        except EX as e:
            print("Exception! Can't click on the element")

    def get_element_text(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text

    def get_title(self):
        return self.driver.title

    def get_element_attribute(self, locator, attribute_name):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.get_attribute(attribute_name)

    def verify_element_displayed(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except:
            return False