# This script will demonstrate the use of selenium to test a basic webapp
# This script does not handle the case where an element is not found
# This script assumes that the web app will pass all of the tests
# Author: William Henderson

from selenium_utils.web_interaction import initialize_driver, navigate_to_url
from selenium_utils.validation import validate_page_title, is_element_present
from selenium_utils.report_generation import initialize_report, log_result
from selenium_utils.utilities import capture_screenshot, read_data
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import JavascriptException
import time


# time in seconds to wait after performing an input
WAIT_TIME_SECS = 0.5
CHECK_JS = False


def wait():
    time.sleep(WAIT_TIME_SECS)


def do_test_1(driver: WebDriver):
    """
    Find the test1 form element, enter some text, and check the output to see if it matches
    """
    # String to use in the form
    test1_string = 'some string for test 1'

    # Get the form element and send the string using keyboard inputs
    form_input_elt = driver.find_element(By.CSS_SELECTOR, '.test1 input')
    form_input_elt.send_keys(test1_string)
    wait()

    # Get the output element and check it for the correct output
    form_output_elt = driver.find_element(By.CSS_SELECTOR, '.test1 label:last-of-type')

    # check the output elemnt
    if form_output_elt.text != 'Output: ' + test1_string:
        print('Test 1: Failed')
        print(f'Expected: "{"Output: " + test1_string}"')
        print(f'Actual:   "{form_output_elt.text}"')
        return
    
    if not CHECK_JS:
        print('Test 1: Success')
        return
    
    # check value of the javascript variable
    try:
        value = driver.execute_script("return name")
    except JavascriptException as err:
        print('Test 1: Failed')
        print(str(err).split('\n')[0])
        return
    
    if value != test1_string:
        print('Test 1: Failed')
        print(f'Expected: "{test1_string}"')
        print(f'Actual:   "{value}"')
        return
    
    print('Test 1: Success')


def do_test_2(driver: WebDriver):
    """
    Find the test2 button, click it a number of times, and check the counter
    """
    # number of clicks to try
    total_clicks = 5

    # find the relevant elements
    button = driver.find_element(By.CSS_SELECTOR, '.test2 button')
    counter = driver.find_element(By.CSS_SELECTOR, '.test2 p:nth-child(n + 3)')  # ":nth-child(n + 3)" will get every third element, but .find_element only returns the first match

    # click the button 
    for num_clicks in range(1, total_clicks + 1):
        button.click()
        wait()

        # get the text of the output, split the number part out, and convert to an int
        counter_value = int(counter.text.split(' ')[-1])

        if counter_value != num_clicks:
            print('Test 2: Failed')
            print(f'Expected: "Counter: {num_clicks}"')
            print(f'Actual:   "{counter.text}"')
            return
        
        if not CHECK_JS:
            continue

        # check value of the javascript variable
        try:
            value = driver.execute_script("return count")
        except JavascriptException as err:
            print('Test 2: Failed')
            print(str(err).split('\n')[0])
            return

        if value != num_clicks:
            print('Test 2: Failed')
            print(f'Expected: "{num_clicks}"')
            print(f'Actual:   "{value}"')
            return
    
    print('Test 2: Success')


def do_test_3(driver: WebDriver):
    """
    Find the test3 button, click it, and check to see if the counter from test2 reset
    """
    # find the relevant elements
    button = driver.find_element(By.CSS_SELECTOR, '.test3 button')
    counter = driver.find_element(By.CSS_SELECTOR, '.test2 p:nth-child(n + 3)')  # same element as in test 2

    button.click()
    wait()

    counter_value = int(counter.text.split(' ')[-1])

    if counter_value != 0:
        print('Test 3: Failed')
        print(f'Expected: "Counter: {0}"')
        print(f'Actual:   "{counter.text}"')
        return
    
    if not CHECK_JS:
        print('Test 3: Success')
        return
    
    # check value of the javascript variable
    try:
        value = driver.execute_script("return count")
    except JavascriptException as err:
        print('Test 3: Failed')
        print(str(err).split('\n')[0])
        return
    
    if value != 0:
        print('Test 3: Failed')
        print(f'Expected: "{0}"')
        print(f'Actual:   "{value}"')
        return
    
    print('Test 3: Success')
    

def main():
    driver = initialize_driver('Chrome')
    navigate_to_url(url='https://group-9-webapp-ts.vercel.app/', driver=driver)

    do_test_1(driver=driver)
    do_test_2(driver=driver)
    do_test_3(driver=driver)

    # block until the user is ready to exit the program
    # otherwise the window would close when driver goes out of scope
    # input('Type "quit" to quit: ')


if __name__ == "__main__":
    main()