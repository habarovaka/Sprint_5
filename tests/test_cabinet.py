import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators

class TestStellarBurgersNavigation:

    def test_logout_from_personal_account_success(self, driver, registered_user):
        driver.get("https://stellarburgers.education-services.ru/login")
        driver.find_element(*TestLocators.EMAIL_INPUT_LOGIN).send_keys(registered_user["email"])
        driver.find_element(*TestLocators.PASSWORD_INPUT_LOGIN).send_keys(registered_user["password"])
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TestLocators.PERSONAL_CABINET_BUTTON)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TestLocators.LOGOUT_BUTTON)).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.LOGIN_BUTTON))
        assert "/login" in driver.current_url
        assert driver.find_element(*TestLocators.LOGIN_BUTTON).is_displayed()

    def test_navigation_from_account_to_constructor_via_link_success(self, driver, registered_user):
        driver.get("https://stellarburgers.education-services.ru/login")
        driver.find_element(*TestLocators.EMAIL_INPUT_LOGIN).send_keys(registered_user["email"])
        driver.find_element(*TestLocators.PASSWORD_INPUT_LOGIN).send_keys(registered_user["password"])
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.PERSONAL_CABINET_BUTTON).click()
        driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        header = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.CONSTRUCTOR_TITLE))
        assert header.text == "Соберите бургер"
        assert header.is_displayed()

    def test_navigation_to_constructor_logo_success(self, driver, registered_user):
        driver.get("https://stellarburgers.education-services.ru/login")
        driver.find_element(*TestLocators.EMAIL_INPUT_LOGIN).send_keys(registered_user["email"])
        driver.find_element(*TestLocators.PASSWORD_INPUT_LOGIN).send_keys(registered_user["password"])
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.PERSONAL_CABINET_BUTTON).click()
        driver.find_element(*TestLocators.LOGO_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.CONSTRUCTOR_TITLE))
        assert driver.current_url == "https://stellarburgers.education-services.ru/"
        assert driver.find_element(*TestLocators.CONSTRUCTOR_TITLE).is_displayed()