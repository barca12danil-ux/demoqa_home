from selenium.webdriver.common.by import By
import time


def test_debug_all_elements(driver):
    """Отладка - смотрим ВСЕ элементы"""
    driver.get('https://demoqa.com/modal-dialogs')
    time.sleep(5)

    print("\n\n=== ВСЕ ЭЛЕМЕНТЫ В ЛЕВОЙ ПАНЕЛИ ===\n")

    # Ищем левую панель
    try:
        left_panel = driver.find_element(By.CSS_SELECTOR, '.left-pannel')
        print("Найдена левая панель .left-pannel")

        # Все элементы внутри
        all_elements = left_panel.find_elements(By.TAG_NAME, '*')
        print(f"\nВСЕГО ЭЛЕМЕНТОВ В ПАНЕЛИ: {len(all_elements)}")

        for i, el in enumerate(all_elements[:30]):
            tag = el.tag_name
            classes = el.get_attribute('class')
            text = el.text.strip()[:50]
            if text or classes:
                print(f"{i + 1}. <{tag}> class='{classes}' text='{text}'")
    except Exception as e:
        print(f"Левая панель не найдена: {e}")

    print("\n\n=== ИЩЕМ ЛОГОТИП ===\n")

    # Все ссылки
    all_links = driver.find_elements(By.TAG_NAME, 'a')
    print(f"\nВСЕГО ССЫЛОК: {len(all_links)}")
    for i, link in enumerate(all_links[:10]):
        href = link.get_attribute('href')
        text = link.text.strip()[:50]
        classes = link.get_attribute('class')
        if text or href:
            print(f"{i + 1}. href='{href}' class='{classes}' text='{text}'")

    # Все изображения
    all_images = driver.find_elements(By.TAG_NAME, 'img')
    print(f"\nВСЕГО ИЗОБРАЖЕНИЙ: {len(all_images)}")
    for i, img in enumerate(all_images):
        src = img.get_attribute('src')
        alt = img.get_attribute('alt')
        print(f"{i + 1}. src='{src}' alt='{alt}'")

    print("\n=== КОНЕЦ ===\n\n")