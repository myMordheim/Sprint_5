from selenium.webdriver.common.by import By
from selenium import webdriver
from locators.registration_page import *
from locators.login_page import *
from conftest import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Test_registration_page():

    def test_correct_registration(self, login, password):
        driver = webdriver.Chrome()
        driver.get(registration_page_url)
        driver.find_element(By.XPATH, registration_name_input).send_keys("Sauron")
        driver.find_element(By.XPATH, registration_email_input).send_keys(login)
        driver.find_element(By.XPATH, registration_password_input).send_keys(password)
        driver.find_element(By.XPATH,registration_registr_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, login_enter)))
        assert driver.current_url == login_page_url
        driver.quit()

    def test_incorrect_password(self, login, password_negative):
        driver = webdriver.Chrome()
        driver.get(registration_page_url)
        driver.find_element(By.XPATH, registration_name_input).send_keys("Sauron")
        driver.find_element(By.XPATH, registration_email_input).send_keys(login)
        driver.find_element(By.XPATH, registration_password_input).send_keys(password_negative)
        driver.find_element(By.XPATH, registration_registr_button).click()
        assert driver.find_element(By.XPATH, registration_wrong_password).text == 'Некорректный пароль'
        driver.quit()
