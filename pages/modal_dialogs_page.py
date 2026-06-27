from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ModalDialogsPage(BasePage):
    def __init__(self, driver, base_url='https://demoqa.com/modal-dialogs'):
        super().__init__(driver, base_url)

    def get_small_modal_button(self):
        return self.driver.find_element(By.ID, 'showSmallModal')

    def get_large_modal_button(self):
        return self.driver.find_element(By.ID, 'showLargeModal')

    def get_close_button_small(self):
        return self.driver.find_element(By.ID, 'closeSmallModal')

    def get_close_button_large(self):
        return self.driver.find_element(By.ID, 'closeLargeModal')

    def click_small_modal_button(self):
        self.get_small_modal_button().click()
        time.sleep(2)

    def click_large_modal_button(self):
        self.get_large_modal_button().click()
        time.sleep(2)

    def click_close_button_small(self):
        self.get_close_button_small().click()
        time.sleep(1)

    def click_close_button_large(self):
        self.get_close_button_large().click()
        time.sleep(1)

    def is_small_modal_visible(self):
        try:
            modal = self.driver.find_element(By.CSS_SELECTOR, ".modal-dialog.modal-sm")
            return modal.is_displayed()
        except:
            return False

    def is_large_modal_visible(self):
        try:
            modal = self.driver.find_element(By.CSS_SELECTOR, ".modal-dialog:not(.modal-sm)")
            return modal.is_displayed()
        except:
            return False

    def is_page_accessible(self):
        try:
            self.driver.get(self.base_url)
            time.sleep(2)
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, 'showSmallModal'))
            )
            return True
        except:
            return False