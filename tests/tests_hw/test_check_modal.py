from pages.modal_dialogs_page import ModalDialogsPage
import pytest


def test_modal_dialogs(driver):
    page = ModalDialogsPage(driver)

    if not page.is_page_accessible():
        pytest.skip("Страница модальных диалогов недоступна")

    page.visit()

    page.click_small_modal_button()
    assert page.is_small_modal_visible(), "Маленькое модальное окно не открылось"

    page.click_close_button_small()
    assert not page.is_small_modal_visible(), "Маленькое модальное окно не закрылось"

    page.click_large_modal_button()
    assert page.is_large_modal_visible(), "Большое модальное окно не открылось"

    page.click_close_button_large()
    assert not page.is_large_modal_visible(), "Большое модальное окно не закрылось"