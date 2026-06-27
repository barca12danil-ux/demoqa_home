from pages.links_page import LinksPage
import time


def test_home_link_new_tab(driver):
    page = LinksPage(driver)
    page.visit()
    time.sleep(2)

    link_text = page.get_home_link_text()
    assert link_text == "Home", f"Текст ссылки должен быть 'Home', получено: '{link_text}'"

    link_href = page.get_home_link_href()
    assert "demoqa.com" in link_href, f"Href должен содержать 'demoqa.com', получено: '{link_href}'"

    initial_handles = len(page.get_all_window_handles())

    page.click_home_link()
    time.sleep(2)

    new_handles = len(page.get_all_window_handles())
    assert new_handles > initial_handles, "Новая вкладка не открылась"

    page.switch_to_new_tab()
    time.sleep(1)