from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class DemoqaPage(BasePage):
    def __init__(self, driver, base_url='https://demoqa.com/'):
        super().__init__(driver, base_url)

    def get_footer_text(self):
        footer = self.driver.find_element(By.TAG_NAME, 'footer')
        return footer.text

    def click_elements_button(self):
        elements_button = self.driver.find_element(By.CSS_SELECTOR, '.card.mt-4.top-card')
        elements_button.click()

    def get_center_text(self):
        from selenium.webdriver.common.by import By
        element = self.driver.find_element(By.XPATH,
                                           "//*[contains(text(), 'Please select an item from left to start practice.')]")
        return element.text