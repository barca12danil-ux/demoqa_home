from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class PracticeFormPage(BasePage):
    def __init__(self, driver, base_url='https://demoqa.com/automation-practice-form'):
        super().__init__(driver, base_url)

    def get_first_name_field(self):
        return self.driver.find_element(By.ID, 'firstName')

    def get_last_name_field(self):
        return self.driver.find_element(By.ID, 'lastName')

    def get_email_field(self):
        return self.driver.find_element(By.ID, 'userEmail')

    def get_submit_button(self):
        return self.driver.find_element(By.ID, 'submit')

    def get_form_element(self):
        return self.driver.find_element(By.ID, 'userForm')

    def get_state_dropdown(self):
        return self.driver.find_element(By.ID, 'state')

    def get_city_dropdown(self):
        return self.driver.find_element(By.ID, 'city')

    def get_first_name_placeholder(self):
        return self.get_first_name_field().get_attribute('placeholder')

    def get_last_name_placeholder(self):
        return self.get_last_name_field().get_attribute('placeholder')

    def get_email_placeholder(self):
        return self.get_email_field().get_attribute('placeholder')

    def get_email_pattern(self):
        return self.get_email_field().get_attribute('pattern')

    def click_submit(self):
        self.get_submit_button().click()

    def get_form_class(self):
        return self.get_form_element().get_attribute('class')

    def fill_state(self, state_name):
        state_field = self.get_state_dropdown()
        state_field.click()
        time.sleep(1)

        state_option = self.driver.find_element(By.XPATH,
                                                f"//div[contains(@class, 'option') and text()='{state_name}']")
        state_option.click()

    def fill_city(self, city_name):
        city_field = self.get_city_dropdown()
        city_field.click()
        time.sleep(1)

        city_option = self.driver.find_element(By.XPATH, f"//div[contains(@class, 'option') and text()='{city_name}']")
        city_option.click()