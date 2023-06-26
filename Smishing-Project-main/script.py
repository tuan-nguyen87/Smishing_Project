import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the driver object
driver = webdriver.Chrome()

# Navigate to the website
driver.get('https://www.facebook.com')

# Find the email and password input fields using their ID
input_email = driver.find_element_by_id('email')
input_pass = driver.find_element_by_id('pass')

# Clear the fields and enter your email and password
input_email.clear()
input_email.send_keys('karrotsh@hotmail.com')
input_pass.clear()
input_pass.send_keys('Kirby1995!')

# Submit the login form
input_pass.submit()