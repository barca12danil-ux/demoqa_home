from pages.alerts_page import AlertsPage
import time


def test_timer_alert(driver):
    page = AlertsPage(driver)
    page.visit()
    time.sleep(2)

    page.click_timer_alert_button()

    alert = page.wait_for_alert(timeout=10)
    alert_text = alert.text

    assert alert_text, "Алерт не появился или пустой"

    page.accept_alert()
    time.sleep(1)