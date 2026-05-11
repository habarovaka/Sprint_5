import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators

def test_register_with_valid_data_shows_success_message(driver, user_email, user_password):
   driver.get("https://stellarburgers.education-services.ru/register")
   driver.find_element(*TestLocators.NAME_INPUT).send_keys('Name')
   driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(user_email)
   driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(user_password)
   driver.find_element(*TestLocators. REGISTER_BUTTON).click()
   WebDriverWait(driver, 5).until(EC.url_contains("https://stellarburgers.education-services.ru/login"))

def test_registration_short_password_show_error(driver, user_email, user_password):
   driver.get("https://stellarburgers.education-services.ru/register")
   driver.find_element(*TestLocators.NAME_INPUT).send_keys('Name')
   driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(user_email)
   driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys('12345')
   driver.find_element(*TestLocators.REGISTER_BUTTON).click()
   WebDriverWait(driver, 5).until(EC.presence_of_element_located(TestLocators.PASSWORD_ERROR))
