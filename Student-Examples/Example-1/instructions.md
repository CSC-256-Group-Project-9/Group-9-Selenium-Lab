# Getting Started

<hr>

**DEV NOTE:** This document contains instructions for running the provided <code>example_test_script.py</code>. This document is not to be delivered to students, but rather, to serve as a reference for documenters.

<hr>

To get started using selenium and the selenium example script, follow these steps:

# 1. Setup Environment

If you have not done so already, follow the environment setup instructions at [Group-9-Environment-Setup](https://github.com/CSC-256-Group-Project-9/Group-9-Environment-Setup/blob/main/For-Students/getting-started.md). Otherwise, activate the virtual environment by following the steps at [Pre-Lab-Instructions](https://github.com/CSC-256-Group-Project-9/Group-9-Environment-Setup/blob/main/pre-lab-instructions-template.md).

Create a new sub-folder for this lab if you have not done so already

**Example:** <code>C:\users\your_username\Documents\CSC-256-Labs\selenium_lab</code>

    cd selenium_lab

# 2. Clone the Repository

Run the following command to clone the repo:

    git clone git@github.com:CSC-256-Group-Project-9/Group-9-Selenium-Lab.git

Navigate to the new folder:

    cd Group-9-Selenium-Lab

# 3. Install requirements.txt

Navigate to the <code>Student-Examples/Example-1</code> folder.

    cd Student-Examples/Example-1

To install the requirements for this script, use <code>pip</code> to install requirements from <code>requirements.txt</code>.

    pip install -r requirements.txt

**NOTE** If you run into issues, you may have to use the command: <code>python -m pip install -r requirements.txt</code> instead.

# 4. Test Installation

Run the <code>test_installation.py</code> script.

    python ./test_installation.py
    
Expected Output:

    DevTools listening on ws://127.0.0.1.....
    Installation verified

# 6. Example Script

You may run the <code>example_test_script.py</code> the same way you ran the <code>test_installation.py</code> script.

    python ./example_test_script.py
