from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from ..locators import Locators


class TestSuccessfulUserLogin:

    def test_successful_user_login(self, browser, registration_user):
        """
        Успешный вход зарегистрированного пользователя
        """

        # Регистрируем пользователя
        user_data = registration_user

        # Выйти из учетной записи
        browser.find_element(*Locators.LOGOUT_BTN).click()

        WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable(Locators.LOGIN_BTN))

        # Войти под уже существующим пользователем
        browser.find_element(*Locators.LOGIN_BTN).click()

        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(Locators.EMAIL_INPUT))

        browser.find_element(*Locators.EMAIL_INPUT).send_keys(user_data['email'])

        browser.find_element(*Locators.PASS_INPUT).send_keys(user_data['password'])

        browser.find_element(*Locators.SUBMIT_LOGIN_BTN).click()

        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(Locators.USER_NAME))

        assert browser.find_element(*Locators.USER_NAME).text == 'User.'
