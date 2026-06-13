from pages.swag_labs import SwagLabs

def test_check_icon(driver):
    page = SwagLabs(driver)
    page.visit()
    assert page.exist_icon()

def test_check_username_field(driver):
    page = SwagLabs(driver)
    page.visit()
    assert page.exist_username_field()

def test_check_password_field(driver):
    page = SwagLabs(driver)
    page.visit()
    assert page.exist_password_field()