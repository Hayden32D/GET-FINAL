#GETs for lookup section

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import newFileOpen
import globalVars
import time

def lookupTests(driver):

    wait = WebDriverWait(driver, 15)
    def documentTypes():
        try:
            open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-Lookup-get_api_Lookup_DocumentTypes")))
            open_tab_button.click()

            # Click the "Try it out" button
            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()
            
            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='operations-Lookup-get_api_Lookup_DocumentTypes']/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]")))

            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for user details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-Lookup-get_api_Lookup_DocumentTypes']/div[1]/button[1]")))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/Lookup/DocumentTypes\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Lookup/DocumentTypes\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Lookup/DocumentTypes\n")
                return 400
            else:
                print("Error")

        except Exception as e:
            print(e)

    def languages():
        try:
            open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-Lookup-get_api_Lookup_Languages")))
            open_tab_button.click()

            # Click the "Try it out" button
            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()
            
            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='operations-Lookup-get_api_Lookup_Languages']/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]")))

            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for user details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-Lookup-get_api_Lookup_Languages']/div/button[1]")))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/Lookup/languages\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Lookup/languages\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Lookup/languages\n")
                return 400
            else:
                print("Error")

        except Exception as e:
            print(e)

    def states():
        try:
            open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-Lookup-get_api_Lookup_states")))
            open_tab_button.click()

            # Click the "Try it out" button
            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()
            
            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='operations-Lookup-get_api_Lookup_states']/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]")))

            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for user details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-Lookup-get_api_Lookup_states']/div[1]/button[1]")))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/Lookup/states\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Lookup/states\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Lookup/states\n")
                return 400
            else:
                print("Error")

        except Exception as e:
            print(e)

    def roles():
        try:
            open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-Lookup-get_api_Lookup_roles")))
            open_tab_button.click()

            # Click the "Try it out" button
            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()
            
            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='operations-Lookup-get_api_Lookup_roles']/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]")))

            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for user details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-Lookup-get_api_Lookup_roles']/div[1]/button[1]")))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/Lookup/roles\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Lookup/roles\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Lookup/roles\n")
                return 400
            else:
                print("Error")

        except Exception as e:
            print(e)

    def getCurrentUser():
        try:
            open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-Lookup-get_api_Lookup_GetCurentUser")))
            open_tab_button.click()

            # Click the "Try it out" button
            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()
            
            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='operations-Lookup-get_api_Lookup_GetCurentUser']/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]")))

            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for user details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-Lookup-get_api_Lookup_GetCurentUser']/div[1]/button[1]")))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/Lookup/getCurrentUser\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Lookup/getCurrentUser\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Lookup/getCurrentUser\n")
                return 400
            else:
                print("Error")

        except Exception as e:
            print(e)


    documentTypes()
    languages()
    states()
    roles()
    getCurrentUser()