import allure
import pytest
from Pages.HomePage import HomePage
from Utilities.ReadConfig import ReadConfig 

@pytest.mark.skip
@pytest.mark.usefixtures("setup")
class Test_homepage:

    @allure.title("Search bar pagination test")
    @allure.description("Navigates to last page via next button") 
    def test_homepage(self):
        hp = HomePage(self.driver)

        hp.enter_age_gate()
        hp.handle_cookies()
        hp.verify_page_loaded()
        hp.search()
        hp.go_to_next_page()
        hp.play_random_video()

