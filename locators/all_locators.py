from selenium.webdriver.common.by import By


class HomePageLocators:
    login_account_button = (By. XPATH, ".//button[text() = 'Войти в аккаунт']")
    account_link = (By. XPATH, ".//a[href = 'account']")
    constructor_link = (By.XPATH, "//a[@href='/']")
    logo = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")
    buns = (By.XPATH, "//span[text()='Булки']/parent::div")
    sauces = (By.XPATH, "//span[text()='Соусы']/parent::div")
    filling = (By.XPATH, "//span[text()='Начинки']/parent::div")
    active_section = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")

class LoginPageLocators:
    login_label = (By. XPATH, ".//h2[text() = 'Вход']")
    login_input = (By. XPATH, ".//label[text() = 'Email']/following_sibling::input")
    password_input = (By. XPATH, ".//label[text() = 'Пароль']/following_sibling::input")
    login_button = (By. XPATH, ".//button[text() = 'Войти']")
    registration_link = (By. XPATH, ".//a[href = 'register']")
    restore_password_link = (By. XPATH, ".//a[href = 'forgot-password']")

class RegistrationPageLocators:
    name_input = (By. XPATH, ".//label[text() = 'Имя']/following_sibling::input")
    email_input = (By. XPATH, ".//label[text() = 'Email']/following_sibling::input")
    password_input = (By. XPATH, ".//label[text() = 'Пароль']/following_sibling::input")
    register_button = (By. XPATH, ".//a[href = 'account']")
    password_error = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")

class AccountPageLocators:
    profile_link = (By.XPATH, "//a[text()='Профиль']")
    name_input = (By. XPATH, ".//label[text() = 'Имя']/following_sibling::input")
    login_input = (By. XPATH, ".//label[text() = 'Логин']/following_sibling::input")
    password_input = (By. XPATH, ".//label[text() = 'Пароль']/following_sibling::input")
    logout_button = (By. XPATH, ".//button[text() = 'Выход']")

