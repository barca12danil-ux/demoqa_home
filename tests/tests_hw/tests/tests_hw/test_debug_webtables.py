from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_debug_pagination(driver):
    driver.get('https://demoqa.com/webtables')

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'addNewRecordButton'))
    )

    time.sleep(2)

    all_divs = driver.find_elements(By.TAG_NAME, 'div')

    for i, div in enumerate(all_divs):
        text = div.text.strip()
        classes = div.get_attribute('class')
        if 'Page 1' in text or 'of 1' in text:
            print(f"НАЙДЕНО!")
            print(f"Index: {i}")
            print(f"Class: '{classes}'")
            print(f"Text: '{text}'")
            print()


    for i, div in enumerate(all_divs):
        text = div.text.strip()
        classes = div.get_attribute('class')
        if 'Page' in text and len(text) < 50:
            print(f"{i + 1}. class='{classes}' text='{text}'")