# This script demonstrates the basics of Selenium using unittest
# This script will test basic functions of Group-9-Webapp
# Author: Zach Walker

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class StudentTestExamples(unittest.TestCase):

    def setUp(self):
        """
        Initialization of webdriver
        """
        self.driver = webdriver.Chrome()
        self.url = 'https://group-9-webapp-ts.vercel.app/'
        self.WAIT_TIME = 0.5  # Increase time to see the test in action!
        self.driver.get(self.url)
        
    def test_input_field(self):
        """
        Find the test1 form element, enter some text, and check the output to see if it matches
        """
        # String to input into text field
        test_string = 'Input field test string'

        # Input test string into text input field and wait for it to reflect
        input_element = self.driver.find_element(By.CSS_SELECTOR, '.test1 input')
        input_element.send_keys(test_string)
        time.sleep(self.WAIT_TIME)

        # Get the output element and assign the text to a variable
        output_element = self.driver.find_element(By.CSS_SELECTOR, '.test1 label:last-of-type')
        output_string = output_element.text

        # Verify expected output using assert
        expected_output = 'Output: ' + test_string
        self.assertEqual(output_string, expected_output, 
                         f'Expected output: {expected_output} but got {output_string}')
        
    def test_counter_button(self):
        """
        Find the test2 button, click it a number of times, and check the counter
        """
        # Number of clicks to try
        total_clicks = 5

        # Find the 'Click Me' button element
        button = self.driver.find_element(By.CSS_SELECTOR, '.test2 button')

        # Click the 'Click Me' button multiple times by using a for loop
        for num_clicks in range(0, total_clicks):
            button.click()
            time.sleep(self.WAIT_TIME)

        # Find counter element and get displayed amount
        counter_element = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/p[3]')
        output_string = counter_element.text

        # Verify expected output using assert method
        expected_output = "Counter: " + str(total_clicks)
        self.assertEqual(output_string, expected_output, 
                         f'Expected output: {expected_output} but got {output_string}')
        
    def test_counter_reset(self):
        """
        Find the test3 button, click it, and check to see if the counter from test2 reset
        """
        # Find the 'Click Me' button element in Test 2 and click it once
        button_test2 = self.driver.find_element(By.CSS_SELECTOR, '.test2 button')
        button_test2.click()
        time.sleep(self.WAIT_TIME)

        # Find the 'Click Me' button element in Test 3 and click it once
        button_test3 = self.driver.find_element(By.CSS_SELECTOR, '.test3 button')
        button_test3.click()
        time.sleep(self.WAIT_TIME)

        # Find counter element and get displayed amount
        counter_element = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/p[3]')
        output_string = counter_element.text

        # Verify expected output using assert method
        expected_output = "Counter: 0"
        self.assertEqual(output_string, expected_output, 
                         f'Expected output: {expected_output} but got {output_string}')

    # Cleanup method called after every test performed
    def tearDown(self):
        self.driver.quit()

# execute the script
if __name__ == "__main__":
    unittest.main()