# Getting Started

To get started using selenium and the selenium example script, follow these steps:
# 1. Setup enviroment
Run the following command to clone the repo:

    git clone git@github.com:CSC-256-Group-Project-9/Group-9-Selenium-Lab.git

Run the following command to swap to the basic-scripting branch:

    git checkout basic-scripting
# 2. Activate Virtual Environment
This will create a virtual environment in the current directory which can be used to install new python modules.

    python -m venv venv

The virtual environment needs to be activated after being created.

**For PowerShell:**

If you have already enabled script execution for your system, you may skip the following step, otherwise, in an elevated terminal (administrator privileges) run the following command:

    set-executionpolicy remotesigned

After script execution is enabled, run the following command to activate the virtual environment:

    .\venv\Scripts\Activate.ps1

At this point you should see <code>(venv)</code> at the beginning of each prompt.

# 3. Install requirements.txt
To install the requirements for this script, use <code>pip</code> to install requirements from <code>requirements.txt</code>.

    pip install -r requirements.txt

# 4. Download Web Driver

<h2 style="color: red;">This step was not reuired to get selenium to work during testing</h2>

## For Chrome:
Check your [Chrome version](chrome://settings/help).

Navigate to [Chrome for Testing availability](https://googlechromelabs.github.io/chrome-for-testing/) and locate your installed version of Chrome. Visit the link labeled <code>chromedriver</code> for your platform.

Inside the downloaded zip file, locate <code>chromedriver.exe</code> and move it to the drivers directory for this repository.

# 5. Test Installation
Run the <code>test_installation.py</code> script.

    python ./test_installation.py
    
Expected Output:

    DevTools listening on ws://127.0.0.1.....
    Installation verified

# 6. Example Script
You may run the <code>example_test_script.py</code> the same way you ran the <code>test_installation.py</code> script.

    python ./example_test_script.py
