# Selenium Lab LLD 7.0

# Example code provided by LLD
driver = initialize_driver("Chrome")
navigate_to_url("https://samplewebsite.com")

if validate_page_title("Sample Website"):
    search_box = find_element("ID", "searchBoxId")
    search_box.send_keys("Test")

    if validate_element_presence("ID", "resultId"):
        log_result("Search Functionality", "Pass", report)
    else:
        log_result("Search Functionality", "Fail", report)
        capture_screenshot("Search_Fail.png")
else:
    log_result("Navigation to Sample Website", "Fail", report)

driver.quit()