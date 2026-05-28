from selenium import webdriver
from locators import Construction

class TestTransition:

    def test_construction_transition_to_buns_section(self, driver_main_page: webdriver.Chrome):
        driver = driver_main_page

        assert driver.find_element(*Construction.BUNS_SECTION_SELECTED)

    def test_construction_transition_to_sauces_section(self, driver_main_page: webdriver.Chrome):
        driver = driver_main_page

        driver.find_element(*Construction.SAUCES_SECTION).click()

        assert driver.find_element(*Construction.SAUCES_SECTION_SELECTED)

    def test_construction_transition_to_toppings_section(self, driver_main_page: webdriver.Chrome):
        driver = driver_main_page

        driver.find_element(*Construction.TOPPINGS_SECTION).click()

        assert driver.find_element(*Construction.TOPPINGS_SECTION_SELECTED)
