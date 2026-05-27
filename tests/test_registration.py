from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import RegistrationPage

class TestRegistration:

    def test_registration_valid_values_successful(self, generator_of_login, generator_of_valid_password):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.education-services.ru/register")

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(RegistrationPage.REGISTRATION_FORM))

        driver.find_element(*RegistrationPage.INPUT_NAME).send_keys("Andrew")
        driver.find_element(*RegistrationPage.INPUT_EMAIL).send_keys(generator_of_login)
        driver.find_element(*RegistrationPage.INPUT_PASSWORD).send_keys(generator_of_valid_password)

        driver.find_element(*RegistrationPage.REGISTRATION_BUTTON).click()
        
        WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element(RegistrationPage.REGISTRATION_HEADER, 'Вход'))
        
        assert driver.current_url == 'https://stellarburgers.education-services.ru/login'
        
        driver.quit()

    def test_registration_invalid_password_unsuccessful(self, generator_of_login, generator_of_invalid_password):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.education-services.ru/register")

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(RegistrationPage.REGISTRATION_FORM))

        driver.find_element(*RegistrationPage.INPUT_NAME).send_keys("Andrew")
        driver.find_element(*RegistrationPage.INPUT_EMAIL).send_keys(generator_of_login)
        driver.find_element(*RegistrationPage.INPUT_PASSWORD).send_keys(generator_of_invalid_password)

        driver.find_element(*RegistrationPage.REGISTRATION_BUTTON).click()
        
        assert driver.find_element(*RegistrationPage.ERROR_TEXT).text == 'Некорректный пароль'
        
        driver.quit()