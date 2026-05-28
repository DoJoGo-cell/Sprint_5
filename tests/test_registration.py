from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import RegistrationPage, AuthorizationPage
from data_for_authorization import Data
from error_texts import Texts

class TestRegistration:

    def test_registration_valid_values_successful(self, generator_of_login, generator_of_valid_password, driver_registration_page: webdriver.Chrome):
        driver = driver_registration_page

        driver.find_element(*RegistrationPage.INPUT_NAME).send_keys(Data.NAME)
        driver.find_element(*RegistrationPage.INPUT_EMAIL).send_keys(generator_of_login)
        driver.find_element(*RegistrationPage.INPUT_PASSWORD).send_keys(generator_of_valid_password)

        driver.find_element(*RegistrationPage.REGISTRATION_BUTTON).click()
        
        element = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AuthorizationPage.AUTHORIZATION_FORM))

        assert element.is_displayed()

    def test_registration_invalid_password_unsuccessful(self, generator_of_login, generator_of_invalid_password, driver_registration_page: webdriver.Chrome):
        driver = driver_registration_page

        driver.find_element(*RegistrationPage.INPUT_NAME).send_keys(Data.NAME)
        driver.find_element(*RegistrationPage.INPUT_EMAIL).send_keys(generator_of_login)
        driver.find_element(*RegistrationPage.INPUT_PASSWORD).send_keys(generator_of_invalid_password)

        driver.find_element(*RegistrationPage.REGISTRATION_BUTTON).click()
        
        assert driver.find_element(*RegistrationPage.ERROR_TEXT).text == Texts.ERROR_TEXT_FOR_INVALID_PASSWORD