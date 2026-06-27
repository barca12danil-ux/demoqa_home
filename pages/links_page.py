from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class LinksPage(BasePage):
    def __init__(self, driver, base_url='https://demoqa.com/links'):
        super().__init__(driver, base_url)

    def get_home_link(self):
        return self.driver.find_element(By.ID, 'simpleLink')

    def get_home_link_text(self):
        return self.get_home_link().text

    def get_home_link_href(self):
        return self.get_home_link().get_attribute('href')

    def click_home_link(self):
        self.get_home_link().click()
        time.sleep(2)

    def get_all_window_handles(self):
        return self.driver.window_handles

    def switch_to_new_tab(self):
        handles = self.get_all_window_handles()
        if len(handles) > 1:
            self.driver.switch_to.window(handles[-1])
            return True
        return False