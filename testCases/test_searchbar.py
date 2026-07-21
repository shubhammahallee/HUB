import allure
import pytest
from Pages.SearchBar import SearchBar

@pytest.mark.usefixtures("setup")
class Test_SearchBar:

    @allure.title("Search bar pagination test")
    @allure.description("Navigates to last page via next button")
    def test_bar(self):
        sb = SearchBar(self.driver)

        sb.enter_age_gate()
        sb.handle_cookie_popup()
        sb.test_last_window()
        #sb.test_diffrent_text()
        #sb.test_category()
        #sb.test_random_video()
