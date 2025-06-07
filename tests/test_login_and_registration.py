from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test_data.test_data import UserData
from helpers.data_helpers import DataHelper
from locators.all_locators import (
    HomePageLocators,
    LoginPageLocators,
    RegistrationPageLocators,
    AccountPageLocators
)

home_locators = HomePageLocators()
login_locators = LoginPageLocators()
registration_locators = RegistrationPageLocators()
account_locators = AccountPageLocators()

# Проверка регистрации: успешная регистрация
class TestLoginAndRegistration:
    def test_register_new_user(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, 10)

        driver.get("https://stellarburgers.nomoreparties.site/")
        login_account_button = wait.until(EC.element_to_be_clickable(home_locators.login_account_buuton))
        login_account_button.click()

        registration_link = wait.until(EC.element_to_be_clickable(login_locators.registration_link))
        registration_link.click()

        name_data = DataHelper.generate_name()
        email_data = DataHelper.generate_login()
        password_data = DataHelper.generate_password()

        register_name_input = wait.until(EC.visibility_of_element_located(registration_locators.name_input))
        register_email_input = wait.until(EC.visibility_of_element_located(registration_locators.email_input))
        register_password_input = wait.until(EC.visibility_of_element_located(registration_locators.password_input))

        register_name_input.send_keys(name_data)
        register_email_input.send_keys(email_data)
        register_password_input.send_keys(password_data)

        register_button = wait.until(EC.element_to_be_clickable(registration_locators.register_button))
        register_button.click()

        login_input = wait.until(EC.visibility_of_element_located(login_locators.login_input))
        password_input = wait.until(EC.visibility_of_element_located(login_locators.password_input))

        login_input.send_keys(email_data)
        password_input.send_keys(password_data)

        login_button = wait.until(EC.element_to_be_clickable(login_locators.login_button))
        login_button.click()

        account_link = wait.until(EC.element_to_be_clickable(login_locators.login_button))
        login_button.click()

        account_link = wait.until(EC.element_to_be_clickable(home_locators.account_link))
        account_link.click()

        account_name_input = wait.until(EC.visibility_of_element_located(account_locators.name_input))
        account_login_input = wait.until(EC.visibility_of_element_located(account_locators.login_input))

        assert account_name_input.get_attribute("value") == name_data
        assert account_login_input.get_attribute("value") == email_data


#Проверка регистрации: ошибка для некорректного пароля
    def test_invalid_password_registration(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, 10)

        driver.get("https://stellarburgers.nomoreparties.site/")
        login_account_button = wait.until(EC.element_to_be_clickable(home_locators.login_account_buuton))
        login_account_button.click()

        registration_link = wait.until(EC.element_to_be_clickable(login_locators.registration_link))
        registration_link.click()

        name_data = DataHelper.generate_name()
        email_data = DataHelper.generate_login()
        invalid_password = "12345"

        driver.find_element(*RegistrationPageLocators.name_input).send_keys(name_data)
        driver.find_element(*RegistrationPageLocators.email_input).send_keys(email_data)
        driver.find_element(*RegistrationPageLocators.password_input).send_keys(invalid_password)
        driver.find_element(*RegistrationPageLocators.register_button).click()

        error = wait.until(EC.visibility_of_element_located(RegistrationPageLocators.password_error))
        assert error.is_displayed()


#Проверка входа: вход по кнопке «Войти в аккаунт» на главной
    def test_login_home_page(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, 10)

        driver.get("https://stellarburgers.nomoreparties.site/")

        login_account_button = wait.until(EC.element_to_be_clickable(home_locators.login_account_buuton))
        login_account_button.click()

        login_input = wait.until(EC.visibility_of_element_located(login_locators.login_input))
        password_input = wait.until(EC.visibility_of_element_located(login_locators.password_input))

        user_data = UserData()
        login_input.send_keys(UserData.email)
        password_input.send_keys(UserData.password)

        login_button = wait.until(EC.element_to_be_clickable(login_locators.login_button))
        login_button.click()

        account_link = wait.until(EC.element_to_be_clickable(home_locators.account_link))
        account_link.click()

        account_name_input = wait.until(EC.visibility_of_element_located(account_locators.name_input))
        account_login_input = wait.until(EC.visibility_of_element_located(account_locators.login_input))

        assert account_name_input.get_attribute("value") == user_data.name
        assert account_login_input.get_attribute("value") == user_data.email


#Проверка входа: вход через кнопку «Личный кабинет»
    def test_login_home_page(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, 10)

        driver.get("https://stellarburgers.nomoreparties.site/")

        login_account_button = wait.until(EC.element_to_be_clickable(home_locators.login_account_buuton))
        login_account_button.click()

        login_input = wait.until(EC.visibility_of_element_located(login_locators.login_input))
        password_input = wait.until(EC.visibility_of_element_located(login_locators.password_input))

        user_data = UserData()
        login_input.send_keys(UserData.email)
        password_input.send_keys(UserData.password)

        login_button = wait.until(EC.element_to_be_clickable(login_locators.login_button))
        login_button.click()

        account_link = wait.until(EC.element_to_be_clickable(home_locators.account_link))
        account_link.click()

        account_name_input = wait.until(EC.visibility_of_element_located(account_locators.name_input))
        account_login_input = wait.until(EC.visibility_of_element_located(account_locators.login_input))

        assert account_name_input.get_attribute("value") == user_data.name
        assert account_login_input.get_attribute("value") == user_data.email

#Проверка входа: вход через кнопку в форме регистрации
    def test_login_from_registration_page(self, create_driver):
        wait = WebDriverWait(driver, 10)
        user = UserData()

        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(*RegistrationPageLocators.login_limk).click()

        wait.until(EC.visibility_of_element_located(LoginPageLocators.email_input)).send_keys(user.email)
        driver.find_element(*LoginPageLocators.password_input).send_keys(user.password)
        driver.find_element(*LoginPageLocators.login_button).click()

        wait.until(EC.visibility_of_element_located(HomePageLocators.account_link))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"


#Проверка входа: вход через кнопку в форме восстановления пароля
    def test_login_from_password_restore_page(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, 10)

        driver.get("https://stellarburgers.nomoreparties.site/")

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(HomePageLocators.login_account_button))
        )
        login_button.click()

        recovery_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.restore_password_link))
        )
        recovery_link.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.password_recovery_link)
        )

        login_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.login_link)
        )
        login_link.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.login_label)
        )

        email_data = DataHelper.generate_login()
        password_data = DataHelper.generate_password()

        email_input = wait.until(EC.visibility_of_element_located(registration_locators.email_input))
        password_input = wait.until(EC.visibility_of_element_located(registration_locators.password_input))

        email_input.send_keys(email_data)
        password_input.send_keys(password_data)

        submit_button = driver.find_element(LoginPageLocators.login_button)
        submit_button.click()

        wait.until(EC.visibility_of_element_located(HomePageLocators.account_link))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

#Проверка выхода из аккаунта:
    def test_logout(self, create_driver):
        wait = WebDriverWait(driver, 10)
        user = UserData()

        # Login
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(*LoginPageLocators.email_input).send_keys(user.email)
        driver.find_element(*LoginPageLocators.password_input).send_keys(user.password)
        driver.find_element(*LoginPageLocators.login_button).click()

        # Logout
        wait.until(EC.visibility_of_element_located(HomePageLocators.account_link)).click()
        wait.until(EC.visibility_of_element_located(AccountPageLocators.logout_button)).click()

        # Verify logout
        wait.until(EC.visibility_of_element_located(LoginPageLocators.login_label))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
