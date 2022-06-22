import pytest


@pytest.mark.usefixtures("BrowserLaunch")
class Test_Launch():

    def test_LaunchApplication(self):
        self.driver.get("https://www.facebook.com")
