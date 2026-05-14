import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from locators import Urls

class TestStellarBurgersLogin:

    def test_login_from_main_page(self, driver, registered_user):
        driver.get(Urls.BASE_URL)
        driver.find_element(*TestLocators.LOGIN_MAIN_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_INPUT_LOGIN).send_keys(registered_user["email"])
        driver.find_element(*TestLocators.PASSWORD_INPUT_LOGIN).send_keys(registered_user["password"])
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        order_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.ORDER_BUTTON))
        assert order_button.is_displayed(), "Кнопка 'Оформить заказ' не отобразилась после входа с главной страницы"

    def test_login_personal_cabinet_button_success(self, driver, registered_user):
        driver.get(Urls.BASE_URL)
        driver.find_element(*TestLocators.PERSONAL_CABINET_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_INPUT_LOGIN).send_keys(registered_user["email"])
        driver.find_element(*TestLocators.PASSWORD_INPUT_LOGIN).send_keys(registered_user["password"])
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        order_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.ORDER_BUTTON))
        assert order_button.is_displayed(), "Не удалось войти через кнопку 'Личный кабинет'"

    def test_login_from_registration_form_success(self, driver, registered_user):
        driver.get(Urls.REGISTRATOR_URL)
        driver.find_element(*TestLocators.LOGIN_BUTTON_FROM_REGISTER).click()
        driver.find_element(*TestLocators.EMAIL_INPUT_LOGIN).send_keys(registered_user["email"])
        driver.find_element(*TestLocators.PASSWORD_INPUT_LOGIN).send_keys(registered_user["password"])
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        order_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.ORDER_BUTTON))
        assert order_button.is_displayed(), "Не удалось войти через ссылку со страницы регистрации"

    def test_login_from_forgot_password_form_success(self, driver, registered_user):
        driver.get(Urls.PASSWORD_URL)
        driver.find_element(*TestLocators.LOGIN_BUTTON_FROM_FOGOT_PASS).click()
        driver.find_element(*TestLocators.EMAIL_INPUT_LOGIN).send_keys(registered_user["email"])
        driver.find_element(*TestLocators.PASSWORD_INPUT_LOGIN).send_keys(registered_user["password"])
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        order_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.ORDER_BUTTON))
        assert order_button.is_displayed(), "Не удалось войти через ссылку со страницы восстановления пароля"