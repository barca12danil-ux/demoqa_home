from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ModalDialogsPage(BasePage):
    def __init__(self, driver, base_url='https://demoqa.com/modal-dialogs'):
        super().__init__(driver, base_url)

    def get_menu_buttons(self):
        """Все кнопки меню (не уникальный локатор)"""
        return self.driver.find_elements(By.XPATH,
                                         "//div[contains(@class, 'element-group') and not(contains(@class, 'header'))]")

    def get_home_icon(self):
        """Иконка для перехода на главную"""
        all_links = self.driver.find_elements(By.TAG_NAME, 'a')
        for link in all_links:
            href = link.get_attribute('href')
            if href and href.rstrip('/') == 'https://demoqa.com':
                return link
        raise Exception("Home link not found")

    def get_page_title(self):
        """Получить заголовок страницы"""
        return self.driver.title

    def get_current_url(self):
        """Получить текущий URL"""
        return self.driver.current_url

    def refresh_page(self):
        """Обновить страницу"""
        self.driver.refresh()
        time.sleep(2)

    def go_back(self):
        """Шаг назад в браузере"""
        self.driver.back()
        time.sleep(2)

    def go_forward(self):
        """Шаг вперед в браузере"""
        self.driver.forward()
        time.sleep(2)

    def set_window_size(self, width, height):
        """Установить размер окна"""
        self.driver.set_window_size(width, height)
        time.sleep(1)

    def click_home_icon(self):
        """Клик по иконке домой"""
        self.get_home_icon().click()
        time.sleep(2)

    def count_menu_buttons(self):
        """Получить количество кнопок меню"""
        return len(self.get_menu_buttons())