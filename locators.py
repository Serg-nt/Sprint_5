from selenium import webdriver
from selenium.webdriver.common.by import By


class Locators:

    # Кнопка "Вход и регистрация"
    LOGIN_BTN = (By.XPATH, '//button[contains(@class, "buttonSecondary") and contains(text(), "Вход")]')

    # Кнопка "Нет аккаунта? Зарегистрироваться"
    NO_ACCOUNT_BTN = (By.XPATH, '//button[contains(@class, "buttonSecondary") and contains(text(), "Нет аккаунта")]')

    # Кнопка "Создать аккаунт"
    CREATE_ACCOUNT_BTN = (By.XPATH, '//button[@type="submit" and contains(text(), "Создать аккаунт")]')

    # Поле ввода email
    EMAIL_INPUT = (By.XPATH, '//input[@placeholder="Введите Email" and @name="email"]')

    # Поле ввода пароля
    PASS_INPUT = (By.XPATH, '//input[@placeholder="Пароль" and @name="password"]')

    # Поле повторного ввода пароля
    PASS_REPEAT_INPUT = (By.XPATH, '//input[@placeholder="Повторите пароль" and @name="submitPassword"]')

    # Кнопка входа в систему
    SUBMIT_LOGIN_BTN = (By.XPATH, '//button[@type="submit" and contains(text(), "Войти")]')

    # Сообщение об ошибке
    ERROR_MSG = (By.XPATH, '//form[contains(@class, "popUp_shell__")]//span[contains(@class, "input_span__") and string-length(text()) > 0]')

    # Кнопка "Выход"
    LOGOUT_BTN = (By.XPATH, '//button[contains(@class, "btnSmall") and text()="Выйти"]')

    # Имя пользователя
    USER_NAME = (By.XPATH, '//h3[contains(@class, "profileText") and contains(@class, "name")]')

    # Кнопка "Разместить объявление" в шапке сайта
    CREATE_AD_BTN = (By.XPATH, '//button[contains(text(), "Разместить")]')

    # Заголовок "Чтобы разместить объявление, авторизуйтесь"
    H1_NEED_AUTORIZATION = (By.XPATH, "//form//h1[contains(@class, 'h1') and contains(text(), 'разместить объявление')]")

    # Поле "Название" в форме создания объявления
    AD_TITLE_INPUT = (By.XPATH, '//input[@name="name" and @placeholder="Название"]')

    # Поле "Описание товара" в форме создания объявления
    AD_DESC_INPUT = (By.XPATH, '//textarea[@placeholder="Описание товара" and @name="description"]')

    # Поле "Стоимость" в форме создания объявления
    AD_PRICE_INPUT = (By.XPATH, '//input[@placeholder="Стоимость" and @type="text"]')

    # Выпадающий список "Категория" в форме создания объявления
    AD_CATEGORY_DD = (By.XPATH, "(//div[contains(@class, 'dropDownMenu_input__')]//button[contains(@class, 'dropDownMenu_arrowDown__')])[1]")

    # Пункт Книги из списка "Категория" в форме создания объявления
    AD_CATEGORY_BOOKS_DD = (By.XPATH, '//button[contains(@class, "dropDownMenu_btn__o8ARs")]//span[text()="Книги"]')

    # Выпадающий список "Город" в форме создания объявления
    AD_CITY_DD = (By.XPATH, "(//div[contains(@class, 'dropDownMenu_input__')]//button[contains(@class, 'dropDownMenu_arrowDown__')])[2]")

    # Пункт Казань из списка "Город" в форме создания объявления
    AD_CITY_KAZAN_DD = (By.XPATH, "//button[.//span[contains(text(), 'Казань')]]")

    # Радиокнопки "Состояние товара" в форме создания объявления
    AD_CONDITION_RB = (By.XPATH, "//form//fieldset//div[contains(@class, 'radioUnput_inputRegular__FbVbr')]")

    # Кнопка "Опубликовать" в форме создания объявления
    PUBLISH_AD_BTN = (By.XPATH, "//button[contains(text(), 'Опубликовать')]")

    # Переход в личный кабинет
    AVATAR_BTN = (By.XPATH, "//button[@class='circleSmall']")

    # Переход в личный кабинет
    AD_NAME_H2 = (By.XPATH, "//h2[text()='Азбука']")