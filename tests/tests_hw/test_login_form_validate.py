from pages.practice_form_page import PracticeFormPage
import time


def test_login_form_validate(driver):
    page = PracticeFormPage(driver)
    page.visit()
    time.sleep(2)

    first_name_placeholder = page.get_first_name_placeholder()
    assert first_name_placeholder == "First Name", f"Ожидался 'First Name', получено: {first_name_placeholder}"

    last_name_placeholder = page.get_last_name_placeholder()
    assert last_name_placeholder == "Last Name", f"Ожидался 'Last Name', получено: {last_name_placeholder}"

    email_placeholder = page.get_email_placeholder()
    assert email_placeholder == "name@example.com", f"Ожидался 'name@example.com', получено: {email_placeholder}"

    email_pattern = page.get_email_pattern()
    assert email_pattern, f"Атрибут pattern не найден у email поля"

    page.click_submit()
    time.sleep(2)

    form_class = page.get_form_class()
    assert "was-validated" in form_class, f"Класс 'was-validated' не найден. Текущие классы: {form_class}"