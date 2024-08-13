from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import newFileOpen
import globalVars


def runProfile(driver):

    wait = WebDriverWait(driver, 15)


    def authorize():
        # Click the login button
        time.sleep(1)
        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.opblock-summary-control")))
        login_button.click()

        # Click the "Try it out" button
        try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
        try_it_out_button.click()

        # Enter login details
        time.sleep(1)
        text_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[class*='body-param']")))
        text_field.clear()
        text_to_write = '{"userName": "HDouglas+creator1@method-automation.com", "password": "Poohbear@32D"}'
        text_field.send_keys(text_to_write)
        #print("Text written to the text field: ", text_to_write)

        # Execute login
        execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
        execute_button.click()

        # Wait for the response
        time.sleep(.5)
        download = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.download-contents")))
        download.click()

        # Open the new file to get the key
        key = newFileOpen.openNewFile()
        #print(key)

        # Authorize with the obtained key
        authorize_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.authorize.unlocked")))
        authorize_button.click()

        time.sleep(1)
        key_input_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input")))
        key_input_field.send_keys("Bearer " + key)

        final_press_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.modal-btn.auth.authorize.button")))
        final_press_button.click()

        # Check if authorization was successful
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.authorize.locked")))

            close = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.btn.modal-btn.auth.btn-done.button")))
            close.click()

            close_open_tab = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.opblock-summary-control")))
            close_open_tab.click()
            time.sleep(2)
        except Exception as e:
            print("Authorization was not granted")
            SystemExit()

    def profileDisciplines():

        # Open the tab for the Profile disciplines API
        open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-Profile-get_api_Profile__UserID__disciplines")))
        open_tab_button.click()

        # Click the "Try it out" button
        try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
        try_it_out_button.click()

        # Enter the user ID
        text_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='operations-Profile-get_api_Profile__UserID__disciplines']/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input")))
        text_field.send_keys(globalVars.USER_ID)

        # Click the "Execute" button
        execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-Profile-get_api_Profile__UserID__disciplines']/div[2]/div/div[2]/button[1]")))
        execute_button.click()

        # Wait for the response status code
        status_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='operations-Profile-get_api_Profile__UserID__disciplines']/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]")))
        status_text = status_element.get_attribute('textContent')

        # Print the status for debugging
        print("Status for user details: " + status_text[0:3])
        status_num = int(status_text[0:3])

        # Close the API tab
        close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-Profile-get_api_Profile__UserID__disciplines']/div[1]/button[1]")))
        close_tab.click()

        # Return the status number
        if status_num == 200:
            print("API call successful (Status 200) for /api/Profile/{UserID}/disciplines\n")
            return 200
        elif status_num == 401:
            print("Unauthorized access (Status 401) for /api/Profile/{UserID}/disciplines\n")
            return 401
        elif status_num == 400:
            print("Bad request (Status 400) for /api/Profile/{UserID}/disciplines\n")
            return 400
        elif status_num == 500:
            print("Internal server error (Status 500) for /api/Profile/{id}/progress\n")
            return 500
        else:
            print("Unexpected status code: ", status_num)
            return status_num
        
    def profileProgress():

        # Open the tab for the Profile disciplines API
        open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-Profile-get_api_Profile__id__progress")))
        open_tab_button.click()

        # Click the "Try it out" button
        try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
        try_it_out_button.click()

        # Enter the user ID
        text_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='operations-Profile-get_api_Profile__id__progress']/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input")))
        text_field.send_keys(globalVars.ID)

        # Click the "Execute" button
        execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-Profile-get_api_Profile__id__progress']/div[2]/div/div[2]/button[1]")))
        execute_button.click()

        # Wait for the response status code
        status_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='operations-Profile-get_api_Profile__id__progress']/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]")))
        status_text = status_element.get_attribute('textContent')

        # Print the status for debugging
        print("Status for user details: " + status_text[0:3])
        status_num = int(status_text[0:3])

        # Close the API tab
        close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-Profile-get_api_Profile__id__progress']/div[1]/button[1]")))
        close_tab.click()

        # Return the status number
        if status_num == 200:
            print("API call successful (Status 200) for /api/Profile/{id}/progress\n")
            return 200
        elif status_num == 401:
            print("Unauthorized access (Status 401) for /api/Profile/{id}/progress\n")
            return 401
        elif status_num == 400:
            print("Bad request (Status 400) for /api/Profile/{id}/progress\n")
            return 400
        elif status_num == 500:
            print("Internal server error (Status 500) for /api/Profile/{id}/progress\n")
            return 500
        else:
            print("Unexpected status code: ", status_num)
            return status_num
        
    def profileValidation():

        # Open the tab for the Profile disciplines API
        open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-Profile-get_api_Profile__id__validation")))
        open_tab_button.click()

        # Click the "Try it out" button
        try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
        try_it_out_button.click()

        # Enter the user ID
        text_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='operations-Profile-get_api_Profile__id__validation']/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input")))
        text_field.send_keys(globalVars.ID)

        # Click the "Execute" button
        execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-Profile-get_api_Profile__id__validation']/div[2]/div/div[2]/button[1]")))
        execute_button.click()

        # Wait for the response status code
        status_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='operations-Profile-get_api_Profile__id__validation']/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]")))
        status_text = status_element.get_attribute('textContent')

        # Print the status for debugging
        print("Status for user details: " + status_text[0:3])
        status_num = int(status_text[0:3])

        # Close the API tab
        close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-Profile-get_api_Profile__id__validation']/div[1]/button[1]")))
        close_tab.click()

        # Return the status number
        if status_num == 200:
            print("API call successful (Status 200) for /api/Profile/{id}/validation\n")
            return 200
        elif status_num == 401:
            print("Unauthorized access (Status 401) for /api/Profile/{id}/validation\n")
            return 401
        elif status_num == 400:
            print("Bad request (Status 400) for /api/Profile/{id}/validation\n")
            return 400
        elif status_num == 500:
            print("Internal server error (Status 500) for /api/Profile/{id}/validation\n")
            return 500
        else:
            print("Unexpected status code: ", status_num)
            return status_num
        
    def profileID():
        # Open the tab for the Profile disciplines API
        open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-Profile-get_api_Profile__id_")))
        open_tab_button.click()

        # Click the "Try it out" button
        try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
        try_it_out_button.click()

        # Enter the user ID
        text_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='operations-Profile-get_api_Profile__id_']/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input")))
        text_field.send_keys(globalVars.ID)

        # Click the "Execute" button
        execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-Profile-get_api_Profile__id_']/div[2]/div/div[2]/button[1]")))
        execute_button.click()

        # Wait for the response status code
        status_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='operations-Profile-get_api_Profile__id_']/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]")))
        status_text = status_element.get_attribute('textContent')

        # Print the status for debugging
        print("Status for user details: " + status_text[0:3])
        status_num = int(status_text[0:3])

        # Close the API tab
        close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-Profile-get_api_Profile__id_']/div[1]/button[1]")))
        close_tab.click()

        # Return the status number
        if status_num == 200:
            print("API call successful (Status 200) for /api/Profile/{id}\n")
            return 200
        elif status_num == 401:
            print("Unauthorized access (Status 401) for /api/Profile/{id}\n")
            return 401
        elif status_num == 400:
            print("Bad request (Status 400) for /api/Profile/{id}\n")
            return 400
        elif status_num == 500:
            print("Internal server error (Status 500) for /api/Profile/{id}\n")
            return 500
        else:
            print("Unexpected status code: ", status_num)
            return status_num


    try:
        #driver.get("https://wsmanybuild.azurewebsites.net/Swagger/index.html")
        # Wait for the page to load completely
        time.sleep(2)
        # Run the profile disciplines test
        #authorize()
        profileDisciplinesNum = profileDisciplines()
        profileProgressNum = profileProgress()
        profileValidationNum = profileValidation()
        profileIDNum = profileID()

        if (profileDisciplinesNum == 200) and (profileProgressNum == 200) and (profileValidationNum == 200) and (profileIDNum == 200):
            print("All tests passed!")
        else:
            print("One or more tests failed!")

    except Exception as e:
        print(f"An error occurred: {e}")
