from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import newFileOpen
import globalVars

def change_order_runner(driver):
    wait = WebDriverWait(driver, 15)

    def change_orderID():
        try:
            open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-ChangeOrder-get_api_ChangeOrder__ID_")))
            open_tab_button.click()

            # Click the "Try it out" button
            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            # Enter the new order ID
            new_order_ID = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-ChangeOrder-get_api_ChangeOrder__ID_"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input')))
            new_order_ID.send_keys(globalVars.ORDER_ID)

            # Click the "Execute" button
            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()
            
            # Check the response
            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-ChangeOrder-get_api_ChangeOrder__ID_"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))

            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for user details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-ChangeOrder-get_api_ChangeOrder__ID_"]/div[1]/button[1]')))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/ChangeOrder/{ID}\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/ChangeOrder/{ID}\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/ChangeOrder/{ID}\n")
                return 400
            elif status_num == 500:
                print("Bad request (Status 500) for /api/ChangeOrder/{ID}\n")
                return 500
            else:
                print("Error")

        except Exception as e:
            print(e)

    def change_order_id_jobID():
        try:
            open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-ChangeOrder-get_api_ChangeOrder_User__UserID__Job__JobID_")))
            open_tab_button.click()

            # Click the "Try it out" button
            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-ChangeOrder-get_api_ChangeOrder_User__UserID__Job__JobID_"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr[1]/td[2]/input')))
            text_field2.send_keys(globalVars.USER_ID)

            text_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-ChangeOrder-get_api_ChangeOrder_User__UserID__Job__JobID_"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr[2]/td[2]/input')))
            text_field.send_keys(globalVars.JOB_ID)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-ChangeOrder-get_api_ChangeOrder_User__UserID__Job__JobID_"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))

            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for user details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-ChangeOrder-get_api_ChangeOrder_User__UserID__Job__JobID_"]/div[1]/button[1]')))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/ChangeOrder/User/{UserID}/Job/{jobID}\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/ChangeOrder/User/{UserID}/Job/{jobID}\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/User/ChangeOrder/{UserID}/Job/{jobID}\n")
                return 400
            elif status_num == 500:
                print("Bad request (Status 500) for /api/User/ChangeOrder/{UserID}/Job/{jobID}\n")
                return 500
            else:
                print("Error")

        except Exception as e:
            print(e)

    change_orderID()
    change_order_id_jobID()
            
