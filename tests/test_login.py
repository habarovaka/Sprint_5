import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators

def test_login_from_main_page(driver, registered_user):
   driver.get("https://stellarburgers.education-services.ru/")
   driver.find_element(*TestLocators.LOGIN_MAIN_BUTTON).click()
   driver.find_element(*TestLocators.EMAIL_INPUT_LOGIN).send_keys(registered_user["email"])
   driver.find_element(*TestLocators.PASSWORD_INPUT_LOGIN).send_keys(registered_user["password"])
   driver.find_element(*TestLocators.LOGIN_BUTTON).click()
   WebDriverWait(driver, 5).until(EC.presence_of_element_located(TestLocators.ORDER_BUTTON))
   assert driver.find_element(*TestLocators.ORDER_BUTTON).is_displayed()

def test_login_personal_cabinet_button_success(driver, registered_user):
   driver.get("https://stellarburgers.education-services.ru/")
   driver.find_element(*TestLocators.PERSONAL_CABINET_BUTTON).click()
   driver.find_element(*TestLocators.EMAIL_INPUT_LOGIN).send_keys(registered_user["email"])
   driver.find_element(*TestLocators.PASSWORD_INPUT_LOGIN).send_keys(registered_user["password"])
   driver.find_element(*TestLocators.LOGIN_BUTTON).click()
   WebDriverWait(driver, 5).until(EC.presence_of_element_located(TestLocators.ORDER_BUTTON))
   assert driver.find_element(*TestLocators.ORDER_BUTTON).is_displayed()

def test_login_from_registration_form_success(driver, registered_user):
   driver.get("https://stellarburgers.education-services.ru/register")
   driver.find_element(*TestLocators.LOGIN_BUTTON_FROM_REGISTER).click()
   driver.find_element(*TestLocators.EMAIL_INPUT_LOGIN).send_keys(registered_user["email"])
   driver.find_element(*TestLocators.PASSWORD_INPUT_LOGIN).send_keys(registered_user["password"])
   driver.find_element(*TestLocators.LOGIN_BUTTON).click()
   WebDriverWait(driver, 5).until(EC.presence_of_element_located(TestLocators.ORDER_BUTTON))
   assert driver.find_element(*TestLocators.ORDER_BUTTON).is_displayed()

def test_login_from_forgot_password_form_success(driver, registered_user):
   driver.get("https://stellarburgers.education-services.ru/forgot-password")
   driver.find_element(*TestLocators.LOGIN_BUTTON_FROM_FOGOT_PASS).click()
   driver.find_element(*TestLocators.EMAIL_INPUT_LOGIN).send_keys(registered_user["email"])
   driver.find_element(*TestLocators.PASSWORD_INPUT_LOGIN).send_keys(registered_user["password"])
   driver.find_element(*TestLocators.LOGIN_BUTTON).click()
   WebDriverWait(driver, 5).until(EC.presence_of_element_located(TestLocators.ORDER_BUTTON))
   assert driver.find_element(*TestLocators.ORDER_BUTTON).is_displayed()