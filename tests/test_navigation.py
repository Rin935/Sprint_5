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

#Проверка перехода в личный кабинет
class TestNavigation:

    def test_account_navigation(self, create_driver):
        wait = WebDriverWait(driver, 10)
        user = UserData()

        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(*LoginPageLocators.email_input).send_keys(user.email)
        driver.find_element(*LoginPageLocators.password_input).send_keys(user.password)
        driver.find_element(*LoginPageLocators.login_button).click()

        wait.until(EC.visibility_of_element_located(HomePageLocators.account_link)).click()

        wait.until(EC.visibility_of_element_located(AccountPageLocators.profile_link))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"

#Проверка перехода из личного кабинета в конструктор: переход по клику на «Конструктор»
    def test_constructor_navigation(self, create_driver):
        wait = WebDriverWait(driver, 10)
        user = UserData()

        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(*LoginPageLocators.email_input).send_keys(user.email)
        driver.find_element(*LoginPageLocators.password_input).send_keys(user.password)
        driver.find_element(*LoginPageLocators.login_button).click()
        wait.until(EC.visibility_of_element_located(HomePageLocators.account_link)).click()

        wait.until(EC.visibility_of_element_located(HomePageLocators.constructor_link)).click()

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

#Проверка перехода из личного кабинета в конструктор: переход по клику на логотип Stellar Burgers
    def test_logo_navigation(self, create_driver):
        wait = WebDriverWait(driver, 10)
        user = UserData()

        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(*LoginPageLocators.email_input).send_keys(user.email)
        driver.find_element(*LoginPageLocators.password_input).send_keys(user.password)
        driver.find_element(*LoginPageLocators.login_input).click()
        wait.until(EC.visibility_of_element_located(HomePageLocators.account_link)).click()

        wait.until(EC.visibility_of_element_located(HomePageLocators.logo)).click()

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"


#Проверка раздела «Конструктор»: переход к разделу «Булки»
class TestConstructor:

    def test_buns(self, create_driver):
        wait = WebDriverWait(driver, 10)
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(*HomePageLocators.buns).click()

        active_section = wait.until(EC.visibility_of_element_located(HomePageLocators.active_section))
        assert "Булки" in active_section.text

#Проверка раздела «Конструктор»: переход к разделу «Соусы»
    def test_sauces(self, create_driver):
        wait = WebDriverWait(driver, 10)
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(*HomePageLocators.sauces).click()

        active_section = wait.until(EC.visibility_of_element_located(HomePageLocators.active_section))
        assert "Соусы" in active_section.text

#Проверка раздела «Конструктор»: переход к разделу «Начинки»
    def test_fillings(self, create_driver):
        wait = WebDriverWait(driver, 10)
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(*HomePageLocators.filling).click()

        active_section = wait.until(EC.visibility_of_element_located(HomePageLocators.active_section))
        assert "Начинки" in active_section.text