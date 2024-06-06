from selenium.webdriver.common.by import By
from selenium import webdriver
from locators.registration_page import *
from URLs import *
from locators.login_page import *
from helpers import *
from conftest import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Test_Registration_Page():

    def test_correct_registration(self, driver):
        driver.get(registration_page_url)
        driver.find_element(By.XPATH, registration_name_input).send_keys("Sauron")
        driver.find_element(By.XPATH, registration_email_input).send_keys(Registration.login())
        driver.find_element(By.XPATH, registration_password_input).send_keys(Registration.password())
        driver.find_element(By.XPATH,registration_registr_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, login_enter)))
        assert driver.current_url == login_page_url

    def test_incorrect_password(self, driver):
        driver.get(registration_page_url)
        driver.find_element(By.XPATH, registration_name_input).send_keys("Sauron")
        driver.find_element(By.XPATH, registration_email_input).send_keys(Registration.login())
        driver.find_element(By.XPATH, registration_password_input).send_keys(Registration.password_negative())
        driver.find_element(By.XPATH, registration_registr_button).click()
        assert driver.find_element(By.XPATH, registration_wrong_password).text == 'Некорректный пароль'
