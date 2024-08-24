#Регистрация
#Проверь:
#Успешную регистрацию.
# Поле «Имя» должно быть не пустым;
# в поле Email введён email в формате логин@домен: например, 123@ya.ru.
# Минимальный пароль — шесть символов.

#Ошибку для некорректного пароля.


import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators


def create_login():
    #генерация логина по формату задания
    login = f"veraegorova13{random.randint(100, 999)}@yandex.ru"
    return login


def create_password(n):
    # генерация цифрового пароля заданной длины
    if n > 2:
        maximum = '9' * n
        minimum = '1' + '0' * (n - 1)
    else:
        maximum = '9'
        minimum = '10'
    password = random.randint(int(minimum), int(maximum))
    return password


def test_form_register_correct_data(driver):
    # проверка успешной регистрации
    driver.get(Constants.URL_REGISTER)
    driver.find_element(*Locators.INPUT_NAME).send_keys(f"Тестовый пользователь {random.randint(1000, 9999)}")
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(create_login())
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(create_password(7))
    driver.find_element(*Locators.BUTTON_REGISTER).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.BUTTON_ENTER))
    assert driver.current_url == Constants.URL_LOGIN


def test_form_register_name_empty(driver):
    # проверка регистрации с пустым именем
    driver.get(Constants.URL_REGISTER)
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(create_login())
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(create_password(7))
    driver.find_element(*Locators.BUTTON_REGISTER).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.BUTTON_REGISTER))
    assert driver.current_url == Constants.URL_REGISTER
def test_form_register_bad_password(driver):
    # проверка некорректного пароля
    driver.get(Constants.URL_REGISTER)
    driver.find_element(*Locators.INPUT_NAME).send_keys(f"name{random.randint(100, 999)}")
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(create_login())
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(create_password(5))
    driver.find_element(*Locators.BUTTON_REGISTER).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ERROR_TEXT_PASSWORD))
    assert driver.find_element(*Locators.ERROR_TEXT_PASSWORD).text == 'Некорректный пароль'
