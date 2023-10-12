from selenium import webdriver

# Initialize a global driver
driver = None

# Function to initialize the driver (you can customize this based on your needs)
def initialize_driver():
    global driver
    driver = webdriver.Chrome()  # Replace with your driver path
    driver.maximize_window()

# Automatically initialize the driver when this module is imported
initialize_driver()