import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Commons.Commonutils import CommonActions


class logout_page(CommonActions):
    logout_dr = (By.XPATH,"(//div[@aria-label='Your profile'])[1]")
    logout_btn = (By.XPATH,"(//span[text()='Log Out']//parent::div//parent::div)[1]")

    def __init__(self,driver):
        self.driver = driver

    def logoutdropdown(self):

        self.explictiwaitbyxpathforclickable("(//div[@aria-label='Your profile'])[1]")
        self.ButtonClick(self.driver.find_element(*logout_page.logout_dr))
        #self.driver.find_element(*logout_page.logout_dr)
    def logoutbutton(self):
       #WebDriverWait(self.driver, 60).until(
        #    EC.element_to_be_clickable(self.driver.find_element(*logout_page.logout_btn)))
        #Baseclass.welementtobeclickable(self.driver.find_element(*logout_page.logout_btn))
        #self.explictiwaitbyxpathforclickable(self.driver.find_element(*logout_page.logout_btn))
        self.explictiwaitbyxpathforclickable("(//span[text()='Log Out']//parent::div//parent::div)[1]")
        self.ButtonClick(self.driver.find_element(*logout_page.logout_btn))
        #lgbutton = self.driver.find_element(*logout_page.logout_btn)
        #return lgbutton
