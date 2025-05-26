from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from ..locators import Locators


def test_registration_with_invalid_email_format(browser):

    """
        Попытка регистрации с email не соответствующем формату *@*.*
    """

    password = "password123"

    browser.find_element(*Locators.LOGIN_BTN).click()

    WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable(Locators.NO_ACCOUNT_BTN))

    browser.find_element(*Locators.NO_ACCOUNT_BTN).click()

    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(Locators.CREATE_ACCOUNT_BTN))

    browser.find_element(*Locators.EMAIL_INPUT).send_keys("1234")

    browser.find_element(*Locators.PASS_INPUT).send_keys(password)

    browser.find_element(*Locators.PASS_REPEAT_INPUT).send_keys(password)

    browser.find_element(*Locators.CREATE_ACCOUNT_BTN).click()

    assert browser.find_element(*Locators.ERROR_MSG).text == 'Ошибка'