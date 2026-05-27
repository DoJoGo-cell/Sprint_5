from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from locators import AuthorizationPage, Construction

class TestTransition:

    def test_construction_transition_to_buns_section(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.education-services.ru")

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AuthorizationPage.AUTHORIZATION_BUTTON_MAIN))

        driver.find_element(*Construction.SAUCES_SECTION_INACTIVE).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Construction.SAUCES_SECTION_ACTIVE))

        driver.find_element(*Construction.BUNS_SECTION_INACTIVE).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Construction.BUNS_SECTION_ACTIVE))

        element = driver.find_element(*Construction.BUNS_SECTION_ACTIVE).find_element(By.XPATH, '..')
        assert "tab_tab_type_current__2BEPc" in element.get_attribute("class")

        driver.quit()

    def test_construction_transition_to_sauces_section(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.education-services.ru")

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AuthorizationPage.AUTHORIZATION_BUTTON_MAIN))

        driver.find_element(*Construction.SAUCES_SECTION_INACTIVE).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Construction.SAUCES_SECTION_ACTIVE))

        element = driver.find_element(*Construction.SAUCES_SECTION_ACTIVE).find_element(By.XPATH, '..')
        assert "tab_tab_type_current__2BEPc" in element.get_attribute("class")

        driver.quit()

    def test_construction_transition_to_toppings_section(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.education-services.ru")

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AuthorizationPage.AUTHORIZATION_BUTTON_MAIN))

        driver.find_element(*Construction.TOPPINGS_SECTION_INACTIVE).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Construction.TOPPINGS_SECTION_ACTIVE))

        element = driver.find_element(*Construction.TOPPINGS_SECTION_ACTIVE).find_element(By.XPATH, '..')
        assert "tab_tab_type_current__2BEPc" in element.get_attribute("class")

        driver.quit()