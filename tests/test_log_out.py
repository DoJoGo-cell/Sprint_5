from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import AuthorizationPage, MainPage, PersonalAccountPage
from data_for_authorization import Data

class TestTransition:

    def test_log_out_account(self, driver_main_page: webdriver.Chrome):
        driver = driver_main_page
        
        driver.find_element(*AuthorizationPage.AUTHORIZATION_BUTTON_MAIN).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AuthorizationPage.AUTHORIZATION_FORM))

        driver.find_element(*AuthorizationPage.INPUT_EMAIL).send_keys(Data.EMAIL)
        driver.find_element(*AuthorizationPage.INPUT_PASSWORD).send_keys(Data.PASSWORD)

        driver.find_element(*AuthorizationPage.AUTHORIZATION_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainPage.BUTTON_ORDER))

        driver.find_element(*MainPage.BUTTON_ACCOUNT).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(PersonalAccountPage.PROFILE_SECTION_ACTIVE))

        driver.find_element(*PersonalAccountPage.BUTTON_LOG_OUT).click()

        element = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AuthorizationPage.AUTHORIZATION_FORM))

        assert element.is_displayed()