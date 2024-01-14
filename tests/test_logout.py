#done
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

# инициализируем драйвер браузера
driver = webdriver.Chrome()
current_url_profile = 'https://stellarburgers.nomoreparties.site/account/profile'
current_url = 'https://stellarburgers.nomoreparties.site/login'

#вход по кнопке «Войти в аккаунт» на главной
driver.get('https://stellarburgers.nomoreparties.site/')
driver.find_element(By.XPATH, "//div/header/nav/a").click()
#вход
driver.find_element(By.XPATH, "//fieldset[1]/div/div/input").send_keys("Elenabasova4123@yandex.ru")
driver.find_element(By.XPATH, "//fieldset[2]/div/div/input").send_keys("sport1234")
driver.find_element(By.XPATH, "//div/form/button").click()
driver.find_element(By.XPATH, "//div/header/nav/a").click()
assert current_url
driver.quite()

