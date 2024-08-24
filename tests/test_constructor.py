#Проверь, что работают переходы к разделам:
#«Булки»,
#«Соусы»,
#«Начинки».
from selenium.webdriver.common.by import By
from locators import Locators


def test_goto_buns(login):
    driver = login
    driver.find_element(*Locators.LINK_SOUSE).click()
    driver.find_element(*Locators.LINK_BUNS).click()
    assert driver.find_element(By.XPATH, '//span[text()="Булки"]/parent::div[contains(@class,"current")]')


def test_goto_souse(login):
    driver = login
    driver.find_element(*Locators.LINK_SOUSE).click()
    assert driver.find_element(By.XPATH, '//span[text()="Соусы"]/parent::div[contains(@class,"current")]')


def test_goto_fillings(login):
    driver = login
    driver.find_element(*Locators.LINK_FILLING).click()
    assert driver.find_element(By.XPATH, '//span[text()="Начинки"]/parent::div[contains(@class,"current")]')
