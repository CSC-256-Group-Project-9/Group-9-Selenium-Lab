# Purpose: This Selenium test program tests the radio buttons 
#       on Formy using different methods to find the element.
#       This test uses Firefox
# Author: Owen Cawlfield

# import all required frameworks
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

# inherit TestCase Class and create a new test class
class FormyProjectTests(unittest.TestCase):

    def setUp(self):
        """
        Initialization of webdriver
        """
        # select which web browser to use, Chrome also works
        self.driver = webdriver.Firefox()
        # The webpage to test.
        self.LINK = 'https://group-9-unofficial.vercel.app/testing'

    def test_default_selection(self):
        """
        Test if radio button 1 is not seleced by default using by name
        """
        # use the link to the webpage
        self.driver.get(self.LINK)
        # set the location of the element to a variable using the ID
        radio = self.driver.find_element(By.ID, 'javascript')
        # determine if the radio button is clicked, should return true is button is not selected
        self.assertFalse(radio.is_selected())

    def test_radio_unselected(self):
        """
        Test if radio button 2 is not selected by default using xPath
        """
        self.driver.get(self.LINK)
        # set the location of the element to a variable using XPATH
        radio2 = self.driver.find_element(By.XPATH, '//*[@id="typescript"]')
        # determine if the radio button is clicked, should return true is button is not selected
        self.assertFalse(radio2.is_selected())

    def test_radio_xPath(self):
        """
        Test radio button 3 using XPath
        """
        # use the link to the webpage
        self.driver.get(self.LINK)
        # set the location of the element to a variable using XPATH
        radio3 = self.driver.find_element(By.XPATH, '//*[@id="typescript"]')
        # click the radio button
        radio3.click()
        # determine if the radio button is clicked returns true if radio button is selected
        self.assertTrue(radio3.is_selected())

    def test_radio_css_selector(self):
        """
        Test radio button 3 using CSS Selector
        """
        # use the link to the webpage
        self.driver.get(self.LINK)
        # set the location of the element to a variable using CSS_SELECTOR
        radio2 = self.driver.find_element(By.CSS_SELECTOR, '#java[name="fav_language"][value="Java"]')
        # click the radio button
        radio2.click()
        # determine if the radio button is clicked returns true if radio button is selected
        self.assertTrue(radio2.is_selected())

    def tearDown(self):
        """
        Cleanup method called after every test performed
        """
        self.driver.close()

# execute the script
if __name__ == "__main__":
    unittest.main()
