from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import newFileOpen
import globalVars

def project_job_runner(driver):
    wait = WebDriverWait(driver, 15)

    def test1():
        try:
            open_tab = wait.until(EC.element_to_be_clickable((By.ID, "operations-ProjectJob-get_api_ProjectJob")))
            open_tab.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-ProjectJob-get_api_ProjectJob"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))
            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for user details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-ProjectJob-get_api_ProjectJob"]/div[1]/button[1]/div')))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/ProjectJob\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/ProjectJob\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/ProjectJob\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/ProjectJob\n")
                return 500
            else:
                print("Error: Something went wrong. Status code: " + status_text[0:3])
                return -1
            
        except Exception as e:
            print(e)

    def test2():
        try:
            open_tab = wait.until(EC.element_to_be_clickable((By.ID, "operations-ProjectJob-get_api_ProjectJob_listbyproject__projectid_")))
            open_tab.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-ProjectJob-get_api_ProjectJob_listbyproject__projectid_"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input')))
            text_field.send_keys(globalVars.PROJ_ID)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-ProjectJob-get_api_ProjectJob_listbyproject__projectid_"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))
            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for user details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-ProjectJob-get_api_ProjectJob_listbyproject__projectid_"]/div[1]/button[1]/div')))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/ProjectJob/listbyproject/{projectid}\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/ProjectJob/listbyproject/{projectid}\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/ProjectJob/listbyproject/{projectid}\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/ProjectJob/listbyproject/{projectid}\n")
                return 500
            else:
                print("Error: Something went wrong. Status code: " + status_text[0:3])
                return -1
            
        
        except Exception as e:
                print(e)

    def test3():
        try:
            open_tab = wait.until(EC.element_to_be_clickable((By.ID, "operations-ProjectJob-get_api_ProjectJob_listbycontractor__contractorid_")))
            open_tab.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-ProjectJob-get_api_ProjectJob_listbycontractor__contractorid_"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input')))
            text_field.send_keys(globalVars.TASK_ID)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-ProjectJob-get_api_ProjectJob_listbycontractor__contractorid_"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))
            status_text = status_element.get_attribute('textContent')

            #print(status_text) #line for debugging
            #print 200
            print("Status for user details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-ProjectJob-get_api_ProjectJob_listbycontractor__contractorid_"]/div[1]/button[1]/div')))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/ProjectJob/listbycontractor/{contractorid}\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/ProjectJob/listbycontractor/{contractorid}\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/ProjectJob/listbycontractor/{contractorid}\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/ProjectJob/listbycontractor/{contractorid}\n")
                return 500
            else:
                print("Error: Something went wrong. Status code: " + status_text[0:3])
                return -1
            
        except Exception as e:
            print(e)

    def test4():
        try:
            open_tab = wait.until(EC.element_to_be_clickable((By.ID, "operations-ProjectJob-get_api_ProjectJob__id_")))
            open_tab.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-ProjectJob-get_api_ProjectJob__id_"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input')))
            text_field.send_keys(globalVars.PROJ_JOB_ID)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-ProjectJob-get_api_ProjectJob__id_"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))
            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for user details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-ProjectJob-get_api_ProjectJob__id_"]/div[1]/button[1]/div')))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/ProjectJob/{id}\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/ProjectJob/{id}\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/ProjectJob/{id}\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/ProjectJob/{id}\n")
                return 500
            else:
                print("Error: Something went wrong. Status code: " + status_text[0:3])
                return -1
            
        except Exception as e:
            print(e)

    def test5():
        try:
            open_tab = wait.until(EC.element_to_be_clickable((By.ID, "operations-ProjectJob-get_api_ProjectJob_milestones__contractid_")))
            open_tab.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-ProjectJob-get_api_ProjectJob_milestones__contractid_"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input')))
            text_field.send_keys(globalVars.TASK_ID)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-ProjectJob-get_api_ProjectJob_milestones__contractid_"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))
            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for user details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-ProjectJob-get_api_ProjectJob_milestones__contractid_"]/div[1]/button[1]/div')))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/ProjectJob/milestones/{contractid}\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/ProjectJob/milestones/{contractid}\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/ProjectJob/milestones/{contractid}\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/ProjectJob/milestones/{contractid}\n")
                return 500
            else:
                print("Error: Something went wrong. Status code: " + status_text[0:3])
                return -1
            
        except Exception as e:
            print(e)


    testRun1 = test1()
    testRun2 = test2()
    testRun3 = test3()
    testRun4 = test4()
    testRun5 = test5()

    if((testRun1 and testRun2 and testRun3 and testRun4 and testRun5) == 200):
        print("All API calls successful")
        return 200







            

