from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from ..locators import Locators


def test_create_ad_by_authorized_user(browser, registration_user):

    """
        Создание объявления авторизованным пользователем
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

    # Создаем объявление
    browser.find_element(*Locators.CREATE_AD_BTN).click()

    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(Locators.AD_TITLE_INPUT))

    browser.find_element(*Locators.AD_TITLE_INPUT).send_keys("Азбука")

    browser.find_element(*Locators.AD_DESC_INPUT).send_keys("Книжка для детей")

    browser.find_element(*Locators.AD_PRICE_INPUT).send_keys(100000)

    browser.find_element(*Locators.AD_CATEGORY_DD).click()

    browser.find_element(*Locators.AD_CATEGORY_BOOKS_DD).click()

    browser.find_element(*Locators.AD_CITY_DD).click()

    browser.find_element(*Locators.AD_CITY_KAZAN_DD).click()

    browser.find_element(*Locators.AD_CONDITION_RB).click()

    browser.find_element(*Locators.PUBLISH_AD_BTN).click()

    browser.find_element(*Locators.AVATAR_BTN).click()

    assert browser.find_element(*Locators.AD_NAME_H2).text == "Азбука"


