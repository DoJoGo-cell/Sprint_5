import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import AuthorizationPage, RegistrationPage, RecoveryPasswordPage
from urls import URLs

@pytest.fixture
def driver_main_page():
    driver = webdriver.Chrome()
    driver.get(URLs.BASE_URL)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AuthorizationPage.AUTHORIZATION_BUTTON_MAIN))
    yield driver
    driver.quit()

@pytest.fixture
def driver_registration_page():
    driver = webdriver.Chrome()
    driver.get(URLs.REGISTRATION_URL)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(RegistrationPage.REGISTRATION_FORM))
    yield driver
    driver.quit()

@pytest.fixture
def driver_forgot_password_page():
    driver = webdriver.Chrome()
    driver.get(URLs.FORGOT_PASSWORD_URL)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(RecoveryPasswordPage.RECOVERY_FORM))
    yield driver
    driver.quit()


