from pages.modal_dialogs import ModalDialogs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_modal_elements(driver):
    page = ModalDialogs(driver)

    page.visit()
    time.sleep(3)

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.left-pannel'))
        )
    except:
        pass

    left_panel = driver.find_element(By.CSS_SELECTOR, '.left-pannel')

    buttons = left_panel.find_elements(By.CSS_SELECTOR, 'li.btn')
    button_count = len(buttons)

    print(f"\n\nНайдено кнопок: {button_count}\n\n")

    assert button_count == 5, f"Ожидалось 5 кнопок, но найдено {button_count}"


def test_navigation_modal(driver):
    page = ModalDialogs(driver)

    page.visit()
    time.sleep(3)

    page.refresh_page()
    time.sleep(2)

    page.click_home_icon()
    time.sleep(2)

    page.go_back()
    time.sleep(2)

    page.set_window_size(900, 400)
    time.sleep(1)

    page.go_forward()
    time.sleep(2)

    current_url = page.get_current_url()
    assert 'demoqa.com' in current_url, f"URL должен содержать 'demoqa.com', но получен: {current_url}"

    page_title = page.get_page_title()
    assert page_title, f"Title не должен быть пустым"

    page.set_window_size(1000, 1000)