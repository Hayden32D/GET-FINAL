from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import newFileOpen
import globalVars

def Disicpline_runner(driver):
    wait = WebDriverWait(driver, 15)

    def Discpline():
        try:
            open_tab = wait.until(EC.element_to_be_clickable((By.ID, "operations-Discipline-get_api_Discipline_listtaskdisciplines__TaskID_")))
            open_tab.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Discipline-get_api_Discipline_listtaskdisciplines__TaskID_"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input')))
            text_field.send_keys(globalVars.TASK_ID)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Discipline-get_api_Discipline_listtaskdisciplines__TaskID_"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))

            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for user details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Discipline-get_api_Discipline_listtaskdisciplines__TaskID_"]/div/button[1]')))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/Discipline\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Discipline\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Discipline\n")
                return 400
            else:
                print("Error")                

        except Exception as e:
            print(e)

    Discpline()