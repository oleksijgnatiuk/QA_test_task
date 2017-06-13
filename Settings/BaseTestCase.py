from selenium import webdriver
from Settings.TestSettings import TestSettings
import unittest

class BaseTestsCase(unittest.TestCase):

    def setUp(self, browser='chrome'): #choosing on which browser tests would be launched, in this case it's CH
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
            self.driver.get(TestSettings.baseUrl)
            self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()