from .urls import BASE_URL
from .helpers import generate_email
from .locators import Locators
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Firefox()
    driver.get(BASE_URL)

    yield driver

    driver.quit()


@pytest.fixture
def registration_user(browser):

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

    return {"email": email, "password": password}
    