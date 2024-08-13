#Tests the chat GETs

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import newFileOpen
import globalVars
import time

def chatGET_Tests(driver):
    #chat methods
    #chat GETs
    wait = WebDriverWait(driver, 15)
    def chat():
        try:
            open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-Chat-get_api_Chat")))
            open_tab_button.click()

            # Click the "Try it out" button
            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()
            
            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='operations-Chat-get_api_Chat']/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]")))

            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for user details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-Chat-get_api_Chat']/div[1]/button[1]")))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/Chat\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Chat\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Chat\n")
                return 400
            elif status_num == 500:
                print("Bad request (Status 500) for /api/Chat\n")
                return 500
            else:
                print("Error")

        except Exception as e:
            print(e)

    def chatID():
        try:
            open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-Chat-get_api_Chat__id_")))
            open_tab_button.click()

            # Click the "Try it out" button
            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='operations-Chat-get_api_Chat__id_']/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input")))
            text_field.send_keys(globalVars.CHAT_ID)
            
            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='operations-Chat-get_api_Chat__id_']/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]")))

            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for user details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-Chat-get_api_Chat__id_']/div[1]/button[1]")))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/Chat/{id}\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Chat/{id}\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Chat/{id}\n")
                return 400
            elif status_num == 500:
                print("Bad request (Status 500) for /api/Chat/{id}\n")
                return 500
            else:
                print("Error")

        except Exception as e:
            print(e)
    
    def specific_chat():
        try:
            open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-Chat-get_api_Chat__threadID___userID_")))
            open_tab_button.click()

            # Click the "Try it out" button
            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field2 = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='operations-Chat-get_api_Chat__threadID___userID_']/div[2]/div/div[1]/div[2]/div/table/tbody/tr[1]/td[2]/input")))
            text_field2.send_keys(globalVars.THREAD_ID)

            text_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='operations-Chat-get_api_Chat__threadID___userID_']/div[2]/div/div[1]/div[2]/div/table/tbody/tr[2]/td[2]/input")))
            text_field.send_keys(globalVars.CHAT_ID)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='operations-Chat-get_api_Chat__threadID___userID_']/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]")))

            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for user details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-Chat-get_api_Chat__threadID___userID_']/div[1]/button[1]")))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/Chat/{id}/{userID}\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Chat/{id}/{userID}\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Chat/{id}/{userID}\n")
                return 400
            elif status_num == 500:
                print("Bad request (Status 500) for /api/Chat/{id}/{userID}\n")
                return 500
            else:
                print("Error")

        except Exception as e:
            print(e)

    def chat_translated():
        try:
            open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-Chat-get_api_Chat_NeedTranslated")))
            open_tab_button.click()

            # Click the "Try it out" button
            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()
            
            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='operations-Chat-get_api_Chat_NeedTranslated']/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]")))

            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for user details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-Chat-get_api_Chat_NeedTranslated']/div[1]/button[1]")))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/Chat/NeedsTranslated\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Chat/NeedsTranslated\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Chat/NeedsTranslated\n")
                return 400
            else:
                print("Error")

        except Exception as e:
            print(e)


    chat()
    chatID()
    specific_chat()
    chat_translated()