from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException 
from Utilities.Logger import Log_details


class BasePage:
    ENTER_BTN = (By.XPATH, "//button[normalize-space()='Ich bin 18 oder älter - Eingabe']")
    COOKIE_BTN = (By.XPATH, "//button[contains(text(), 'Ok') or contains(@class, 'accept')]")
    COOKIE_BTN_ALT = (By.XPATH, "//button[@class='buttonBase js-acceptGlobalCookies']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.log = Log_details.get_logger()

    def enter_age_gate(self):
        self.wait.until(EC.element_to_be_clickable(self.ENTER_BTN)).click()
        self.log.info("Age gate passed")

    def handle_cookies(self):
        try:
            cookie = self.wait.until(EC.any_of(
                EC.element_to_be_clickable(self.COOKIE_BTN),
                EC.element_to_be_clickable(self.COOKIE_BTN_ALT)
            ))
            cookie.click()
            self.log.info("✅ Cookie popup closed")
        except (TimeoutException, NoSuchElementException):
            self.log.info("ℹ️ No cookie popup found")

    # Alias — keeps old test calls working
    def handle_cookie_popup(self):
        self.handle_cookies()
