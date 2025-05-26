from selenium import webdriver
from selenium.webdriver.common.by import By


class Locators:

    # Кнопка "Вход и регистрация" в шапке сайта
    LOGIN_BTN = (By.XPATH, '//*[@id="root"]//button[contains(@class, "buttonSecondary") and contains(., "Вход")]')

    # Кнопка "Нет аккаунта" в форме входа
    NO_ACCOUNT_BTN = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[3]/button[2]')

    # Кнопка "Создать аккаунт" в форме регистрации
    CREATE_ACCOUNT_BTN = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[3]/button[1]')

    # Поле ввода Email в формах входа/регистрации
    EMAIL_INPUT = (By.XPATH, '//input[contains(@class, "input_inputStandart__JweLZ") and @placeholder="Введите Email"]')

    # Поле ввода Пароля в формах входа/регистрации
    PASS_INPUT = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[2]/div[2]/div/div/input')

    # Поле ввода Повторить пароль в формах входа/регистрации
    PASS_REPEAT_INPUT = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[2]/div[3]/div/div/input')

    # Кнопка "Разместить объявление" в шапке сайта
    CREATE_AD_BTN = (By.XPATH, '//button[contains(text(), "Разместить")]')

    # Аватар пользователя в шапке после авторизации
    USER_AVATAR = (By.XPATH, '//*[@id="root"]/div/div[1]/div/div[1]/button/svg')

    # Имя пользователя в шапке после авторизации
    USER_NAME = (By.XPATH, '//*[@id="root"]/div/div[1]/div/div[1]/div/h3')

    # Сообщение "Повторите пароль" в форме регистрации
    REPEAT_PASS_MSG = (By.XPATH, '')

    # Сообщение об ошибке при неверных данных
    ERROR_MSG = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[2]/div[1]/span')

    # Кнопка "Войти" в форме авторизации
    SUBMIT_LOGIN_BTN = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[3]/button[1]')

    # Кнопка "Выйти" на главной странице
    LOGOUT_BTN = (By.XPATH, '//*[@id="root"]/div/div[1]/div/div[1]/div/button')

    # Заголовок "Чтобы разместить объявление, авторизуйтесь"
    H1_NEED_AUTORIZATION = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[1]/h1')

    # Поле "Название" в форме создания объявления
    AD_TITLE_INPUT = (By.XPATH, '//input[@name="name" and @placeholder="Название"]')

    # Поле "Описание товара" в форме создания объявления
    AD_DESC_INPUT = (By.XPATH, '//textarea[@placeholder="Описание товара" and @name="description"]')

    # Поле "Стоимость" в форме создания объявления
    AD_PRICE_INPUT = (By.XPATH, '//input[@placeholder="Стоимость" and @type="text"]')

    # Выпадающий список "Категория" в форме создания объявления
    AD_CATEGORY_DD = (By.XPATH, "(//div[contains(@class, 'dropDownMenu_input__')]//button)[1]")

    # Пункт Книги из списка "Категория" в форме создания объявления
    AD_CATEGORY_BOOKS_DD = (By.XPATH, '//button[contains(@class, "dropDownMenu_btn__o8ARs")]//span[text()="Книги"]')

    # Выпадающий список "Город" в форме создания объявления
    AD_CITY_DD = (By.XPATH, "(//div[contains(@class, 'dropDownMenu_input__')]//button)[2]")

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