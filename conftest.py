import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from TestData.Testdatainput import Testdatainput


@pytest.fixture(scope="class")
def BrowserLaunch(request):
    web = webdriver.ChromeOptions()
    web.add_argument("--start-maximized")
    web.add_argument("--incognito")
    web.add_argument("--disable-notifications")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture(params=Testdatainput.credential_excel_dic)
def fbloginvaliddata(request):
    return request.param

@pytest.fixture(params=Testdatainput.credential_excel_dic)
def fbloginvaliddata(request):
    return request.param