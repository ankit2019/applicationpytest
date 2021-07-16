import pytest
from selenium import webdriver

import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


class Testaddition:
    driver = None

    @pytest.fixture()
    def Setup(self):
        Testaddition.driver = webdriver.Chrome(
            executable_path="D:\\Ankit\\eclipse\\CalcualtorWebApplication\\Driver\\chromedriver.exe")
        Testaddition.driver.get("file:///D:/Ankit/project/CalcualtorWebApplication/src/main/webapp/Calculator.html")

    def testAdditionwithpositiveValues(self, Setup):
        ButtonEight = Testaddition.driver.find_element_by_css_selector("input[value='9']")
        Buttonplus = Testaddition.driver.find_element_by_css_selector("input[value='+']")
        ButtonFour = Testaddition.driver.find_element_by_css_selector("input[value='4']")
        ButtonEqual = Testaddition.driver.find_element_by_css_selector("input[value='=']")
        ButtonEdit = Testaddition.driver.find_element_by_id("result")

        ButtonEight.click()
        Buttonplus.click()
        ButtonFour.click()
        ButtonEqual.click()

        ActualResult = ButtonEdit.get_attribute("value")
        assert ActualResult== "13", "Addition error"
