import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from locators import Urls

class TestStellarBurgersConstructor:

    def test_constructor_go_to_buns_section_success(self, driver):
        driver.get(Urls.BASE_URL)
        driver.find_element(*TestLocators.SAUCES_TAB).click()
        driver.find_element(*TestLocators.BUNS_TAB).click()
        active_buns = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.BUNS_TAB_ACTIVE))
        assert active_buns.is_displayed(), "Вкладка 'Булки' должна быть активна"

    def test_constructor_go_to_sauces_section_success(self, driver):
        driver.get(Urls.BASE_URL)
        driver.find_element(*TestLocators.SAUCES_TAB).click()
        active_sauces = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.SAUCES_TAB_ACTIVE))
        assert active_sauces.is_displayed(), "Вкладка 'Соусы' должна быть активна"

    def test_constructor_go_to_fillings_section_success(self, driver):
        driver.get(Urls.BASE_URL)
        driver.find_element(*TestLocators.FILLINGS_TAB).click()
        active_fillings = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.FILLINGS_TAB_ACTIVE))
        assert active_fillings.is_displayed(), "Вкладка 'Начинки' должна быть активна"