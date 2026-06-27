from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class TextBoxPage(BasePage):
    def __init__(self, driver, base_url='https://demoqa.com/text-box'):
        super().__init__(driver, base_url)

    def get_full_name_field(self):
        return self.driver.find_element(By.ID, 'userName')

    def get_email_field(self):
        return self.driver.find_element(By.ID, 'userEmail')

    def get_current_address_field(self):
        return self.driver.find_element(By.ID, 'currentAddress')

    def get_permanent_address_field(self):
        return self.driver.find_element(By.ID, 'permanentAddress')

    def get_submit_button(self):
        return self.driver.find_element(By.ID, 'submit')

    def get_output_name(self):
        return self.driver.find_element(By.ID, 'name')

    def get_output_email(self):
        return self.driver.find_element(By.ID, 'email')

    def get_output_current_address(self):
        return self.driver.find_element(By.XPATH, "//*[@id='output']//p[@id='currentAddress']")

    def get_output_permanent_address(self):
        return self.driver.find_element(By.XPATH, "//*[@id='output']//p[@id='permanentAddress']")

    def fill_full_name(self, text):
        self.get_full_name_field().send_keys(text)

    def fill_current_address(self, text):
        self.get_current_address_field().send_keys(text)

    def click_submit(self):
        self.get_submit_button().click()

    def get_output_name_text(self):
        return self.get_output_name().text

    def get_output_current_address_text(self):
        return self.get_output_current_address().text