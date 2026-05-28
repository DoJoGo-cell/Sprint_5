from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import AuthorizationPage, RegistrationPage, MainPage, RecoveryPasswordPage
from data_for_authorization import Data

class TestAuthorization:

    def test_authorization_button_on_main_page(self, driver_main_page: webdriver.Chrome):
        driver = driver_main_page

        driver.find_element(*AuthorizationPage.AUTHORIZATION_BUTTON_MAIN).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AuthorizationPage.AUTHORIZATION_FORM))

        driver.find_element(*AuthorizationPage.INPUT_EMAIL).send_keys(Data.EMAIL)
        driver.find_element(*AuthorizationPage.INPUT_PASSWORD).send_keys(Data.PASSWORD)

        driver.find_element(*AuthorizationPage.AUTHORIZATION_BUTTON).click()

        element = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainPage.BUTTON_ORDER))
        assert element.is_displayed()

    def test_authorization_button_personal_account(self, driver_main_page: webdriver.Chrome):
        driver = driver_main_page

        driver.find_element(*MainPage.BUTTON_ACCOUNT).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AuthorizationPage.AUTHORIZATION_FORM))

        driver.find_element(*AuthorizationPage.INPUT_EMAIL).send_keys(Data.EMAIL)
        driver.find_element(*AuthorizationPage.INPUT_PASSWORD).send_keys(Data.PASSWORD)

        driver.find_element(*AuthorizationPage.AUTHORIZATION_BUTTON).click()

        element = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainPage.BUTTON_ORDER))
        assert element.is_displayed()

    def test_authorization_button_on_registration_page(self, driver_registration_page: webdriver.Chrome):
        driver = driver_registration_page

        driver.find_element(*RegistrationPage.AUTHORIZATION_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AuthorizationPage.AUTHORIZATION_FORM))

        driver.find_element(*AuthorizationPage.INPUT_EMAIL).send_keys(Data.EMAIL)
        driver.find_element(*AuthorizationPage.INPUT_PASSWORD).send_keys(Data.PASSWORD)

        driver.find_element(*AuthorizationPage.AUTHORIZATION_BUTTON).click()

        element = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainPage.BUTTON_ORDER))
        assert element.is_displayed()

    def test_authorization_button_password_recovery(self, driver_forgot_password_page: webdriver.Chrome):
        driver = driver_forgot_password_page

        driver.find_element(*RecoveryPasswordPage.BUTTON_TRANSITION).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AuthorizationPage.AUTHORIZATION_FORM))

        driver.find_element(*AuthorizationPage.INPUT_EMAIL).send_keys(Data.EMAIL)
        driver.find_element(*AuthorizationPage.INPUT_PASSWORD).send_keys(Data.PASSWORD)

        driver.find_element(*AuthorizationPage.AUTHORIZATION_BUTTON).click()

        element = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainPage.BUTTON_ORDER))
        assert element.is_displayed()















