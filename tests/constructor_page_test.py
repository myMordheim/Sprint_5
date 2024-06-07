from selenium.webdriver.common.by import By
from selenium import webdriver
from locators.login_page import *
from locators.order_page import *
from URLs import *
from data import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestConstructorPage():

    def test_transfer_to_bun(self, driver):
        driver.get(login_page_url)
        driver.find_element(By.XPATH, login_email_input).send_keys(user_data[0])
        driver.find_element(By.XPATH, login_password_input).send_keys(user_data[1])
        driver.find_element(By.XPATH, login_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, order_button)))
        driver.find_element(By.XPATH, selector_sauce).click()
        driver.find_element(By.XPATH, selector_buns).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, selector_buns)))
        assert 'tab_type_current' in driver.find_element(By.XPATH, parent_buns).get_attribute('class')

    def test_transfer_to_sauce(self, driver):
        driver.get(login_page_url)
        driver.find_element(By.XPATH, login_email_input).send_keys(user_data[0])
        driver.find_element(By.XPATH, login_password_input).send_keys(user_data[1])
        driver.find_element(By.XPATH, login_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, selector_sauce)))
        driver.find_element(By.XPATH, selector_sauce).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, parent_suace)))
        assert 'tab_type_current' in driver.find_element(By.XPATH, parent_suace).get_attribute('class')

    def test_transfer_to_fillings(self, driver):
        driver.get(login_page_url)
        driver.find_element(By.XPATH, login_email_input).send_keys(user_data[0])
        driver.find_element(By.XPATH, login_password_input).send_keys(user_data[1])
        driver.find_element(By.XPATH, login_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, order_button)))
        driver.find_element(By.XPATH, selector_fillings).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, parent_fillings)))
        assert 'tab_type_current' in driver.find_element(By.XPATH, parent_fillings).get_attribute('class')
