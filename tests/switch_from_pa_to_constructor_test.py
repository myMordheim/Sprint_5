from selenium.webdriver.common.by import By
from selenium import webdriver
from locators.login_page import *
from locators.personal_account_page import *
from locators.order_page import *
from URLs import *
from data import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class Test_Transfer_From_Personal_Account():

    def test_transfer_from_PA_to_constructor(self, driver):
        driver.get(login_page_url)
        driver.find_element(By.XPATH, login_email_input).send_keys(user_data[0])
        driver.find_element(By.XPATH, login_password_input).send_keys(user_data[1])
        driver.find_element(By.XPATH, login_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, login_personal_account_button)))
        driver.find_element(By.XPATH, login_personal_account_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, pa_profile)))
        driver.find_element(By.XPATH, pa_to_order_page).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, order_button)))
        assert driver.current_url == order_page_url

    def test_transfer_from_PA_to_constructor_by_click_on_logo(self, driver):
        driver.get(login_page_url)
        driver.find_element(By.XPATH, login_email_input).send_keys(user_data[0])
        driver.find_element(By.XPATH, login_password_input).send_keys(user_data[1])
        driver.find_element(By.XPATH, login_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, login_personal_account_button)))
        driver.find_element(By.XPATH, login_personal_account_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, stellar_burger_logo)))
        driver.find_element(By.XPATH, stellar_burger_logo).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, order_button)))
        assert driver.current_url == order_page_url



