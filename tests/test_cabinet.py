import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators

def test_logout_from_personal_account_success(driver, registered_user):
    driver.get("https://stellarburgers.education-services.ru/")
    driver.find_element(*TestLocators.LOGIN_MAIN_BUTTON).click()
    driver.find_element(*TestLocators.EMAIL_INPUT_LOGIN).send_keys(registered_user["email"])
    driver.find_element(*TestLocators.PASSWORD_INPUT_LOGIN).send_keys(registered_user["password"])
    driver.find_element(*TestLocators.LOGIN_BUTTON).click()
    driver.find_element(*TestLocators.PERSONAL_CABINET_BUTTON).click()
    driver.find_element(*TestLocators.LOGOUT_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.url_contains("https://stellarburgers.education-services.ru"))

def test_navigation_from_account_to_constructor_via_link_success(driver, registered_user):
    driver.get("https://stellarburgers.education-services.ru/")
    driver.find_element(*TestLocators.PERSONAL_CABINET_BUTTON).click()
    driver.find_element(*TestLocators.EMAIL_INPUT_LOGIN).send_keys(registered_user["email"])
    driver.find_element(*TestLocators.PASSWORD_INPUT_LOGIN).send_keys(registered_user["password"])
    driver.find_element(*TestLocators.LOGIN_BUTTON).click()
    driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TestLocators.CONSTRUCTOR_BUTTON))

def test_navigation_to_constructor_logo_success(driver, registered_user):
    driver.get("https://stellarburgers.education-services.ru/")
    driver.find_element(*TestLocators.PERSONAL_CABINET_BUTTON).click()
    driver.find_element(*TestLocators.EMAIL_INPUT_LOGIN).send_keys(registered_user["email"])
    driver.find_element(*TestLocators.PASSWORD_INPUT_LOGIN).send_keys(registered_user["password"])
    driver.find_element(*TestLocators.LOGO_BUTTON).click()
    assert driver.current_url == "https://stellarburgers.education-services.ru/"
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.CONSTRUCTOR_TITLE))
    assert driver.find_element(*TestLocators.CONSTRUCTOR_TITLE).is_displayed()