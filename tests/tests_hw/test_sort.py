from pages.webtables_page import WebTablesPage
from selenium.webdriver.common.by import By
import time


def test_table_sort(driver):
    page = WebTablesPage(driver)
    page.visit()
    time.sleep(2)

    headers = page.driver.find_elements(By.XPATH, "//div[contains(@class, 'rt-th')]")

    for i, header in enumerate(headers[:3]):
        header_text = header.text.strip()
        if header_text:
            header.click()
            time.sleep(1)

            sort_class = header.get_attribute('class')
            assert 'sorted' in sort_class or 'asc' in sort_class or 'desc' in sort_class, \
                f"Сортировка не применилась к столбцу '{header_text}'. Класс: {sort_class}"