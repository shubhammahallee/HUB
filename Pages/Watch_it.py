from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException 
from Pages.BasePage import BasePage
import random


class Watch_it(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)

    def play_video(self):
        try:
            videos = self.wait.until(
                EC.presence_of_all_elements_located((By.XPATH, "//a[@title]")))

            if videos:
                chosen = random.choice(videos)
                self.driver.execute_script("arguments[0].click();", chosen)
                self.driver.fullscreen_window()
                self.log.info("✅ Video played")
            else:
                self.log.info("❌ Not played")

        except (TimeoutException, NoSuchElementException) as e:
            self.log.info(f"❌ Error: {e}")
