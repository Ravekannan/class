import time

import pytest
from selenium.webdriver.common.by import By

from Commons.Commonutils import CommonActions
from Pages.Login_page import login_page
from Pages.Loginout_page import logout_page
from TestData.Testdatainput import Testdatainput


class Test_Facebook_Login(CommonActions):

    @pytest.mark.UAT
    def test_LaunchURL(self):
        self.driver.get("http://www.facebook.com")
        print(self.driver.title)

    @pytest.mark.UAT
    def ValidLoginandLogout(self):
        self.textBoxvaluebyName(self.driver.find_element(by=By.ID, value="email"),"kumar.sathish189@gmail.com")
        self.textBoxvaluebyName(self.driver.find_element(by=By.ID, value="pass"), "Admin@123")
        #self.driver.find_element(by=By.ID, value="email").send_keys("kumar.sathish189@gmail.com")
        #self.driver.find_element(by=By.ID, value="pass").send_keys("Admin@123")
        self.ButtonClick(self.driver.find_element(by=By.NAME, value="login"))
        time.sleep(2)
        self.explictiwaitbyxpathforclickable("(//div[@aria-label='Your profile'])[1]")
        self.driver.find_element(by=By.XPATH, value="(//div[@aria-label='Your profile'])[1]").click()
        time.sleep(2)
        self.explictiwaitbyxpathforclickable("(//span[text()='Log Out']//parent::div//parent::div)[1]")
        self.driver.find_element(by=By.XPATH, value="(//span[text()='Log Out']//parent::div//parent::div)[1]").click()

    #@pytest.mark.Sit
    def ValidLoginandLogout(self,fbloginvaliddata):
        size = len(Testdatainput.credential_excel_dic[0])
        print(size)
        value = size / 2
        print(int(value))
        for i in range(1, int(value) + 1):
            self.textBoxvaluebyName(self.driver.find_element(by=By.ID, value="email"), fbloginvaliddata["username"+str(i)])
            self.textBoxvaluebyName(self.driver.find_element(by=By.ID, value="pass"), fbloginvaliddata["password"+str(i)])
            self.ButtonClick(self.driver.find_element(by=By.NAME, value="login"))
            #time.sleep(2)
            self.explictiwaitbyxpathforclickable("(//div[@aria-label='Your profile'])[1]")
            self.driver.find_element(by=By.XPATH, value="(//div[@aria-label='Your profile'])[1]").click()
            #time.sleep(2)
            self.explictiwaitbyxpathforclickable("(//span[text()='Log Out']//parent::div//parent::div)[1]")
            self.driver.find_element(by=By.XPATH, value="(//span[text()='Log Out']//parent::div//parent::div)[1]").click()

    #@pytest.mark.Sit
    def loginDDwithexcel(self, fbloginvaliddata):

        size = len(Testdatainput.credential_excel_dic[0])
        print(size)
        value = size / 2
        print(int(value))
        for i in range(1, int(value) + 1):
            lp = login_page(self.driver)
            lp.username(fbloginvaliddata["username" + str(i)])
            #lp.password().clear()
            lp.password().send_keys(fbloginvaliddata["password" + str(i)])
            lp.login_button().click()
            lp = logout_page(self.driver)
            #self.welementtobeclickable(lp.logoutdropdown())
            lp.logoutdropdown()
            #self.welementtobeclickable(lp.logoutbutton())
            lp.logoutbutton()

    def test_loginwithinvalidcredentials(self):

            lp = login_page(self.driver)
            lp.username("2343433445EWFEWRT$#%")
            # lp.password().clear()
            lp.password().send_keys("2324323443545")
            lp.login_button().click()
            actualerromesage=lp.incorrect_credentials_text().text
            print(actualerromesage)
            if actualerromesage=="The email address or mobile number you entered isn't connected to an account. Find your account and log in.":
                print("Pass")
            else:
                print("Fail")
            assert actualerromesage=="The email address or mobile number you entered isn't connected to an account. Find your account and log in."

    def test_loginwithinvalidpassword(self):
        #self.driver.back
        #self.driver.refresh
        time.sleep(2)
        lp = login_page(self.driver)
        lp.username("kumar.sathish189@gmail.com")
        # lp.password().clear()
        lp.password().send_keys("2324323443545")
        lp.login_button().click()
        actualerromesage = lp.incorrect_password_text().text
        print(actualerromesage)
        assert actualerromesage == "The password that you've entered is incorrect. Forgotten password?"