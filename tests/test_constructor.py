import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators

def test_constructor_go_to_buns_section_success(driver):
    driver.get("https://stellarburgers.education-services.ru/")
    driver.find_element(*TestLocators.SAUCES_TAB).click()
    driver.find_element(*TestLocators.BUNS_TAB).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(TestLocators.BUNS_TAB_ACTIVE))
    assert driver.find_element(*TestLocators.BUNS_TAB_ACTIVE).is_displayed()

def test_constructor_go_to_sauces_section_success( driver):
    driver.get("https://stellarburgers.education-services.ru/")
    driver.find_element(*TestLocators.SAUCES_TAB).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(TestLocators.SAUCES_TAB_ACTIVE))
    assert driver.find_element(*TestLocators.SAUCES_TAB_ACTIVE).is_displayed()

def test_constructor_go_to_fillings_section_success(driver):
    driver.get("https://stellarburgers.education-services.ru/")
    driver.find_element(*TestLocators.FILLINGS_TAB).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.FILLINGS_TAB_ACTIVE))
    assert driver.find_element(*TestLocators.FILLINGS_TAB_ACTIVE).is_displayed()