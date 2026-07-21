from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from Pages.BasePage import BasePage
import time
import random


class HomePage(BasePage):
    SEARCH_INPUT = (By.ID, "searchInput")
    NEXT_PAGE_BTN = (By.XPATH, "//li[@class='page_next omega']//a[@class='orangeButton']")
    VIDEO_LINKS = (By.XPATH, "//a[@title]")

    def __init__(self, driver):
        super().__init__(driver)

    def verify_page_loaded(self):
        try:
            self.wait.until(EC.presence_of_element_located(self.SEARCH_INPUT))
            self.log.info("✅ Homepage loaded successfully")
            self.driver.save_screenshot("screenshots/homepage.png")
        except (TimeoutException, NoSuchElementException) as e:
            raise AssertionError(f"❌ Homepage did not load properly: {e}")

    def search(self, keyword="pink"):
        try:
            search_box = self.wait.until(EC.element_to_be_clickable((By.NAME, "search")))
            search_box.clear()
            search_box.send_keys(keyword)
            search_box.send_keys(Keys.ENTER)
            self.log.info(f"✅ Searched for '{keyword}'")
        except (TimeoutException, NoSuchElementException) as e:
            raise AssertionError(f"❌ Search failed: {e}")

    def go_to_next_page(self):
        try:
            next_btn = self.wait.until(EC.element_to_be_clickable(self.NEXT_PAGE_BTN))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_btn)
            next_btn.click()
            self.log.info("✅ Next page clicked")
        except (TimeoutException, NoSuchElementException) as e:
            raise AssertionError(f"❌ Failed to go to next page: {e}")

    def play_random_video(self, watch_time=30):
        try:
            videos = self.wait.until(EC.presence_of_all_elements_located(self.VIDEO_LINKS))

            if not videos:
                raise AssertionError("❌ No videos found on the page")

            video = random.choice(videos)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", video)
            self.wait.until(EC.element_to_be_clickable(video)).click()

            self.log.info("✅ Random video opened")
            time.sleep(watch_time)

        except (TimeoutException, NoSuchElementException) as e:
            raise AssertionError(f"❌ Video play failed: {e}")