from pages.practice_form_page import PracticeFormPage
import time


def test_fill_state_and_city(driver):
    page = PracticeFormPage(driver)
    page.visit()
    time.sleep(2)

    page.fill_state("NCR")
    time.sleep(1)

    page.fill_city("Delhi")
    time.sleep(1)

    state_field = page.get_state_dropdown()
    city_field = page.get_city_dropdown()

    assert state_field, "Поле State не найдено"
    assert city_field, "Поле City не найдено"