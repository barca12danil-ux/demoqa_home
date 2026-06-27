from selenium.webdriver.common.by import By
import time


def test_debug_modal_elements(driver):
    driver.get('https://demoqa.com/modal-dialogs')
    time.sleep(2)

    print("\n=== ИЩЕМ 5 КНОПОК МЕНЮ ===\n")

    all_divs = driver.find_elements(By.TAG_NAME, 'div')

    menu_items = []
    for div in all_divs:
        text = div.text.strip()
        classes = div.get_attribute('class')

        if text in ['Elements', 'Forms', 'Alerts, Frame & Windows', 'Widgets', 'Interactions']:
            menu_items.append({
                'text': text,
                'class': classes,
                'tag': div.tag_name
            })

    print(f"Найдено элементов меню: {len(menu_items)}\n")
    for i, item in enumerate(menu_items):
        print(f"{i + 1}. Text: '{item['text']}'")
        print(f"   Class: '{item['class']}'")
        print(f"   Tag: {item['tag']}")
        print()

    print("\n=== ИЩЕМ ИКОНКУ HOME ===\n")

    all_links = driver.find_elements(By.TAG_NAME, 'a')

    for i, link in enumerate(all_links):
        href = link.get_attribute('href')

        if href and ('demoqa.com' in href and href.rstrip('/') in ['https://demoqa.com', 'https://demoqa.com/']):
            print(f"✅ НАЙДЕНА HOME ССЫЛКА!")
            print(f"   Index: {i + 1}")
            print(f"   Href: '{href}'")
            print(f"   Class: '{link.get_attribute('class')}'")
            print(f"   Text: '{link.text.strip()}'")
            print(f"   Tag: {link.tag_name}")

            try:
                svg = link.find_element(By.TAG_NAME, 'svg')
                print(f"   ✅ Содержит SVG")
            except:
                print(f"   ❌ Без SVG")
            print()
            break

    print("\n=== ВСЕ ССЫЛКИ С demoqa.com ===\n")

    for i, link in enumerate(all_links[:5]):
        href = link.get_attribute('href')
        if href and 'demoqa.com' in href:
            print(f"{i + 1}. Href: '{href}' | Text: '{link.text.strip()}' | Class: '{link.get_attribute('class')}'")