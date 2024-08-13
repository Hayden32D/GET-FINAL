from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import newFileOpen
import globalVars
import time

def Job_runner(driver):
    wait = WebDriverWait(driver, 20)

    def test1():
        try:
            open_tab = wait.until(EC.element_to_be_clickable((By.ID, "operations-Job-get_api_Job__jobID__getavailabledetail")))
            open_tab.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Job-get_api_Job__jobID__getavailabledetail"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input')))
            text_field.send_keys(globalVars.PROJ_ID)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Job-get_api_Job__jobID__getavailabledetail"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))

            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for user details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Job-get_api_Job__jobID__getavailabledetail"]/div[1]/button[1]')))
            close_tab.click()

            # Return the status number
            if status_num == 200:
                print("API call successful (Status 200) for /api/Job/{JobID}/getavailabledetail\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Job/{JobID}/getavailabledetail\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Job/{JobID}/getavailabledetail\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/Job/{JobID}/getavailabledetail\n")
                return 500
            else:
                print("Unexpected status code: ", status_num)
                return status_num

        except Exception as e:
            print(e)

    def test2():
        try:
            open_tab = wait.until(EC.element_to_be_clickable((By.ID, "operations-Job-get_api_Job__jobID__details")))
            open_tab.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Job-get_api_Job__jobID__details"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input')))
            text_field.send_keys(globalVars.PROJ_ID)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Job-get_api_Job__jobID__details"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))

            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for user details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Job-get_api_Job__jobID__details"]/div[1]/button[1]')))
            close_tab.click()

            # Return the status number
            if status_num == 200:
                print("API call successful (Status 200) for /api/Job/{JobID}/details\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Job/{JobID}/details\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Job/{JobID}/details\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/Job/{JobID}/details\n")
                return 500
            else:
                print("Unexpected status code: ", status_num)
                return status_num

        except Exception as e:
            print(e)
    
    def test3():
        try:
            open_tab = wait.until(EC.element_to_be_clickable((By.ID, "operations-Job-get_discipline__jobID___userID_")))
            open_tab.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Job-get_discipline__jobID___userID_"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr[1]/td[2]/input')))
            text_field.send_keys(globalVars.PROJ_ID)

            text_field2 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Job-get_discipline__jobID___userID_"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr[2]/td[2]/input')))
            text_field2.send_keys(globalVars.USER_ID)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Job-get_discipline__jobID___userID_"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))

            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for user details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Job-get_discipline__jobID___userID_"]/div[1]/button[1]')))
            close_tab.click()

            # Return the status number
            if status_num == 200:
                print("API call successful (Status 200) for /api/Job/{JobID}/{userID}\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Job/{JobID}/{userID}\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Job/{JobID}/{userID}\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/Job/{JobID}/{userID}\n")
                return 500
            else:
                print("Unexpected status code: ", status_num)
                return status_num

        except Exception as e:
            print(e)

    def test4():
        try:
            open_tab = wait.until(EC.element_to_be_clickable((By.ID, "operations-Job-get_api_Job__jobID__tasks")))
            open_tab.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Job-get_api_Job__jobID__tasks"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input')))
            text_field.send_keys(globalVars.PROJ_ID)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Job-get_api_Job__jobID__tasks"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))

            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for user details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Job-get_api_Job__jobID__tasks"]/div[1]/button[1]')))
            close_tab.click()

            # Return the status number
            if status_num == 200:
                print("API call successful (Status 200) for /api/Job/{JobID}/tasks\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Job/{JobID}/tasks\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Job/{JobID}/tasks\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/Job/{JobID}/tasks\n")
                return 500
            else:
                print("Unexpected status code: ", status_num)
                return status_num

        except Exception as e:
            print(e)
    
    def test5():
        try:
            open_tab = wait.until(EC.element_to_be_clickable((By.ID, "operations-Job-get_api_Job__jobID__disciplines")))
            open_tab.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Job-get_api_Job__jobID__disciplines"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input')))
            text_field.send_keys(globalVars.PROJ_ID)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Job-get_api_Job__jobID__disciplines"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))

            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for user details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Job-get_api_Job__jobID__disciplines"]/div[1]/button[1]')))
            close_tab.click()

            # Return the status number
            if status_num == 200:
                print("API call successful (Status 200) for /api/Job/{JobID}/disciplines\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Job/{JobID}/disciplines\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Job/{JobID}/disciplines\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/Job/{JobID}/disciplines\n")
                return 500
            else:
                print("Unexpected status code: ", status_num)
                return status_num

        except Exception as e:
            print(e)

    def test6():
        try:
            open_tab = wait.until(EC.element_to_be_clickable((By.ID, "operations-Job-get_api_Job_topavailable__UserID_")))
            open_tab.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Job-get_api_Job_topavailable__UserID_"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input')))
            text_field.send_keys(globalVars.PROJ_ID)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Job-get_api_Job_topavailable__UserID_"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))

            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for user details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Job-get_api_Job_topavailable__UserID_"]/div[1]/button[1]')))
            close_tab.click()

            # Return the status number
            if status_num == 200:
                print("API call successful (Status 200) for /api/Job/topavailable/{UserID}\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Job/{JobID}/topavailable/{UserID}\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Job/{JobID}/topavailable/{UserID}\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/Job/{JobID}/topavailable/{UserID}\n")
                return 500
            else:
                print("Unexpected status code: ", status_num)
                return status_num

        except Exception as e:
            print(e)

    def test7():
        try:
            open_tab = wait.until(EC.element_to_be_clickable((By.ID, "operations-Job-get_api_Job__jobID__Chat__userID_")))
            open_tab.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Job-get_api_Job__jobID__Chat__userID_"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr[1]/td[2]/input')))
            text_field.send_keys(globalVars.PROJ_ID)

            text_field2 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Job-get_api_Job__jobID__Chat__userID_"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr[2]/td[2]/input')))
            text_field2.send_keys(globalVars.USER_ID)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Job-get_api_Job__jobID__Chat__userID_"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))

            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for user details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Job-get_api_Job__jobID__Chat__userID_"]/div[1]/button[1]')))
            close_tab.click()

            # Return the status number
            if status_num == 200:
                print("API call successful (Status 200) for /api/Job/{jobID}/Chat/{userID}\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Job/{jobID}/Chat/{userID}\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Job/{jobID}/Chat/{userID}\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/Job/{jobID}/Chat/{userID}\n")
                return 500
            else:
                print("Unexpected status code: ", status_num)
                return status_num

        except Exception as e:
            print(e)

    def test8():
        try:
            open_tab = wait.until(EC.element_to_be_clickable((By.ID, "operations-Job-get_api_Job__jobID__ChangeOrders")))
            open_tab.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Job-get_api_Job__jobID__ChangeOrders"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input')))
            text_field.send_keys(globalVars.PROJ_ID)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Job-get_api_Job__jobID__ChangeOrders"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))

            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for user details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Job-get_api_Job__jobID__ChangeOrders"]/div[1]/button[1]')))
            close_tab.click()

            # Return the status number
            if status_num == 200:
                print("API call successful (Status 200) for /api/Job/{jobID}/ChangeOrders\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Job/{jobID}/ChangeOrders\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Job/{jobID}/ChangeOrders\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/Job/{jobID}/ChangeOrders\n")
                return 500
            else:
                print("Unexpected status code: ", status_num)
                return status_num

        except Exception as e:
            print(e)

    def test9():
        try:
            open_tab = wait.until(EC.element_to_be_clickable((By.ID, "operations-Job-get_api_Job__jobID__Contractors")))
            open_tab.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Job-get_api_Job__jobID__Contractors"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input')))
            text_field.send_keys(globalVars.PROJ_ID)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Job-get_api_Job__jobID__Contractors"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))

            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for user details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Job-get_api_Job__jobID__Contractors"]/div[1]/button[1]')))
            close_tab.click()

            # Return the status number
            if status_num == 200:
                print("API call successful (Status 200) for /api/Job/{jobID}/Contractors\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Job/{jobID}/Contractors\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Job/{jobID}/Contractors\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/Job/{jobID}/Contractors\n")
                return 500
            else:
                print("Unexpected status code: ", status_num)
                return status_num

        except Exception as e:
            print(e)

    def test10():
        try:
            open_tab = wait.until(EC.element_to_be_clickable((By.ID, "operations-Job-get_api_Job__projectId__notes")))
            open_tab.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Job-get_api_Job__projectId__notes"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input')))
            text_field.send_keys(globalVars.PROJ_ID)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Job-get_api_Job__projectId__notes"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))

            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for user details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Job-get_api_Job__projectId__notes"]/div[1]/button[1]')))
            close_tab.click()

            # Return the status number
            if status_num == 200:
                print("API call successful (Status 200) for /api/Job/{projectID}/notes\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Job/{projectID}/notes\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Job/{projectID}/notes\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/Job/{projectID}/notes\n")
                return 500
            else:
                print("Unexpected status code: ", status_num)
                return status_num

        except Exception as e:
            print(e)

    def test11():
        try:
            open_tab = wait.until(EC.element_to_be_clickable((By.ID, "operations-Job-get_api_Job_note__ID_")))
            open_tab.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Job-get_api_Job_note__ID_"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input')))
            text_field.send_keys(globalVars.CONTRACT_ID)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Job-get_api_Job_note__ID_"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))

            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for user details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Job-get_api_Job_note__ID_"]/div[1]/button[1]')))
            close_tab.click()

            # Return the status number
            if status_num == 200:
                print("API call successful (Status 200) for /api/Job/note/{ID}\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Job/note/{ID}\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Job/note/{ID}\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/Job/note/{ID}\n")
                return 500
            else:
                print("Unexpected status code: ", status_num)
                return status_num

        except Exception as e:
            print(e)
    

    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    test9()
    test10()
    test11()