from pages.demoqa_page import DemoqaPage


def test_check_footer_text(driver):
    page = DemoqaPage(driver)
    page.visit()
    footer_text = page.get_footer_text()
    # Проверяем что текст содержит TOOLSQA.COM
    assert 'TOOLSQA.COM' in footer_text
    assert 'ALL RIGHTS RESERVED' in footer_text


def test_check_elements_page_text(driver):
    page = DemoqaPage(driver)
    page.visit()
    page.click_elements_button()
    center_text = page.get_center_text()
    assert center_text == 'Please select an item from left to start practice.'