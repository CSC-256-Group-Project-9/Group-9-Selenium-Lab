# Group 9 Selenium Lab

# Getting Started

To get started using selenium and the selenium example script, follow these steps:
# 0. Setup enviroment
- Insert steps to enable scripts on powershell
- Run the following script to clone the repo:
    -     $ git clone git@github.com:CSC-256-Group-Project-9/Group-9-Selenium-Lab.git
- Run the following script to swap to the basic-scripting branch
    -     $ git checkout basic-scripting
# 1. Activate Virtual Environment
This will create a virtual environment in the current directory which can be used to install new python modules.

    $ python -m venv venv

The virtual environment needs to be activated after being created.

**For PowerShell:**

    $ .\venv\Scripts\Activate.ps1

At this point you should see <code>(venv)</code> at the beginning of each prompt.

# 2. Install requirements.txt
To install the requirements for this script, use <code>pip</code> to install requirements from <code>requirements.txt</code>.

    $ pip install -r requirements.txt

# 3. Download Web Driver

<h2 style="color: red;">This step was not reuired to get selenium to work during testing</h2>

## For Chrome:
Check your [Chrome version](chrome://settings/help).

Navigate to [Chrome for Testing availability](https://googlechromelabs.github.io/chrome-for-testing/) and locate your installed version of Chrome. Visit the link labeled <code>chromedriver</code> for your platform.

Inside the downloaded zip file, locate <code>chromedriver.exe</code> and move it to the drivers directory for this repository.

# 4. Test Installation
Run the <code>test_installation.py</code> script.

    $ python ./test_installation.py
    
    DevTools listening on ws://127.0.0.1.....
    Installation verified

# 5. Example Script
You may run the <code>example_test_script.py</code> the same way you ran the <code>test_installation.py</code> script.

    $ python ./example_test_script.py
