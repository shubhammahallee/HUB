import allure
import pytest
from Pages.Watch_it import Watch_it

@pytest.mark.usefixtures("setup")
class Test_Watch_it:

    @allure.title("Search bar pagination test")
    @allure.description("Navigates to last page via next button")
    def test_watch(self):
        wi = Watch_it(self.driver)

        wi.enter_age_gate()
        wi.handle_cookies()
        wi.play_video()