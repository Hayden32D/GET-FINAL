#GETs for Health Check

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import newFileOpen
import globalVars
import time

def healthTestRun(driver):
    #health GETs

    wait = WebDriverWait(driver, 20)

    def contactList():
        try:
            open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-HealthCheck-Fortis_Contact_Lists")))
            open_tab_button.click()

            # Click the "Try it out" button
            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-HealthCheck-Fortis_Contact_Lists"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))

            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for user details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-HealthCheck-Fortis_Contact_Lists"]/div[1]/button[1]')))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/Health/ContactList\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Health/ContactList\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Health/ContactList\n")
                return 400
            elif status_num == 500:
                print("Bad request (Status 500) for /api/Health/ContactList")
                return 500
            else:
                print("Error")

        except Exception as e:
            print(e)

    def health_ready():
        try:
            open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-HealthCheck-Ready")))
            open_tab_button.click()

            # Click the "Try it out" button
            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-HealthCheck-Ready"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))

            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for user details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-HealthCheck-Ready"]/div[1]/button[1]')))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/Health/Ready\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Health/Ready\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Health/Ready\n")
                return 400
            elif status_num == 500:
                print("Bad request (Status 500) for /api/Health/Ready")
                return 500
            else:
                print("Error")

        except Exception as e:
            print(e)
            
    contactList()
    health_ready()
    