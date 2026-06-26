from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ModalDialogs(BasePage):
    def __init__(self, driver, base_url='https://demoqa.com/modal-dialogs'):
        super().__init__(driver, base_url)

    def get_submenu_buttons(self):
        return self.driver.find_elements(By.CSS_SELECTOR, '.sidebar .menu-list .nav-item .btn')

    def get_home_icon(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.navbar-brand')

    def count_submenu_buttons(self):
        return len(self.get_submenu_buttons())

    def click_home_icon(self):
        self.get_home_icon().click()

    def refresh_page(self):
        self.driver.refresh()

    def go_back(self):
        self.driver.back()

    def go_forward(self):
        self.driver.forward()

    def set_window_size(self, width, height):
        self.driver.set_window_size(width, height)

    def get_current_url(self):
        return self.driver.current_url

    def get_page_title(self):
        return self.driver.title