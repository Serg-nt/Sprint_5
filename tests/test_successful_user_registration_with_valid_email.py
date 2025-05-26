from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from ..locators import Locators


def test_successful_user_registration_with_valid_email(browser, registration_user):

    """
        Успешная регистрация пользователя с email по правильной маске
    """
    # Регистрируем пользователя
    user_data = registration_user

    assert browser.find_element(*Locators.USER_NAME).text == 'User.'

    