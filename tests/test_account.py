#Переход в личный кабинет
#Проверь переход по клику на «Личный кабинет».
#Переход из личного кабинета в конструктор
#Проверь переход по клику на «Конструктор» и на логотип Stellar Burgers.

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
from constants import Constants


def test_lk(driver):
    #Проверь переход по клику на «Личный кабинет»
    driver.get(Constants.URL_LOGIN)
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.BUTTON_ENTER).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(Locators.BUTTON_PLACE_AN_ORDER))
    assert driver.current_url == Constants.URL_MAIN and driver.find_element(*Locators.BUTTON_PLACE_AN_ORDER).text == (
        'Оформить заказ')
    driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Профиль")))
    assert driver.current_url == Constants.URL_PROFILE



def test_goto_constructor_click(driver):
    #переход из личного кабинета по клику на «Конструктор»
    driver.get(Constants.URL_LOGIN)
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.BUTTON_ENTER).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(Locators.BUTTON_PLACE_AN_ORDER))
    assert driver.current_url == Constants.URL_MAIN and driver.find_element(*Locators.BUTTON_PLACE_AN_ORDER).text == (
        'Оформить заказ')
    driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(Locators.TEXT_PROFILE))
    assert driver.current_url == Constants.URL_PROFILE

    driver.find_element(*Locators.BUTTON_CONSTRUCTOR).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(Locators.BUTTON_PLACE_AN_ORDER))
    assert driver.current_url == Constants.URL_MAIN


def test_goto_image_click(driver):
    # переход из личного кабинета через логотип Stellar Burgers.
    driver.get(Constants.URL_MAIN)
    driver.find_element(*Locators.BUTTON_ACCOUNT).click()
    assert driver.current_url == Constants.URL_LOGIN

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.TEXT_ENTER))
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.BUTTON_ENTER).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(Locators.BUTTON_PLACE_AN_ORDER))
    assert driver.current_url == Constants.URL_MAIN and \
           driver.find_element(*Locators.BUTTON_PLACE_AN_ORDER).text == 'Оформить заказ'

    driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.TEXT_PROFILE))
    assert driver.current_url == Constants.URL_PROFILE

    driver.find_element(*Locators.IMAGE_LOGO).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(Locators.BUTTON_PLACE_AN_ORDER))
    assert driver.current_url == Constants.URL_MAIN


def test_exit(driver):
    #Проверь выход по кнопке «Выйти» в личном кабинете.
    driver.get(Constants.URL_LOGIN)
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.BUTTON_ENTER).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(Locators.BUTTON_PLACE_AN_ORDER))
    assert driver.current_url == Constants.URL_MAIN and driver.find_element(*Locators.BUTTON_PLACE_AN_ORDER).text == (
        'Оформить заказ')
    driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.TEXT_PROFILE))
    assert driver.current_url == Constants.URL_PROFILE
    driver.find_element(*Locators.BUTTON_EXIT).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(Locators.TEXT_ENTER))
    assert driver.current_url == Constants.URL_LOGIN
