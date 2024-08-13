from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import newFileOpen
import globalVars

def project_runner(driver):
    wait = WebDriverWait(driver, 15)

    def test1():
        try:
            open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-Project-get_api_Project__id__tasks")))
            open_tab_button.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Project-get_api_Project__id__tasks"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input')))
            text_field.send_keys(globalVars.ID) #TO-DO find a working number to send

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Project-get_api_Project__id__tasks"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))
            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for project details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Project-get_api_Project__id__tasks"]/div[1]/button[1]/div')))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/Project/{id}/tasks\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Project/{id}/tasks\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Project/{id}/tasks\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/Project/{id}/tasks\n")
                return 500
            else:
                print("Error")


        except Exception as e:
            print(e)

    def test2():
        try:
            open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-Project-get_api_Project__ProjID__notes")))
            open_tab_button.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Project-get_api_Project__ProjID__notes"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input')))
            text_field.send_keys(globalVars.ID) #TO-DO find a working number to send

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Project-get_api_Project__ProjID__notes"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))
            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for project details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Project-get_api_Project__ProjID__notes"]/div[1]/button[1]/div')))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/Project/{ProjID}/notes\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Project/{ProjID}/notes\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Project/{ProjID}/notes\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/Project/{ProjID}/notes\n")
                return 500
            else:
                print("Error")


        except Exception as e:
            print(e)

    def test3():
        try:
            open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-Project-get_api_Project_note__ID_")))
            open_tab_button.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Project-get_api_Project_note__ID_"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input')))
            text_field.send_keys(globalVars.ID) #TO-DO find a working number to send

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Project-get_api_Project_note__ID_"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))
            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for project details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Project-get_api_Project_note__ID_"]/div[1]/button[1]/div')))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/Project/note/{ID}\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Project/note/{ID}\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Project/note/{ID}\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/Project/note/{ID}\n")
                return 500
            else:
                print("Error")


        except Exception as e:
            print(e)

    testResult = test1()
    testResult1 = test2()
    testResult2 = test3()

    if((testResult and testResult1 and testResult2) == 200):
        print("All tests passed")
        return 200
