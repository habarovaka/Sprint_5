import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from locators import Urls

class TestStellarBurgersRegistration:

    def test_register_with_valid_data_success(self, driver, user_email, user_password):
        driver.get(Urls.REGISTRATOR_URL)
        driver.find_element(*TestLocators.NAME_INPUT).send_keys('Name')
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(user_email)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(user_password)
        driver.find_element(*TestLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.url_contains("/login"))
        assert "/login" in driver.current_url
        assert driver.find_element(*TestLocators.LOGIN_BUTTON).is_displayed()

    def test_registration_short_password_show_error(self, driver, user_email):
        driver.get(Urls.REGISTRATOR_URL)
        driver.find_element(*TestLocators.NAME_INPUT).send_keys('Name')
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(user_email)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys('12345')
        driver.find_element(*TestLocators.REGISTER_BUTTON).click()
        error_message = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.PASSWORD_ERROR))
        assert error_message.is_displayed()
        assert error_message.text == "Некорректный пароль"