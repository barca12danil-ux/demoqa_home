from selenium import webdriver
from selenium.webdriver.common.by import By

drver = webdriver.Chrome()
drver.get('https://demoqa.com/')

icon = drver.find_element(By.CSS_SELECTOR,  '"#app > header > a')
if icon is None:
    print('Не найден')
else:
    print('Найден')