import pytest
import random
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from locators import Urls

# Фикстура для генерации email
@pytest.fixture
def user_email():
    digits = random.randint(10000, 99999)
    return f"ksenya_habarova_46_{digits}@yandex.ru"

# Фикстура для генерации пароля
@pytest.fixture
def user_password():
    return f"Pass{random.randint(100, 999)}!"

# Универсальная фикстура для драйвера
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Фикстура регистрирует пользователя и возвращает его данные
@pytest.fixture
def registered_user(driver, user_email, user_password):
    driver.get(Urls.REGISTRATOR_URL)
    driver.find_element(*TestLocators. NAME_INPUT).send_keys("Ksenya")
    driver.find_element(*TestLocators. EMAIL_INPUT).send_keys(user_email)
    driver.find_element(*TestLocators. PASSWORD_INPUT).send_keys(user_password)
    driver.find_element(*TestLocators.REGISTER_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.url_contains(Urls.LOGIN_URL))
    user_data = {"email": user_email, "password": user_password}
    yield user_data
    login_payload = {"email": user_email, "password": user_password}
    response = requests.post(f"{Urls.BASE_URL}/api/auth/login", data=login_payload)
    if response.status_code == 200:
        token = response.json().get("accessToken")
        requests.delete(f"{Urls.BASE_URL}/api/auth/user", headers={'Authorization': token})