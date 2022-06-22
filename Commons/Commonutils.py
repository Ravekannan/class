from datetime import datetime
from time import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, glob

@pytest.mark.usefixtures("BrowserLaunch")
class CommonActions:

    screenshotpath="C:\\Users\\sathishkumar\\PycharmProjects\\SeleniumFramework\\Screenshot\\"
    def explictiwaitbyName(self,nameAttribute):
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.NAME, nameAttribute)))
    def explictiwaitbyXpath(self,xpathAttribute):
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.Xpath, xpathAttribute)))
    def explictiwaitbyNameforclickable(self,nameAttribute):
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.NAME, nameAttribute)))

    def explictiwaitbyxpathforclickable(self, xpathAttribute):
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, xpathAttribute)))

    def explictiwaitbyxpathforvisibilityofElement(self, xpathAttribute):
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH, xpathAttribute)))

    def textBoxvaluebyName(self,TextboxElement,TexttobeEnter):
        TextboxElement.clear()
        TextboxElement.send_keys(TexttobeEnter)

    def ButtonClick(self,TextboxElement):
        TextboxElement.click()

    def screenshot(self,filename):
        self.driver.save_screenshot(
            self.screenshotpath+filename+".png")

    def datetime(self):
        milliseconds = int(time() * 1000)
        return milliseconds

    def removefileinFolder(self):
        dir = self.screenshotpath
        for file in os.scandir(dir):
            os.remove(file.path)

    def DropdownSelectbyIndex(self, DropdownElement,indexposition):
        daydropwn = Select(DropdownElement)
        daydropwn.select_by_index(indexposition)

    def DropdownSelectbyValue(self, DropdownElement, valuetobeselected):

        monthdropwn = Select(DropdownElement)
        monthdropwn.select_by_value(valuetobeselected)

    def DropdownSelectbyVisibleText(self, DropdownElement, valuetobeselected):

        yeardropwn = Select(DropdownElement)
        yeardropwn.select_by_visible_text(valuetobeselected)

    def GenderSelection(self,Genderwebelement):
        Genderwebelement.click()

    def welementtobeclickable(self, elementvalue):
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(elementvalue))

    def welementtobevisible(self, elementvalue):
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located(elementvalue))
