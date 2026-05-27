from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import AuthorizationPage, RegistrationPage, MainPage, RecoveryPasswordPage

class TestAuthorization:

    def test_authorization_button_on_main_page(self, registration_data_for_authorization):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.education-services.ru")

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AuthorizationPage.AUTHORIZATION_BUTTON_MAIN))

        driver.find_element(*AuthorizationPage.AUTHORIZATION_BUTTON_MAIN).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AuthorizationPage.AUTHORIZATION_FORM))

        driver.find_element(*AuthorizationPage.INPUT_EMAIL).send_keys(registration_data_for_authorization['Email'])
        driver.find_element(*AuthorizationPage.INPUT_PASSWORD).send_keys(registration_data_for_authorization['Пароль'])

        driver.find_element(*AuthorizationPage.AUTHORIZATION_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainPage.BUTTON_ORDER))

        assert driver.current_url == 'https://stellarburgers.education-services.ru/'

        driver.quit()

    def test_authorization_button_personal_account(self, registration_data_for_authorization):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.education-services.ru")

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AuthorizationPage.AUTHORIZATION_BUTTON_MAIN))

        driver.find_element(*MainPage.BUTTON_ACCOUNT).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AuthorizationPage.AUTHORIZATION_FORM))

        driver.find_element(*AuthorizationPage.INPUT_EMAIL).send_keys(registration_data_for_authorization['Email'])
        driver.find_element(*AuthorizationPage.INPUT_PASSWORD).send_keys(registration_data_for_authorization['Пароль'])

        driver.find_element(*AuthorizationPage.AUTHORIZATION_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainPage.BUTTON_ORDER))

        assert driver.current_url == 'https://stellarburgers.education-services.ru/'

        driver.quit()

    def test_authorization_button_on_registration_page(self, registration_data_for_authorization):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.education-services.ru/register")

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(RegistrationPage.REGISTRATION_FORM))

        driver.find_element(*RegistrationPage.AUTHORIZATION_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AuthorizationPage.AUTHORIZATION_FORM))

        driver.find_element(*AuthorizationPage.INPUT_EMAIL).send_keys(registration_data_for_authorization['Email'])
        driver.find_element(*AuthorizationPage.INPUT_PASSWORD).send_keys(registration_data_for_authorization['Пароль'])

        driver.find_element(*AuthorizationPage.AUTHORIZATION_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainPage.BUTTON_ORDER))

        assert driver.current_url == 'https://stellarburgers.education-services.ru/'

        driver.quit()

    def test_authorization_button_password_recovery(self, registration_data_for_authorization):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.education-services.ru/forgot-password")

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(RecoveryPasswordPage.RECOVERY_FORM))

        driver.find_element(*RecoveryPasswordPage.BUTTON_TRANSITION).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AuthorizationPage.AUTHORIZATION_FORM))

        driver.find_element(*AuthorizationPage.INPUT_EMAIL).send_keys(registration_data_for_authorization['Email'])
        driver.find_element(*AuthorizationPage.INPUT_PASSWORD).send_keys(registration_data_for_authorization['Пароль'])

        driver.find_element(*AuthorizationPage.AUTHORIZATION_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainPage.BUTTON_ORDER))

        assert driver.current_url == 'https://stellarburgers.education-services.ru/'

        driver.quit()
















