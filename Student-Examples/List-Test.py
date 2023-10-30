# Purpose: This Selenium test program tests "test 5" list and determines if it is functional
# Author: David Smedberg

# import all required packages
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import warnings

# Initializes a class that will run these tests
class WebAppTests(unittest.TestCase):

    def setUp(self):
        """
        Initialization of the webdriver
        """
        # These options just make it so it's not throwing a certificate error every test as well as unclosed errors. (since it isn't an official website), they are irrelevant to the actual test
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # Initializes the webdriver and gets the link (with the given "ignore certificate" options)
        self.driver = webdriver.Chrome(options=options)
        self.link = "https://group-9-webapp-official.vercel.app/testing"

    def test_scenario1(self):
        """
        Test the input box, then click the button, and verify the item list is similar
        """
        # Gets the webdriver and opens it up (chrome)
        self.driver.get(self.link)

        # Gathers elements from test 5
        input_box = self.driver.find_element(By.ID, "test5-input")
        button = self.driver.find_element(By.ID, "test5-button")
        item_list = self.driver.find_element(By.ID, "list-contents")

        # Clicks the input field
        input_box.click()

        # Types in one object, finds the click button right under it, and clicks it
        object1 = "Ham"
        input_box.send_keys("Ham")
        button.click()

        # Checks to see if the list contains the typed item
        assert item_list.text == object1

    def test_scenario2(self):
        """
        Test again the input box, then click the button, and verify the item list is similar
        """
        # Gets the webdriver and opens it up (chrome)
        self.driver.get(self.link)

        # Gathers elements from test 5
        input_box = self.driver.find_element(By.ID, "test5-input")
        button = self.driver.find_element(By.ID, "test5-button")
        item_list = self.driver.find_element(By.ID, "list-contents")

        # Clicks the input field
        input_box.click()

        # Types in one object, finds the click button right under it, and clicks it
        object2 = "Eggs"
        input_box.send_keys("Eggs")
        button.click()

        # Checks to see if the list contains the typed item
        assert item_list.text == object2

    def test_scenario3(self):
        """
        Test a final time the input box, then click the button, and verify the item list is similar
        """
        # Gets the webdriver and opens it up (chrome)
        self.driver.get(self.link)

        # Gathers elements from test 5
        input_box = self.driver.find_element(By.ID, "test5-input")
        button = self.driver.find_element(By.ID, "test5-button")
        item_list = self.driver.find_element(By.ID, "list-contents")

        # Clicks the input field
        input_box.click()

        # Types in one object, finds the click button right under it, and clicks it
        object3 = "Ground Beef"
        input_box.send_keys("Ground Beef")
        button.click()

        # Checks to see if the list contains the typed item
        assert item_list.text == object3

    def tearDown(self):
        """
        Closing method that cleans up after every test performed
        """
        self.driver.close()


# Runs the test
if __name__ == "__main__":
    unittest.main()
