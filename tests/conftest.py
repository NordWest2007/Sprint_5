import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators


@pytest.fixture()
def driver():
    driver_chrome = webdriver.Chrome()
    yield driver_chrome

    driver_chrome.quit()


@pytest.fixture()
def login(driver):
    driver.get(Constants.URL_MAIN)
    driver.find_element(*Locators.BUTTON_ACCOUNT).click()
    assert driver.current_url == Constants.URL_LOGIN
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(Locators.TEXT_ENTER))
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.BUTTON_ENTER).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(Locators.BUTTON_PLACE_AN_ORDER))
    assert driver.current_url == Constants.URL_MAIN
    return driver
