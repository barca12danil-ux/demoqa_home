from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ModalDialogs(BasePage):
    def __init__(self, driver, base_url='https://demoqa.com/modal-dialogs'):
        super().__init__(driver, base_url)

    def get_submenu_buttons(self):
        """Получить все кнопки подменю"""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.left-pannel'))
            )
        except:
            pass

        left_panel = self.driver.find_element(By.CSS_SELECTOR, '.left-pannel')
        return left_panel.find_elements(By.CSS_SELECTOR, 'li.btn.btn-light')

    def get_home_icon(self):
        """Получить иконку главной страницы"""
        return self.driver.find_element(By.CSS_SELECTOR, "img[src*='Toolsqa']")

    def count_submenu_buttons(self):
        """Подсчитать количество кнопок"""
        return len(self.get_submenu_buttons())

    def click_home_icon(self):
        """Кликнуть на иконку"""
        self.get_home_icon().click()

    def refresh_page(self):
        """Обновить страницу"""
        self.driver.refresh()

    def go_back(self):
        """Шаг назад"""
        self.driver.back()

    def go_forward(self):
        """Шаг вперед"""
        self.driver.forward()

    def set_window_size(self, width, height):
        """Установить размер окна"""
        self.driver.set_window_size(width, height)

    def get_current_url(self):
        """Получить текущий URL"""
        return self.driver.current_url

    def get_page_title(self):
        """Получить заголовок страницы"""
        return self.driver.title