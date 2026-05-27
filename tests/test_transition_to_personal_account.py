from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import AuthorizationPage, MainPage, PersonalAccountPage

class TestTransition:

    def test_transition_to_personal_account_from_main_page(self, registration_data_for_authorization):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.education-services.ru")
        
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AuthorizationPage.AUTHORIZATION_BUTTON_MAIN))

        driver.find_element(*AuthorizationPage.AUTHORIZATION_BUTTON_MAIN).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AuthorizationPage.AUTHORIZATION_FORM))

        driver.find_element(*AuthorizationPage.INPUT_EMAIL).send_keys(registration_data_for_authorization['Email'])
        driver.find_element(*AuthorizationPage.INPUT_PASSWORD).send_keys(registration_data_for_authorization['Пароль'])

        driver.find_element(*AuthorizationPage.AUTHORIZATION_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainPage.BUTTON_ORDER))

        driver.find_element(*MainPage.BUTTON_ACCOUNT).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(PersonalAccountPage.PROFILE_SECTION_ACTIVE))

        assert driver.current_url == "https://stellarburgers.education-services.ru/account/profile"

        driver.quit()
