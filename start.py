# System imports
import os
import sys

# Pages
from webpages.Login.Login import LoginPage
from webpages.UserForm.UserForm import UserForm

# Logger
import Config
import logging

log = logging.getLogger(__name__)

def main():
    try:
            # Check if the user provided a file path as an argument
        if len(sys.argv) != 2:
            print("Usage: python start.py <file_path>")
            return
        
        # Get the file path from the command-line argument
        file_path = sys.argv[1]

        # Check if the file exists
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            return
        else:
            # Login
            login = LoginPage(file_path)
            login.performLogin()
            
            # Open User form page and fill data
            userForm = UserForm(file_path)
            userForm.performAction()
    except Exception as e:
        log.error(e)

if __name__ == "__main__":
    # init_logger()
    main()