from selenium.webdriver.common.by import By
from selenium import webdriver
from locators.login_page import *
from locators.order_page import *
from locators.registration_page import *
from locators.forgot_password_page import *
from data import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class Test_login_page():

    def test_login_from_main_page(self):
        driver = webdriver.Chrome()
        driver.get(login_page_url)
        driver.find_element(By.XPATH, login_email_input).send_keys(user_data[0])
        driver.find_element(By.XPATH, login_password_input).send_keys(user_data[1])
        driver.find_element(By.XPATH, login_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, order_button)))
        assert driver.current_url == order_page_url
        driver.quit()

    def test_login_from_personal_account(self):
        driver = webdriver.Chrome()
        driver.get(login_page_url)
        driver.find_element(By.XPATH, login_personal_account_button).click()
        driver.find_element(By.XPATH, login_email_input).send_keys(user_data[0])
        driver.find_element(By.XPATH, login_password_input).send_keys(user_data[1])
        driver.find_element(By.XPATH, login_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, order_button)))
        assert driver.current_url == order_page_url
        driver.quit()

    def test_login_from_registration_page(self):
        driver = webdriver.Chrome()
        driver.get(login_page_url)
        driver.find_element(By.LINK_TEXT, login_page_registration_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, registration_login_button)))
        driver.find_element(By.LINK_TEXT, registration_login_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, login_enter)))
        driver.find_element(By.XPATH, login_email_input).send_keys(user_data[0])
        driver.find_element(By.XPATH, login_password_input).send_keys(user_data[1])
        driver.find_element(By.XPATH, login_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, order_button)))
        assert driver.current_url == order_page_url
        driver.quit()

    def test_login_from_forgotten_password_page(self):
        driver = webdriver.Chrome()
        driver.get(login_page_url)
        driver.find_element(By.LINK_TEXT, login_forgot_password).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, login_button_on_forgot_password)))
        driver.find_element(By.LINK_TEXT, login_button_on_forgot_password).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, login_enter)))
        driver.find_element(By.XPATH, login_email_input).send_keys(user_data[0])
        driver.find_element(By.XPATH, login_password_input).send_keys(user_data[1])
        driver.find_element(By.XPATH, login_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, order_button)))
        assert driver.current_url == order_page_url
        driver.quit()







