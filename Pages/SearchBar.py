import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from Pages.BasePage import BasePage
import time
import random


class SearchBar(BasePage):
    search_bar = (By.ID, "searchInput")
    NEXT_PAGE_BTN = (By.XPATH, "//li[@class='page_next omega']//a[@class='orangeButton']")
    category_btn = (By.XPATH, "//span[@class='arrowMenu'][normalize-space()='Kategorien']")
    select_category = (By.XPATH, "//div[contains(@class,'video-category-page')]//div[2]//div[2]//ul[1]//li[5]//div[1]//div[1]//a[1]//div[1]")
    select_one = (By.XPATH, "//li[80]//div[1]//div[1]//a[1]//div[1]")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 40)

    def test_diffrent_text(self):
        text = self.wait.until(EC.visibility_of_element_located(self.search_bar))
        time.sleep(2)
        text.click()
        text.send_keys("pink")
        time.sleep(2)
        text.clear()
        text.send_keys("milf")
        time.sleep(2)
        text.clear()
        text.send_keys("stepmom")
        time.sleep(2)
        text.clear()
        text.send_keys("stepsis")
        time.sleep(2)
        text.clear()
        text.send_keys("teen")
        time.sleep(2)
        text.clear()
        text.send_keys("virgin")
        time.sleep(2)
        text.clear()
        self.driver.refresh()

    def test_last_window(self):
        for i in range(454):
            try:
                next_btn = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.NEXT_PAGE_BTN)
                )
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});", next_btn
                )
                time.sleep(0.5)
                self.driver.execute_script("arguments[0].click();", next_btn)
                self.log.info(f"✅ Page {i + 1} clicked")
            except (TimeoutException, NoSuchElementException):
                self.log.info(f"⚠️ Next button not found at page {i + 1}, stopping.")
                break

        self.driver.save_screenshot("screenshots/Congo_landed_successfully_on_last_page.png")

    def test_category(self):
        self.wait.until(EC.element_to_be_clickable(self.category_btn)).click()
        self.wait.until(EC.visibility_of_element_located(self.select_category))
        element = self.driver.find_element(*self.select_category)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)
        self.log.info(self.select_category)

    def test_random_video(self):
        try:
            videos = self.wait.until(
                EC.presence_of_all_elements_located((By.XPATH, "//a[@title]"))
            )
            self.log.info(f"Total videos found: {len(videos)}")

            if videos:
                chosen = random.choice(videos)
                self.driver.execute_script("arguments[0].click();", chosen)
                self.driver.fullscreen_window()
                self.log.info("✅ Video clicked successfully")
            else:
                self.log.info("❌ No videos found")

        except (TimeoutException, NoSuchElementException) as e:
            self.log.info(f"❌ Error: {e}")

        time.sleep(60)
        self.driver.save_screenshot("screenshots/Video_played.png")