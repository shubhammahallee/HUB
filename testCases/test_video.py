import allure
import pytest

from Pages.Video import Video

@pytest.mark.usefixtures("setup")
class Test_video:

    @allure.title("Search bar pagination test")
    @allure.description("Navigates to last page via next button")
    def test_videopage(self):
        vp = Video(self.driver)
        vp.enter_age_gate()
        vp.verify_logo()
        #vp.cookies()
        vp.menu_btn()
        vp.shorts()