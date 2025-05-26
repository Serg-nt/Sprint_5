from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from ..locators import Locators


def test_create_ad_requires_authorization(browser):

    """
        Попытка создания объявления неавторизованным пользователем
    """

    browser.find_element(*Locators.CREATE_AD_BTN).click()

    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(Locators.H1_NEED_AUTORIZATION))

    assert browser.find_element(*Locators.H1_NEED_AUTORIZATION).text == 'Чтобы разместить объявление, авторизуйтесь'