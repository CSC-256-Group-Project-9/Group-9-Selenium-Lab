from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def main():
    #test1()
    #test2()
    test3()
    #test4()

def test1():
    """ Testing Textbox"""
    input_data = "Nathaniel"

    """ Creates the driver for the chrome browser """
    driver = webdriver.Chrome()

    """ Gets the formy webpage link to open site"""
    driver.get("https://formy-project.herokuapp.com/keypress")
    
    """ Set the initalization of the variable element_text_box to  equal the webpage element by the ID of name """
    element_text_box = driver.find_element(By.ID,"name")

    """ Clicked the textbox and then input data into the string varibale input_data which is set to Nathaniel """
    
    element_text_box.click()
    element_text_box.send_keys(input_data)
    time.sleep(0.5)

    """ Initalizing the text data of the text box equak to a variable"""
    element_text_box_text1 = driver.find_element(By.ID,"name").text
    element_text_box_text1 = input_data
    time.sleep(0.5)

    """ Created a variable that is initalized to the webpage element with the ID of button and clicked it just for example in run time """
    element_button1 = driver.find_element(By.ID,"button")
    element_button1.click()
    
    """ Checks if if the text box input data matchs its data the text box is sent by the keyboard"""
    if element_text_box_text1 !=  input_data:
        print("test 1 faild")
        print(f'Expected result: "{"OutPut: " + input_data}"')
        print(f'Actual: "{element_text_box_text1}"')

    if element_text_box_text1 == input_data:
        print("Test 1 Success")
    

    time.sleep(4)
    driver.close

def test2():
    """ Testing Drop Down Arrows"""
    
    """ Creates the driver for the chrome browser """
    driver = webdriver.Chrome()

    """ Gets the formy webpage link to open site"""
    driver.get("https://formy-project.herokuapp.com/autocomplete")

    """ get the element of Formy website """
    autocomplete_address = driver.find_element(By.ID,"autocomplete")
    autocomplete_address.click()
    
    """ creates data to input into the element """
    autocomplete_data = "1110, autumn springs dr"
    
    """ sets autocomplete_data as text in element's text box """
    autocomplete_address.send_keys(autocomplete_data)
   
    """ actual text data of element is set to the same as words in text box"""
    autocomplete_text = driver.find_element(By.ID,"autocomplete").text
    autocomplete_text = autocomplete_data

    """ test if autocomplete text box words are the same as actual text data if not equal it fail other wise it passes"""
    if autocomplete_text != autocomplete_data:
        print(f"Test 2 Failed!")
        print(f'Expected result: "{" OutPut: " + autocomplete_data}"')
        print(f'Actual Result: "{autocomplete_address.text}"' )
    
    if autocomplete_text == "1110, autumn springs dr":
        print(f'Test 2 Successful')


    time.sleep(4)
    driver.close
    
def test3():
   """ Creates the driver for the chrome browser """
   driver = webdriver.Chrome()

   """ Gets the formy webpage link to open site"""
   driver.get("https://formy-project.herokuapp.com/radiobutton")

   time.sleep(1)
   radio_button_2 = driver.find_element(By.XPATH,"/html/body/div/div[2]/input")
   radio_button_2.click()
   time.sleep(1)

   radio_button_1 = driver.find_element(By.ID,"radio-button-1")
   radio_button_1.click()
   time.sleep(1)

   radio_button_3 = driver.find_element(By.XPATH,"/html/body/div/div[3]/input") 
   radio_button_3.click()

   if radio_button_1 == driver.find_element(By.ID,"radio-button-1") and (radio_button_2 == driver.find_element(By.XPATH,"/html/body/div/div[2]/input") ):
        print("test 3 successful")
   else:
       print('test failed')

   time.sleep(4)
   driver.close

def test4():
    
    """ Creates the driver for the chrome browser """
    driver = webdriver.Chrome()

    """ Gets the formy webpage link to open site"""
    driver.get("https://formy-project.herokuapp.com/checkbox")

    check_box1 = driver.find_element(By.ID,"checkbox-1")
    check_box1.click()
    time.sleep(1)

    check_box2 = driver.find_element(By.ID,"checkbox-2")
    check_box2.click()
    time.sleep(1)

    check_box3 = driver.find_element(By.ID,"checkbox-3")
    check_box3.click()
    time.sleep(1)

    if  check_box1 == driver.find_element(By.ID,"checkbox-1") and check_box2 == driver.find_element(By.ID,"checkbox-2") and check_box3 == driver.find_element(By.ID,"checkbox-3"):

        print("test 4 successful")
    
    else:
        print("test 4 failed")

    time.sleep(4)
    driver.close
if __name__ == "__main__":
    main()
