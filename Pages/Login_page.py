from selenium.webdriver.common.by import By

from Commons.Commonutils import CommonActions


class login_page(CommonActions):

    def __init__(self, driver):
        self.driver = driver

    usrname = (By.ID, "email")
    psword = (By.ID, "pass")
    login_btn = (By.XPATH, "//button[text()='Log In']")
    forgot_pwd = (By.LINK_TEXT, "/Forgotten password?")
    Create_acct = (By.XPATH, "//a[text()='Create New Account']")
    incorrext = (By.XPATH,"// div[text() = 'Wrong credentials']")
    incorrect_usertext =(By.XPATH,"//*[@id='email_container']//div[2]")
    incorrect_passwordtext =(By.XPATH,"//*[@id='pass']//ancestor::div[starts-with(@class , 'clearfix')]//div[2]")


    # constructor

    def username(self,username):
        self.textBoxvaluebyName(self.driver.find_element(*login_page.usrname),username)
        #return self.driver.find_element(*login_page.usrname)

    def password(self):
        return self.driver.find_element(*login_page.psword)

    def login_button(self):
        return self.driver.find_element(*login_page.login_btn)

    def forgot_password(self):
        return self.driver.find_element(*login_page.forgot_pwd)

    def incorrect_credentials(self):
        return self.driver.find_element(*login_page.incorrext)

    def incorrect_credentials_text(self):
        self.explictiwaitbyxpathforvisibilityofElement("//*[@id='email_container']//div[2]")
        return self.driver.find_element(*login_page.incorrect_usertext)

    def incorrect_password_text(self):
        self.explictiwaitbyxpathforvisibilityofElement("//*[@id='pass']//ancestor::div[starts-with(@class , 'clearfix')]//div[2]")
        return self.driver.find_element(*login_page.incorrect_passwordtext)
