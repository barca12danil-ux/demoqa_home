from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class AlertsPage(BasePage):
    def __init__(self, driver, base_url='https://demoqa.com/alerts'):
        super().__init__(driver, base_url)

    def get_timer_alert_button(self):
        return self.driver.find_element(By.ID, 'timerAlertButton')

    def click_timer_alert_button(self):
        self.get_timer_alert_button().click()

    def wait_for_alert(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        return self.driver.switch_to.alert

    def get_alert_text(self):
        alert = self.wait_for_alert()
        return alert.text

    def accept_alert(self):
        alert = self.wait_for_alert()
        alert.accept()