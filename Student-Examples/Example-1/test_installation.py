# This script will verifies the local installation of selenium
# Author: William Henderson

from selenium_utils.web_interaction import initialize_driver


def main():
    try:
        driver = initialize_driver('Chrome')
        print('Installation verified')
    except ValueError as err:
        print(f'Invalid driver type: {err}')
    

if __name__ == "__main__":
    main()