# Purpose: This Selenium test script tests the input fields 
#       on Formy using different methods to find the element.
# Author: Zach Walker

# import all required frameworks
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

# inherit TestCase Class and create a new test class
class FormyProjectTests(unittest.TestCase):

    # Create website url variable
    URL = 'https://formy-project.herokuapp.com/form'

    def setUp(self):
        """
        Initialization of webdriver
        """
        # In this example Google Chrome is being used as the web driver
        # You may change to desired browser 
        self.driver = webdriver.Chrome()
        # This allows the driver to locate and open the website/web app
        self.driver.get(self.URL)

    def test_first_name_input(self):
        """
        Test input field first name using XPath
        """      
        # Find element and send input string
        first_name = self.driver.find_element(By.XPATH, '//*[@id="first-name"]')
        first_name.send_keys('John')

        # Get attribute and test if equal to input value
        elem_value = first_name.get_attribute('value')
        self.assertEqual(elem_value, 'John', f"Expected input value to be 'John', but got '{elem_value}'")

    def test_last_name_input(self):
        """
        Test input field last name using CSS Selector
        """  
        # Find element and send input string
        last_name = self.driver.find_element(By.CSS_SELECTOR, 'input[id="last-name"]')
        last_name.send_keys('Doe')

        # Get attribute and test if equal to input value
        elem_value = last_name.get_attribute('value')
        self.assertEqual(elem_value, 'Doe', f"Expected input value to be 'Doe', but got '{elem_value}'")
    
    def test_job_title_input(self):
        """
        Test input field job title using ID
        """
        # Find element and send input string
        job_title = self.driver.find_element(By.ID, 'job-title')
        job_title.send_keys('Software Engineer')

        # Get attribute and test if equal to input value
        elem_value = job_title.get_attribute('value')
        self.assertEqual(elem_value, 'Software Engineer', f"Expected input value to be 'Software Engineer', but got '{elem_value}'")

    def tearDown(self):
        """
        Cleanup method called after every test performed
        """
        self.driver.quit()

# execute the script
if __name__ == "__main__":
    unittest.main()
