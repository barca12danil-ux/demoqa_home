from selenium.webdriver.common.by import By
from pages.webtables_page import WebTablesPage
import time


def test_add_record(driver):
    page = WebTablesPage(driver)
    page.visit()
    time.sleep(2)

    page.click_add_button()

    assert page.is_modal_visible(), "Модальное окно не открылось"

    page.fill_form("John", "Doe", "john@example.com", "30", "50000", "IT")
    page.click_submit()

    time.sleep(2)

    assert not page.is_modal_visible(), "Модальное окно не закрылось"

    body_text = page.driver.find_element(By.TAG_NAME, 'body').text
    assert "John Doe" in body_text, "Данные не добавлены в таблицу"


def test_edit_record(driver):
    page = WebTablesPage(driver)
    page.visit()
    time.sleep(2)

    page.click_add_button()
    page.fill_form("Edit", "Test", "edit@example.com", "25", "40000", "HR")
    page.click_submit()
    time.sleep(2)

    page.click_edit(1)
    time.sleep(1)

    first_name_field = page.get_first_name_field()
    first_name_field.clear()
    first_name_field.send_keys("Updated")

    page.click_submit()
    time.sleep(2)

    body_text = page.driver.find_element(By.TAG_NAME, 'body').text
    assert "Updated" in body_text, "Данные не обновлены в таблице"


def test_delete_record(driver):
    page = WebTablesPage(driver)
    page.visit()
    time.sleep(2)

    page.click_add_button()
    page.fill_form("Delete", "Me", "delete@example.com", "20", "30000", "Sales")
    page.click_submit()
    time.sleep(2)

    body_text_before = page.driver.find_element(By.TAG_NAME, 'body').text
    assert "Delete Me" in body_text_before, "Запись не добавлена"

    page.click_delete(1)
    time.sleep(1)

    body_text_after = page.driver.find_element(By.TAG_NAME, 'body').text
    assert "Delete Me" not in body_text_after, "Запись не удалена из таблицы"