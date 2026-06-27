from pages.webtables_page import WebTablesPage
from selenium.webdriver.common.by import By
import time


def test_pagination(driver):
    page = WebTablesPage(driver)
    page.visit()
    time.sleep(2)

    page.set_rows_per_page(10)
    time.sleep(1)

    assert page.is_previous_button_disabled(), "Кнопка Previous должна быть заблокирована"

    for i in range(12):
        page.click_add_button()
        page.fill_form(f"User{i}", f"Test{i}", f"user{i}@example.com", "25", "40000", "HR")
        page.click_submit()
        time.sleep(1)

    page_info = page.get_page_info()
    assert "of 2" in page_info.text or "of 3" in page_info.text, f"Не появилась 2-я страница. Информация: {page_info.text}"

    assert not page.is_next_button_disabled(), "Кнопка Next должна быть доступна"

    page.click_next()
    time.sleep(1)

    page.click_previous()
    time.sleep(1)