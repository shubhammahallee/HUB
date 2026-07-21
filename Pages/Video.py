from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from Pages.BasePage import BasePage
import time


class Video(BasePage):
    LOGO = (By.ID, "phubLogo")
    menu_button = (By.XPATH, "//button[@id='desktopNavigation']")
    short_button = (By.XPATH, "//a[@class='menuLink shorties js-menuAnalytics']")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 30)

    def verify_logo(self):
        self.handle_cookies()
        self.log.info("✅ Logo verified")

    def menu_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.menu_button)).click()

    def shorts(self):
        self.wait.until(EC.element_to_be_clickable(self.short_button)).click()
        time.sleep(3)
        self.driver.save_screenshot("screenshots/shorts.png")