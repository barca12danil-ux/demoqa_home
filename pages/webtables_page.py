from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class WebTablesPage(BasePage):
    def __init__(self, driver, base_url='https://demoqa.com/webtables'):
        super().__init__(driver, base_url)

    def get_add_button(self):
        return self.driver.find_element(By.ID, 'addNewRecordButton')

    def get_first_name_field(self):
        return self.driver.find_element(By.ID, 'firstName')

    def get_last_name_field(self):
        return self.driver.find_element(By.ID, 'lastName')

    def get_email_field(self):
        return self.driver.find_element(By.ID, 'userEmail')

    def get_age_field(self):
        return self.driver.find_element(By.ID, 'age')

    def get_salary_field(self):
        return self.driver.find_element(By.ID, 'salary')

    def get_department_field(self):
        return self.driver.find_element(By.ID, 'department')

    def get_submit_button(self):
        return self.driver.find_element(By.ID, 'submit')

    def get_modal_dialog(self):
        return self.driver.find_element(By.CLASS_NAME, 'modal-content')

    def get_table_wrapper(self):
        return self.driver.find_element(By.CLASS_NAME, 'web-tables-wrapper')

    def get_table_rows(self):
        return self.driver.find_elements(By.XPATH, "//div[contains(@class, 'rt-tr-group')]")

    def get_edit_button(self, row_index):
        return self.driver.find_element(By.XPATH, f"(//span[@title='Edit'])[{row_index}]")

    def get_delete_button(self, row_index):
        return self.driver.find_element(By.XPATH, f"(//span[@title='Delete'])[{row_index}]")

    def get_row_data(self, row_index):
        return self.driver.find_elements(By.XPATH,
                                         f"(//div[contains(@class, 'rt-tr-group')])[{row_index}]//div[contains(@class, 'rt-td')]")

    def get_next_button(self):
        return self.driver.find_element(By.XPATH, "//button[text()='Next']")

    def get_previous_button(self):
        return self.driver.find_element(By.XPATH, "//button[text()='Previous']")

    def get_page_info(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'col-auto') and contains(text(), 'Page')]")

    def get_rows_select(self):
        return self.driver.find_element(By.TAG_NAME, 'select')

    def click_add_button(self):
        self.get_add_button().click()
        time.sleep(1)

    def fill_form(self, first_name, last_name, email, age, salary, department):
        self.get_first_name_field().send_keys(first_name)
        self.get_last_name_field().send_keys(last_name)
        self.get_email_field().send_keys(email)
        self.get_age_field().send_keys(age)
        self.get_salary_field().send_keys(salary)
        self.get_department_field().send_keys(department)

    def click_submit(self):
        self.get_submit_button().click()
        time.sleep(1)

    def click_edit(self, row_index):
        self.get_edit_button(row_index).click()
        time.sleep(1)

    def click_delete(self, row_index):
        self.get_delete_button(row_index).click()
        time.sleep(1)

    def get_first_name_value(self):
        return self.get_first_name_field().get_attribute('value')

    def is_modal_visible(self):
        try:
            modal = self.get_modal_dialog()
            return modal.is_displayed()
        except:
            return False

    def get_table_row_count(self):
        return len(self.get_table_rows())

    def is_next_button_disabled(self):
        try:
            next_btn = self.get_next_button()
            disabled = next_btn.get_attribute('disabled')
            return disabled == 'true' or disabled is not None
        except:
            return True

    def is_previous_button_disabled(self):
        try:
            prev_btn = self.get_previous_button()
            disabled = prev_btn.get_attribute('disabled')
            return disabled == 'true' or disabled is not None
        except:
            return True

    def click_next(self):
        next_btn = self.get_next_button()
        next_btn.click()
        time.sleep(1)

    def click_previous(self):
        prev_btn = self.get_previous_button()
        prev_btn.click()
        time.sleep(1)

    def set_rows_per_page(self, count):
        select_element = self.get_rows_select()
        select = Select(select_element)
        select.select_by_visible_text(f'Show {count}')
        time.sleep(1)