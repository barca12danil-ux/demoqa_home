from pages.modal_dialogs import ModalDialogsPage
import time


def test_modal_elements(driver):
    """
    Проверка наличия кнопок меню на странице Modal Dialogs
    """
    # a. Перейти на страницу
    page = ModalDialogsPage(driver)
    page.visit()
    time.sleep(2)

    # b. Проверить что кнопок подменю 5 штук
    buttons_count = page.count_menu_buttons()
    assert buttons_count >= 5, f"Ожидалось минимум 5 кнопок, найдено: {buttons_count}"


def test_navigation_modal(driver):
    """
    Проверка навигации на странице Modal Dialogs
    """
    # a. Перейти на страницу
    page = ModalDialogsPage(driver)
    page.visit()
    time.sleep(2)

    # b. Обновить страницу
    page.refresh_page()

    # c. Перейти на главную через иконку
    page.click_home_icon()

    # d. Шаг назад
    page.go_back()

    # e. Установить размеры экрана 900x400
    page.set_window_size(900, 400)

    # f. Шаг вперед
    page.go_forward()

    # g. Проверка URL на главной странице
    page.click_home_icon()
    current_url = page.get_current_url()
    assert "demoqa.com" in current_url and "/modal" not in current_url, \
        f"Неверный URL: {current_url}"

    # h. Проверка title на главной
    title = page.get_page_title()
    assert title, "Title пустой"

    # i. Вернуть размеры экрана по умолчанию
    page.set_window_size(1000, 1000)