from selenium.webdriver.common.by import By
import time


def test_debug_elements_page(driver):
    driver.get('https://demoqa.com/')
    time.sleep(2)

    elements_button = driver.find_element(By.CSS_SELECTOR, '.card.mt-4.top-card')
    elements_button.click()
    time.sleep(2)

    print(f"\n\nURL: {driver.current_url}\n")

    body = driver.find_element(By.TAG_NAME, 'body')
    print(f"BODY TEXT:\n{body.text}\n")

    text_center_elements = driver.find_elements(By.CSS_SELECTOR, '.text-center')
    print(f"\nНайдено .text-center элементов: {len(text_center_elements)}")

    for i, el in enumerate(text_center_elements):
        print(f"TEXT-CENTER {i}: {el.text}")

    all_elements = driver.find_elements(By.CSS_SELECTOR, 'div, p, span')
    print(f"\nВсе элементы с текстом:")
    for i, el in enumerate(all_elements[:20]):
        if el.text.strip():
            print(f"{i}: [{el.tag_name}] {el.text[:100]}")