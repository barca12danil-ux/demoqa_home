from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Accordion(BasePage):
    def __init__(self, driver, base_url='https://demoqa.com/accordion'):
        super().__init__(driver, base_url)

    def wait_page_load(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.ID, 'accordion'))
        )

    def get_section1_content_p(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#section1Content > p')

    def get_section1_heading(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#section1Heading')

    def get_section2_content_p1(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#section2Content > p:nth-child(1)')

    def get_section2_content_p2(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#section2Content > p:nth-child(2)')

    def get_section3_content_p(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#section3Content > p')

    def is_section1_content_visible(self):
        return self.get_section1_content_p().is_displayed()

    def click_section1_heading(self):
        self.get_section1_heading().click()

    def is_section2_content_p1_visible(self):
        return self.get_section2_content_p1().is_displayed()

    def is_section2_content_p2_visible(self):
        return self.get_section2_content_p2().is_displayed()

    def is_section3_content_visible(self):
        return self.get_section3_content_p().is_displayed()