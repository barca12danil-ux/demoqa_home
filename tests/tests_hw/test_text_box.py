from pages.text_box_page import TextBoxPage
import time


def test_text_box(driver):
    page = TextBoxPage(driver)
    page.visit()
    time.sleep(2)

    full_name = "John Doe"
    current_address = "123 Main Street, New York"

    page.fill_full_name(full_name)
    page.fill_current_address(current_address)

    page.click_submit()
    time.sleep(2)

    output_name = page.get_output_name_text()
    output_address = page.get_output_current_address_text()

    assert full_name in output_name, f"Имя '{full_name}' не найдено в выводе: {output_name}"
    assert current_address in output_address, f"Адрес '{current_address}' не найден в выводе: {output_address}"