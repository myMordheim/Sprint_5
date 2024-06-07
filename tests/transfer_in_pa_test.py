from selenium.webdriver.common.by import By
from selenium import webdriver
from locators.login_page import *
from locators.personal_account_page import *
from URLs import *
from data import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestTransferIntoPersonalAccount():

    def test_transfer_into_PA(self, driver):
        driver.get(login_page_url)
        driver.find_element(By.XPATH, login_email_input).send_keys(user_data[0])
        driver.find_element(By.XPATH, login_password_input).send_keys(user_data[1])
        driver.find_element(By.XPATH, login_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, login_personal_account_button)))
        driver.find_element(By.XPATH, login_personal_account_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, pa_profile)))
        assert driver.current_url == personal_account_url

