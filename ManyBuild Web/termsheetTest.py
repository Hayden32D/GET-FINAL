from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import newFileOpen
import globalVars

def terms_runner(driver):
    wait = WebDriverWait(driver, 15)

    def test():
        try:
            open_tab = wait.until(EC.element_to_be_clickable((By.ID, "operations-TermsSheet-get_api_TermsSheet__id__view")))
            open_tab.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-TermsSheet-get_api_TermsSheet__id__view"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input')))
            text_field.send_keys(globalVars.TERMS_SHEET)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-TermsSheet-get_api_TermsSheet__id__view"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))

            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for user details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-TermsSheet-get_api_TermsSheet__id__view"]/div[1]/button[1]')))
            close_tab.click()

            # Return the status number
            if status_num == 200:
                print("API call successful (Status 200) for /api/TermsSheet/{id}/view\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/TermsSheet/{id}/view\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/TermsSheet/{id}/view\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/TermsSheet/{id}/view\n")
                return 500
            else:
                print("Unexpected status code: ", status_num)
                return status_num

        except Exception as e:
            print(e)

    test()