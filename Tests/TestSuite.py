from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from Settings.BaseTestCase import BaseTestsCase
from Elements.MainPageElements import MainPageElements
import re
import pytest
from time import sleep


class TestSuite(BaseTestsCase):

    @pytest.fixture() #pytest tag to launch the test suite using pytest lib

    def test_checkMainPage(self):
        self.assertEqual("Welcome to Croove!", self.driver.find_element_by_tag_name("h1").text)

    def test_checkInfoBtn(self):
        MainPageElements.clickInfoBtn(self)
        element_present = expected_conditions.presence_of_element_located((By.TAG_NAME, 'h2'))
        WebDriverWait(self.driver, 10).until(element_present) #active waiting implemented
        self.assertEqual("challenge instructions", self.driver.find_element_by_tag_name("h2").text)

    def test_checkResultsPage(self):
        MainPageElements.clickSeeNumberBtn(self)
        self.assertEqual("Random Number Generator!", self.driver.find_element_by_tag_name("h1").text)

    def test_checkResultsPageToMain(self):
        MainPageElements.clickSeeNumberBtn(self)
        self.assertEqual("Random Number Generator!", self.driver.find_element_by_tag_name("h1").text)
        MainPageElements.clickBackToMainMenu(self)
        self.assertEqual("Welcome to Croove!", self.driver.find_element_by_tag_name("h1").text)

    def test_checkGeneratedNumber(self):
        scope = list(range(100))
        MainPageElements.clickSeeNumberBtn(self)
        notice_msg = self.driver.find_element_by_class_name("result").text
        generated_number = int(re.search(r'\d+', notice_msg).group())
        if generated_number in scope:
            print("Generated number is within the range and it is {0}".format(generated_number))
        else:
            print("Generated number overreaches the range and it is {0}".format(generated_number))
            raise

    def test_twoNumbers(self):
        scope = list(range(100))
        MainPageElements.clickSeeNumberBtn(self)
        first_msg = self.driver.find_element_by_class_name("result").text
        first_number = int(re.search(r'\d+', first_msg).group())
        MainPageElements.clickAnotherNumberBtn(self)
        sleep(1) #static sleep in order to catch the second integer
        second_msg = self.driver.find_element_by_class_name("result").text
        second_number = int(re.search(r'\d+', second_msg).group())
        if first_number in scope and second_number in scope:
            print("Both numbers are within the scope")
        elif first_number == second_number:
            print("Both numbers are the same")
        else:
            print("One or both numbers overreach the scope")
            raise