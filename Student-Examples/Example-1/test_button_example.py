# Purpose: This Selenium test script tests the submit button 
#       on Formy website using different methods to find the element.
# Author: Zach Walker

# import all required frameworks
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inherit TestCase Class and create a new test class
class FormyProjectTests(unittest.TestCase):
    
    # Constant link variables for consistency
    LINK = 'https://formy-project.herokuapp.com/form'
    LINK_SUBMIT = 'https://formy-project.herokuapp.com/thanks'
    
    def setUp(self):
        """
        Initialization of webdriver
        """
        # In this example Google Chrome is being used as the web driver
        # You may change to desired browser 
        self.driver = webdriver.Chrome()

        # This allows the driver to locate and open the website/web app
        self.driver.get(self.LINK)
        

    def test_submit_class_name(self):
        """
        Test that the submit button takes you to the 'Thanks' page using by class name
        """
        # Use CSS selector to find element
        button = self.driver.find_element(By.CSS_SELECTOR, '.btn.btn-lg.btn-primary')
        button.click()

        # Wait for browser to change url
        WebDriverWait(self.driver, 10).until(EC.url_changes(self.LINK))

        # Test url has changed by using an assert method
        self.assertEqual(self.driver.current_url, 
                         self.LINK_SUBMIT, 
                         f"Expected URL: {self.LINK_SUBMIT}, but got {self.driver.current_url}")
        
    def test_submit_xPath(self):
        """
        Test that the submit button takes you to the 'Thanks' page using by XPath
        """   
        # Use xPath to find element
        button = self.driver.find_element(By.XPATH, '/html/body/div/form/div/div[8]/a')
        button.click()

        # Wait for browser to change url
        WebDriverWait(self.driver, 10).until(EC.url_changes(self.LINK))

        # Test url has changed by using an assert method
        self.assertEqual(self.driver.current_url, 
                         self.LINK_SUBMIT, 
                         f"Expected URL: {self.LINK_SUBMIT}, but got {self.driver.current_url}")
    

    # Cleanup method called after every test performed
    def tearDown(self):
        self.driver.close()

# Execute the script
if __name__ == "__main__":
    unittest.main()
