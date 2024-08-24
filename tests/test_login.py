#Вход
#Проверь:
#вход по кнопке «Войти в аккаунт» на главной,
#вход через кнопку «Личный кабинет»,
#вход через кнопку в форме регистрации,
#вход через кнопку в форме восстановления пароля.

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
from constants import Constants

#
def test_login_main_form(driver):
    # вход по кнопке «Войти в аккаунт» на главной,
    driver.get(Constants.URL_MAIN)
    driver.find_element(*Locators.BUTTON_ACCOUNT).click()
    assert driver.current_url == Constants.URL_LOGIN
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.TEXT_ENTER))
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.BUTTON_ENTER).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.BUTTON_PLACE_AN_ORDER))
    assert driver.current_url == Constants.URL_MAIN and driver.find_element(
        *Locators.BUTTON_PLACE_AN_ORDER).text == 'Оформить заказ'


def test_login_personal_classroom(driver):
    # вход через кнопку «Личный кабинет»,
    driver.get(Constants.URL_MAIN)
    driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
    assert driver.current_url == Constants.URL_LOGIN
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.TEXT_ENTER))
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.BUTTON_ENTER).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.BUTTON_PLACE_AN_ORDER))
    assert (driver.current_url == Constants.URL_MAIN and
            driver.find_element(*Locators.BUTTON_PLACE_AN_ORDER).text == 'Оформить заказ')


def test_login_from_register_form(driver):
    # вход через кнопку в форме регистрации,
    driver.get(Constants.URL_REGISTER)
    driver.find_element(By.LINK_TEXT, 'Войти').click()
    assert driver.current_url == Constants.URL_LOGIN
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.TEXT_ENTER))
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.BUTTON_ENTER).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.BUTTON_PLACE_AN_ORDER))
    assert (driver.current_url == Constants.URL_MAIN and
            driver.find_element(*Locators.BUTTON_PLACE_AN_ORDER).text == 'Оформить заказ')


def test_login_from_forgot_password(driver):
    # вход через кнопку в форме восстановления пароля.
    driver.get(Constants.URL_FORGOT_PASSWORD)
    driver.find_element(*Locators.TEXT_LINK_ENTER).click()
    assert driver.current_url == Constants.URL_LOGIN
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.TEXT_ENTER))
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.BUTTON_ENTER).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.BUTTON_PLACE_AN_ORDER))
    assert (driver.current_url == Constants.URL_MAIN and
            driver.find_element(*Locators.BUTTON_PLACE_AN_ORDER).text == 'Оформить заказ')
