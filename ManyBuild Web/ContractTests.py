from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import newFileOpen
import globalVars

def contract_tests_runner(driver):
    wait = WebDriverWait(driver, 15)

    def contractID():
        try:
            open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-Contract-get_api_Contract_get__contractid_")))
            open_tab_button.click()

            # Click the "Try it out" button
            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            # Enter the new order ID
            new_order_ID = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Contract-get_api_Contract_get__contractid_"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input')))
            new_order_ID.send_keys(globalVars.CONTRACT_ID)

            # Click the "Execute" button
            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()
            
            # Check the response
            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Contract-get_api_Contract_get__contractid_"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))

            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for user details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Contract-get_api_Contract_get__contractid_"]/div[1]/button[1]')))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/Contract/get/{contract_id}\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Contract/get/{contract_id}\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Contract/get/{contract_id}\n")
                return 400
            elif status_num == 500:
                print("Bad request (Status 500) for /api/Contract/get/{contract_id}\n")
                return 500
            else:
                print("Error")


        except Exception as e:
            print(e)

    def contract_html():
        try:
            open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-Contract-get_api_Contract_get__contractid__html")))
            open_tab_button.click()

            # Click the "Try it out" button
            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            # Enter the contract ID
            new_order_ID = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Contract-get_api_Contract_get__contractid__html"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input')))
            new_order_ID.send_keys(globalVars.CONTRACT_ID)

            # Click the "Execute" button
            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Contract-get_api_Contract_get__contractid__html"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))
            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for user details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Contract-get_api_Contract_get__contractid__html"]/div[1]/button[1]')))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/Contract/get/{contract_id}/html\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Contract/get/{contract_id}/html\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Contract/get/{contract_id}/html\n")
                return 400
            elif status_num == 500:
                print("Bad request (Status 500) for /api/Contract/get/{contract_id}/html\n")
                return 500
            else:
                print("Error")

        except Exception as e:
            print(e)

    contractID()
    contract_html()