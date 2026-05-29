from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import RegistrationPage, AuthorizationPage
from data_for_authorization import Data
from error_texts import Texts
from generators import Generators

class TestRegistration:

    def test_registration_valid_values_successful(self, driver_registration_page: webdriver.Chrome):
        driver = driver_registration_page

        driver.find_element(*RegistrationPage.INPUT_NAME).send_keys(Data.NAME)
        driver.find_element(*RegistrationPage.INPUT_EMAIL).send_keys(Generators.generate_of_login())
        driver.find_element(*RegistrationPage.INPUT_PASSWORD).send_keys(Generators.generate_of_valid_password())

        driver.find_element(*RegistrationPage.REGISTRATION_BUTTON).click()
        
        element = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AuthorizationPage.AUTHORIZATION_FORM))

        assert element.is_displayed()

    def test_registration_invalid_password_unsuccessful(self, driver_registration_page: webdriver.Chrome):
        driver = driver_registration_page

        driver.find_element(*RegistrationPage.INPUT_NAME).send_keys(Data.NAME)
        driver.find_element(*RegistrationPage.INPUT_EMAIL).send_keys(Generators.generate_of_login())
        driver.find_element(*RegistrationPage.INPUT_PASSWORD).send_keys(Generators.generate_of_invalid_password())

        driver.find_element(*RegistrationPage.REGISTRATION_BUTTON).click()
        

        assert driver.find_element(*RegistrationPage.ERROR_TEXT_PASSWORS).text == Texts.ERROR_TEXT_FOR_INVALID_PASSWORD

    def test_registration_empty_name_unsuccessful(self, driver_registration_page: webdriver.Chrome):
        driver = driver_registration_page

        driver.find_element(*RegistrationPage.INPUT_EMAIL).send_keys(Generators.generate_of_login())
        driver.find_element(*RegistrationPage.INPUT_PASSWORD).send_keys(Generators.generate_of_valid_password())

        driver.find_element(*RegistrationPage.REGISTRATION_BUTTON).click()
        
        reg_header = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(RegistrationPage.REGISTRATION_HEADER))
        assert reg_header.is_displayed()