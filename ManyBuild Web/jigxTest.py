import newFileOpen
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def runJigTest(driver):

    wait = WebDriverWait(driver, 15)

    def jigxForm():
        # Open the tab for the Profile disciplines API
        open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-Jigx-get_api_Jigx_Form")))
        open_tab_button.click()

        # Click the "Try it out" button
        try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
        try_it_out_button.click()

        # Click the "Execute" button
        execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-Jigx-get_api_Jigx_Form']/div[2]/div/div[2]/button[1]")))
        execute_button.click()

        # Wait for the response status code
        status_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='operations-Jigx-get_api_Jigx_Form']/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]")))
        status_text = status_element.get_attribute('textContent')

        # Print the status for debugging
        print("Status for user details: " + status_text[0:3])
        status_num = int(status_text[0:3])

        # Close the API tab
        close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-Jigx-get_api_Jigx_Form']/div[1]/button[1]")))
        close_tab.click()

        # Return the status number
        if status_num == 200:
            print("API call successful (Status 200) for /api/Jigx/Form\n")
            return 200
        elif status_num == 401:
            print("Unauthorized access (Status 401) for /api/Jigx/Form\n")
            return 401
        elif status_num == 400:
            print("Bad request (Status 400) for /api/Jigx/Form\n")
            return 400
        elif status_num == 500:
            print("Internal server error (Status 500) for /api/Jigx/Form\n")
            return 500
        else:
            print("Unexpected status code: ", status_num)
            return status_num

    try:
        # Run the profile disciplines test
        jigxFormNum = jigxForm()

        if jigxFormNum == 200: # TO-DO
            print("All tests passed!")
        else:
            print("One or more tests failed!")

    except Exception as e:
        print(f"An error occurred: {e}")