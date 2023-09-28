# Selenium Lab LLD 7.0

from web_interaction import initialize_driver, navigate_to_url
from validation import validate_page_title, is_element_present
from report_generation import initialize_report, log_result
from utilities import capture_screenshot, read_data


def main():
    # Example code provided by LLD
    driver = initialize_driver("Chrome")
    navigate_to_url("https://samplewebsite.com")

    if validate_page_title("Sample Website"):
        search_box = find_element("ID", "searchBoxId")  # find_element is not defined in LLD - William
        search_box.send_keys("Test")

        if is_element_present("ID", "resultId"):
            log_result("Search Functionality", "Pass", report)
        else:
            log_result("Search Functionality", "Fail", report)
            capture_screenshot("Search_Fail.png")
    else:
        log_result("Navigation to Sample Website", "Fail", report)

    driver.quit()


# Added for good practice - William
if __name__ == "__main__":
    main()
