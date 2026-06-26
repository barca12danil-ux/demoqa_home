from pages.accordion import Accordion
import time


def test_visible_accordion(driver):
    page = Accordion(driver)
    page.visit()
    page.wait_page_load()
    time.sleep(2)

    page.click_section1_heading()
    time.sleep(2)

    assert not page.is_section1_content_visible(), "Элемент должен быть скрыт после клика"

def test_visible_accordion_default(driver):
    page = Accordion(driver)
    page.visit()
    page.wait_page_load()
    time.sleep(2)

    assert not page.is_section2_content_p1_visible(), "section2Content > p:nth-child(1) должен быть скрыт"
    assert not page.is_section2_content_p2_visible(), "section2Content > p:nth-child(2) должен быть скрыт"
    assert not page.is_section3_content_visible(), "section3Content > p должен быть скрыт"