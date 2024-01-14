from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
current_url = 'https://stellarburgers.nomoreparties.site/login'

driver.get('https://stellarburgers.nomoreparties.site/')
driver.find_element(By.XPATH, "//div/header/nav/a").click()
assert current_url
driver.guit()
