from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from ..locators import Locators
from ..helpers import generate_email


class TestSuccessfulUserRegistrationWithValidEmail:

    def test_successful_user_registration_with_valid_email(self, browser):
        """
        Успешная регистрация пользователя с email по правильной маске
        """
        email = generate_email()
        password = "password123"

        browser.find_element(*Locators.LOGIN_BTN).click()

        WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable(Locators.NO_ACCOUNT_BTN))

        browser.find_element(*Locators.NO_ACCOUNT_BTN).click()

        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(Locators.CREATE_ACCOUNT_BTN))

        browser.find_element(*Locators.EMAIL_INPUT).send_keys(email)

        browser.find_element(*Locators.PASS_INPUT).send_keys(password)

        browser.find_element(*Locators.PASS_REPEAT_INPUT).send_keys(password)

        browser.find_element(*Locators.CREATE_ACCOUNT_BTN).click()

        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(Locators.USER_NAME))

        assert browser.find_element(*Locators.USER_NAME).text == 'User.'
