from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

current_url = 'https://stellarburgers.nomoreparties.site/'

#переход по клику на Конструктор
driver = webdriver.Chrome()
driver.get('https://stellarburgers.nomoreparties.site/profile')
driver.find_element(By.XPATH, "//div/header/nav/ul/li[1]/a").click()
time.sleep(5)
assert current_url
driver.quit()

#переход по лого
driver.get('https://stellarburgers.nomoreparties.site/profile')
driver.find_element(By.XPATH, "//div/header/nav/div/a").click()
time.sleep(5)
assert current_url
driver.quit()
