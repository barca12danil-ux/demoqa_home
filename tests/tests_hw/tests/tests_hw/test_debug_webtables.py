from selenium.webdriver.common.by import By
import time


def test_debug_modal_visibility(driver):
    driver.get('https://demoqa.com/modal-dialogs')
    time.sleep(2)

    small_btn = driver.find_element(By.ID, 'showSmallModal')
    small_btn.click()
    time.sleep(2)

    print("\n=== ПРОВЕРКА МОДАЛЬНОГО ОКНА ===\n")

    try:
        modal_by_id = driver.find_element(By.ID, 'smallModal')
        print(f"✅ Модальное окно по ID найдено")
        print(f"   Displayed: {modal_by_id.is_displayed()}")
        print(f"   Class: {modal_by_id.get_attribute('class')}")
    except Exception as e:
        print(f"❌ Модальное окно по ID не найдено: {e}")

    try:
        modal_by_class = driver.find_element(By.CLASS_NAME, 'modal-dialog')
        print(f"✅ Модальное окно по классу найдено")
        print(f"   Displayed: {modal_by_class.is_displayed()}")
    except Exception as e:
        print(f"❌ Модальное окно по классу не найдено: {e}")

    all_modals = driver.find_elements(By.XPATH, "//*[contains(@class, 'modal')]")
    print(f"\nВсего modal элементов: {len(all_modals)}")

    for i, modal in enumerate(all_modals):
        displayed = modal.is_displayed()
        classes = modal.get_attribute('class')
        print(f"{i + 1}. Class: '{classes}' Displayed: {displayed}")