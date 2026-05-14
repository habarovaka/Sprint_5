from selenium.webdriver.common.by import By

class TestLocators:
    # --- ГЛАВНАЯ СТРАНИЦА ---
    # Кнопка «Войти в аккаунт» на главной
    LOGIN_MAIN_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    # Кнопка «Конструктор» в хедере
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
    # Кнопка «Оформить заказ» (видна только после входа)
    ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
    # Локатор логотипа (ссылка-картинка в хедере)
    LOGO_BUTTON = (By.XPATH, ".//div[contains(@class, 'header__logo')]/a")
    # Заголовок "Соберите бургер" для проверки, что мы на главной
    CONSTRUCTOR_TITLE = (By.XPATH, ".//h1[text()='Соберите бургер']")

    # --- РЕГИСТРАЦИЯ ---
    # Поля ввода в регистрации (ищем по тексту рядом)
    NAME_INPUT = (By.XPATH, ".//label[text()='Имя']/parent::div//input")
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/parent::div//input")
    PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/parent::div//input")
    # Кнопка «Зарегистрироваться»
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    # Текст ошибки «Некорректный пароль»
    PASSWORD_ERROR = (By.XPATH, ".//p[contains(@class, 'input__error') and text()='Некорректный пароль']")

    # --- ВХОД ---
    # Поля ввода на странице логина (те же названия, что и в регистрации)
    EMAIL_INPUT_LOGIN = (By.XPATH, ".//label[text()='Email']/parent::div//input")
    PASSWORD_INPUT_LOGIN = (By.XPATH, ".//label[text()='Пароль']/parent::div//input")
    # Кнопка «Войти» на форме логина
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")

    # Ссылки «Войти» на других страницах (привязываемся к контексту "соседа")
    LOGIN_BUTTON_FROM_REGISTER = (By.XPATH, ".//p[contains(text(),'Уже зарегистрированы')]/a[text()='Войти']")
    LOGIN_BUTTON_FROM_FOGOT_PASS = (By.XPATH, ".//p[contains(text(),'Вспомнили пароль')]/a[text()='Войти']")

    # --- ЛИЧНЫЙ КАБИНЕТ ---
    # Кнопка «Личный кабинет» в хедере
    PERSONAL_CABINET_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")
    # Кнопка «Выйти» в самом кабинете
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")

    # --- КОНСТРУКТОР ---
    # Сами вкладки (для клика)
    BUNS_TAB = (By.XPATH, ".//span[text()='Булки']/parent::div")
    SAUCES_TAB = (By.XPATH, ".//span[text()='Соусы']/parent::div")
    FILLINGS_TAB = (By.XPATH, ".//span[text()='Начинки']/parent::div")

    # Активные вкладки (проверка, что класс сменился на 'current')
    BUNS_TAB_ACTIVE = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current')]/span[text()='Булки']")
    SAUCES_TAB_ACTIVE = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current')]/span[text()='Соусы']")
    FILLINGS_TAB_ACTIVE = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current')]/span[text()='Начинки']")

class Urls:
    BASE_URL = "https://stellarburgers.education-services.ru/"
    LOGIN_URL = f"{BASE_URL}login"
    PROFILE_URL = f"{BASE_URL}account/profile"
    REGISTRATOR_URL = f"{BASE_URL}register"
    PASSWORD_URL = f"{BASE_URL}forgot-password"