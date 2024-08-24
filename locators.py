from selenium.webdriver.common.by import By


class Locators:
    # Главная страница
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, '//p[text()="Личный Кабинет"]')  # кнопка Личный кабинет
    BUTTON_PLACE_AN_ORDER = (By.XPATH, '//button[text()="Оформить заказ"]')   # кнопка Оформить заказ
    BUTTON_CONSTRUCTOR = (By.XPATH, '//p[text()="Конструктор"]')  # кнопка Конструктор
    BUTTON_ACCOUNT = (By.XPATH, '//button[text()="Войти в аккаунт"]')  # кнопка Войти в аккаунт
    IMAGE_LOGO = (By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]')  # Логотип
    LINK_BUNS = (By.XPATH, '//span[text()="Булки"]/parent::div')  # закладка Булки
    LINK_SOUSE = (By.XPATH, '//span[text()="Соусы"]')  # закладка Соусы
    LINK_FILLING = (By.XPATH, '//span[text()="Начинки"]')  # закладка Начинки

    # Страница регистрации
    BUTTON_REGISTER = (By.XPATH, '//button[text()="Зарегистрироваться"]')  # кнопка Зарегистрироваться
    INPUT_NAME = (By.XPATH, '//label[text()="Имя"]/parent::div/input')  # поле для ввода имени
    INPUT_EMAIL = (By.XPATH, '//label[text()="Email"]/parent::div/input')  # поле для ввода email
    INPUT_PASSWORD = (By.XPATH, '//label[text()="Пароль"]/parent::div/input')  # поле для ввода пароля
    ERROR_TEXT_PASSWORD = (
    By.XPATH, '//p[@class="input__error text_type_main-default"]')  # тект ошибки Некорректный пароль

    # Страница логина
    TEXT_ENTER = (By.XPATH, '//h2[text()="Вход"]')  # надпись Вход
    BUTTON_ENTER = (By.XPATH, '//button[text()="Войти"]')  # кнопка Войти

    # Страница профиля
    TEXT_PROFILE = (By.LINK_TEXT, "Профиль")  # ссылка Профиль
    BUTTON_EXIT = (By.XPATH, '//button[text()="Выход"]')  # Кнопка Выход

    # Страница Забыли пароль
    TEXT_LINK_ENTER = (By.LINK_TEXT, 'Войти')  # ссылка Войти
