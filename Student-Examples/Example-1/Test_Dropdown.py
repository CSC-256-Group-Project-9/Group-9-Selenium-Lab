# Purpose: This Selenium test program tests the functionality
#       of Web app using different methods to find the element.
# Author: Owen Cawlfield

# import all required frameworks
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


# Inherit TestCase Class and create a new test class
class SampleWebAppTests(unittest.TestCase):
    # Constant link variables for consistency
    def setUp(self):
        """
        Initialization of webdriver
        """
        self.driver = webdriver.Chrome()
        self.url = 'https://formy-project.herokuapp.com/form'

    def test_dropdown_selector(self):
        """
        test the functionality of a dropdown menu
        """
        self.driver.get(self.url)

        # makes a list of option tags
        dropdown = self.driver.find_elements(by=By.TAG_NAME, value="Option")

        # print the number of elements in the list of the dropdown box
        print(f'The number of elements in the dropdown box are: {len(dropdown)}')

        # prints all the items in the dropdown box
        for item in dropdown:
            print(item.text)

    # cleanup method called after every test performed
    def tearDown(self):
        self.driver.close()


# execute the script
if __name__ == "__main__":
    unittest.main()

