from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import newFileOpen
import globalVars

def project_bid_runner(driver):
    wait = WebDriverWait(driver, 15)

    def project_test_1():
        try:
            open_tab = wait.until(EC.element_to_be_clickable((By.ID, "operations-ProjectBid-get_api_ProjectBid")))
            open_tab.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-ProjectBid-get_api_ProjectBid"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))

            status_text = status_element.get_attribute('textContent')
            # Print the status for debugging
            print("Status for user details: " + status_text[0:3])
            status_num = int(status_text[0:3])
            #print(status_text)

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-ProjectBid-get_api_ProjectBid"]/div[1]/button[1]')))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/ProjectBid\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/ProjectBid\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/ProjectBid\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/ProjectBid\n")
                return 500
            else:
                print("Unexpected status code: ", status_num)
                return status_num
            
        except Exception as e:
            print(e)

    def project_test_2():
        try:
            open_tab = wait.until(EC.element_to_be_clickable((By.ID, "operations-ProjectBid-get_api_ProjectBid__id_")))
            open_tab.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-ProjectBid-get_api_ProjectBid__id_"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input')))
            text_field.send_keys(globalVars.PROJ_BID_ID)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-ProjectBid-get_api_ProjectBid__id_"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))

            status_text = status_element.get_attribute('textContent')

            # Print the status for debugging
            print("Status for user details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-ProjectBid-get_api_ProjectBid__id_"]/div[1]/button[1]')))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/ProjectBid/id\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/ProjectBid/id\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/ProjectBid/id\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/ProjectBid/id\n")
                return 500
            else:
                print("Unexpected status code: ", status_num)
                return status_num
            
        except Exception as e:
            print(e)

    project_test_1()
    project_test_2()

