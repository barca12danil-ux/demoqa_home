from selenium.webdriver.common.by import By
import time


def test_debug_modal_elements(driver):
    driver.get('https://demoqa.com/modal-dialogs')
    time.sleep(2)

    print("\n=== ИЩЕМ КНОПКИ МЕНЮ ===\n")

    all_buttons = driver.find_elements(By.TAG_NAME, 'button')
    print(f"Всего кнопок на странице: {len(all_buttons)}\n")

    for i, btn in enumerate(all_buttons):
        text = btn.text.strip()
        classes = btn.get_attribute('class')
        id_attr = btn.get_attribute('id')

        if text and len(text) < 30:
            print(f"{i + 1}. ID: '{id_attr}'")
            print(f"   Text: '{text}'")
            print(f"   Class: '{classes}'")
            print()

    print("\n=== ИЩЕМ ИКОНКУ HOME ===\n")

    all_links = driver.find_elements(By.TAG_NAME, 'a')
    print(f"Всего ссылок: {len(all_links)}\n")

    for i, link in enumerate(all_links):
        href = link.get_attribute('href')
        classes = link.get_attribute('class')
        text = link.text.strip()

        if 'demoqa.com' in str(href) and ('home' in str(classes).lower() or text == 'DemoQA'):
            print(f"{i + 1}. Href: '{href}'")
            print(f"   Class: '{classes}'")
            print(f"   Text: '{text}'")
            print()

    try:
        logo = driver.find_element(By.XPATH, "//*[@class='logo']")
        print(f"✅ Логотип найден: {logo.get_attribute('class')}")
    except:
        print("❌ Логотип не найден")