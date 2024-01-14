from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get('https://stellarburgers.nomoreparties.site')
driver.find_element(By.XPATH, "//section[1]/div[1]/div[2]/span").click()
time.sleep(5)
driver.find_element(By.XPATH, "//section[1]/div[1]/div[3]/span").click()
time.sleep(5)
driver.find_element(By.XPATH, "//section[1]/div[1]/div[1]/span").click()
time.sleep(5)


driver.quit()
