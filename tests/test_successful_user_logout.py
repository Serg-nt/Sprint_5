from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from ..locators import Locators


class TestSuccessfulUserLogout:

    def test_successful_user_logout(self, browser, registration_user):
        """
        Успешный выход пользователя из системы
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

        # Выйти из системы
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGOUT_BTN))

        browser.find_element(*Locators.LOGOUT_BTN).click()

        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BTN))

        assert browser.find_element(*Locators.LOGIN_BTN).text == 'Вход и регистрация'
