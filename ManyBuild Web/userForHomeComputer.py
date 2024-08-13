from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import newFileOpen
import globalVars
import time

def userTests(driver):

    #user methods
    #user details

    def userDetails():
        open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-User-get_api_User_details")))
        open_tab_button.click()

        try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
        try_it_out_button.click()

        execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
        execute_button.click()

        status_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr.response")))
        
        status_text = status_element.get_attribute('textContent')
        #print(status_text) #line for debugging
        #print 200
        print("Status for user details: " + status_text[0:3])
        status_num = int(status_text[0:3])

        close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-User-get_api_User_details']/div[1]/button[1]")))
        close_tab.click()
        #time.sleep(2)

        if status_num == 200:
            print("API call successful (Status 200) for /api/User/details\n")
            return 200
        elif status_num == 401:
            print("Unauthorized access (Status 401) for /api/User/details\n")
            return 401
        elif status_num == 400:
            print("Bad request (Status 400) for /api/User/details\n")
            return 400
        else:
            print("Error")

    def userDocs():
        open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-User-get_api_User_documents")))
        open_tab_button.click()

        try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
        try_it_out_button.click()

        execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
        execute_button.click()

        status_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr.response")))
        
        status_text = status_element.get_attribute('textContent')
        #print(status_text) #line for debugging
        #print 200
        print("Status for user details: " + status_text[0:3])
        status_num = int(status_text[0:3])

        close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-User-get_api_User_documents']/div[1]/button[1]")))
        close_tab.click()
        #time.sleep(2)

        if status_num == 200:
            print("API call successful (Status 200) for /api/User/documents\n")
            return 200
        elif status_num == 401:
            print("Unauthorized access (Status 401) for /api/User/documents\n")
            return 401
        elif status_num == 400:
            print("Bad request (Status 400) for /api/User/documents\n")
            return 400
        else:
            print("Error")

    def userProfile():
        open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-User-get_api_User_profile")))
        open_tab_button.click()

        try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
        try_it_out_button.click()

        execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
        execute_button.click()

        status_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr.response")))
        
        status_text = status_element.get_attribute('textContent')
        #print(status_text) #line for debugging
        #print 200
        print("Status for user details: " + status_text[0:3])
        status_num = int(status_text[0:3])

        close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-User-get_api_User_profile']/div[1]/button[1]")))
        close_tab.click()
        #time.sleep(2)

        if status_num == 200:
            print("API call successful (Status 200) for /api/User/Profile\n")
            return 200
        elif status_num == 401:
            print("Unauthorized access (Status 401) for /api/User/Profile\n")
            return 401
        elif status_num == 400:
            print("Bad request (Status 400) for /api/User/Profile\n")
            return 400
        else:
            print("Error")

    def userProjects():
        open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-User-get_api_User_projects")))
        open_tab_button.click()

        try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
        try_it_out_button.click()

        execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
        execute_button.click()

        status_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr.response")))
        
        status_text = status_element.get_attribute('textContent')
        #print(status_text) #line for debugging
        #print 200
        print("Status for user details: " + status_text[0:3])
        status_num = int(status_text[0:3])

        close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-User-get_api_User_projects']/div[1]/button[1]")))
        close_tab.click()

        if status_num == 200:
            print("API call successful (Status 200) for /api/User/Projects\n")
            return 200
        elif status_num == 401:
            print("Unauthorized access (Status 401) for /api/User/Projects\n")
            return 401
        elif status_num == 400:
            print("Bad request (Status 400) for /api/User/Projects\n")
            return 400
        else:
            print("Error")

    def userSummary():
        open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-User-get_api_User_summary")))
        open_tab_button.click()

        try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
        try_it_out_button.click()

        execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
        execute_button.click()

        status_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr.response")))
        
        status_text = status_element.get_attribute('textContent')
        #print(status_text) #line for debugging
        #print 200
        print("Status for user details: " + status_text[0:3])
        status_num = int(status_text[0:3])

        close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-User-get_api_User_summary']/div/button[1]")))
        close_tab.click()

        if status_num == 200:
            print("API call successful (Status 200) for /api/User/summary\n")
            return 200
        elif status_num == 401:
            print("Unauthorized access (Status 401) for /api/User/summary\n")
            return 401
        elif status_num == 400:
            print("Bad request (Status 400) for /api/User/summary\n")
            return 400
        else:
            print("Error")

    def userToolImages():
        open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-User-get_api_User_toolimages")))
        open_tab_button.click()

        try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
        try_it_out_button.click()

        execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
        execute_button.click()

        status_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='operations-User-get_api_User_toolimages']/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]")))
        
        status_text = status_element.get_attribute('textContent')
        #print(status_text) #line for debugging
        #print 200
        print("Status for user details: " + status_text[0:3])
        status_num = int(status_text[0:3])
        time.sleep(.5)

        close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-User-get_api_User_toolimages']/div/button[1]")))
        close_tab.click()

        if status_num == 200:
            print("API call successful (Status 200) for /api/User/toolimages\n")
            return 200
        elif status_num == 401:
            print("Unauthorized access (Status 401) for /api/User/toolimages\n")
            return 401
        elif status_num == 400:
            print("Bad request (Status 400) for /api/User/toolimages\n")
            return 400
        else:
            print("Error")

    def userToolImagesID():
        open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-User-get_api_User_usertoolimages__UserID_")))
        open_tab_button.click()

        try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
        try_it_out_button.click()

        text_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='operations-User-get_api_User_usertoolimages__UserID_']/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input")))
        text_field.send_keys(globalVars.USER_ID)

        execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
        execute_button.click()

        status_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='operations-User-get_api_User_usertoolimages__UserID_']/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]")))

        status_text = status_element.get_attribute('textContent')
        #print(status_text) #line for debugging
        #print 200
        print("Status for user details: " + status_text[0:3])
        status_num = int(status_text[0:3])

        close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-User-get_api_User_usertoolimages__UserID_']/div[1]/button[1]")))
        close_tab.click()

        if status_num == 200:
            print("API call successful (Status 200) for /api/User/toolimagesID\n")
            return 200
        elif status_num == 401:
            print("Unauthorized access (Status 401) for /api/User/toolimagesID\n")
            return 401
        elif status_num == 400:
            print("Bad request (Status 400) for /api/User/toolimagesID\n")
            return 400
        else:
            print("Error")


    def userAvailablejobs():
        open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-User-get_api_User_availablejobs")))
        open_tab_button.click()

        try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
        try_it_out_button.click()

        execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
        execute_button.click()

        status_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='operations-User-get_api_User_availablejobs']/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]")))
        
        status_text = status_element.get_attribute('textContent')
        #print(status_text) #line for debugging
        #print 200
        print("Status for user details: " + status_text[0:3])
        status_num = int(status_text[0:3])

        close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-User-get_api_User_availablejobs']/div/button[1]")))
        close_tab.click()

        if status_num == 200:
            print("API call successful (Status 200) for /api/User/availablejobs\n")
            return 200
        elif status_num == 401:
            print("Unauthorized access (Status 401) for /api/User/availablejobs\n")
            return 401
        elif status_num == 400:
            print("Bad request (Status 400) for /api/User/availablejobs\n")
            return 400
        else:
            print("Error")
        
    def userBudgets():
        open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-User-get_api_User_budgets")))
        open_tab_button.click()

        try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
        try_it_out_button.click()

        execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
        execute_button.click()

        status_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr.response")))
        
        status_text = status_element.get_attribute('textContent')
        #print(status_text) #line for debugging
        #print 200
        print("Status for user details: " + status_text[0:3])
        status_num = int(status_text[0:3])

        close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-User-get_api_User_budgets']/div/button[1]")))
        close_tab.click()

        if status_num == 200:
            print("API call successful (Status 200) for /api/User/budgets\n")
            return 200
        elif status_num == 401:
            print("Unauthorized access (Status 401) for /api/User/budgets\n")
            return 401
        elif status_num == 400:
            print("Bad request (Status 400) for /api/User/budgets\n")
            return 400
        else:
            print("Error")

    def userProjectDetails():
        open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-User-get_api_User_projectdetails")))
        open_tab_button.click()

        try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
        try_it_out_button.click()

        execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
        execute_button.click()

        status_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr.response")))
        
        status_text = status_element.get_attribute('textContent')
        #print(status_text) #line for debugging
        #print 200
        print("Status for user details: " + status_text[0:3])
        status_num = int(status_text[0:3])

        close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-User-get_api_User_projectdetails']/div/button[1]")))
        close_tab.click()

        if status_num == 200:
            print("API call successful (Status 200) for /api/User/projectdetails\n")
            return 200
        elif status_num == 401:
            print("Unauthorized access (Status 401) for /api/User/projectdetails\n")
            return 401
        elif status_num == 400:
            print("Bad request (Status 400) for /api/User/projectdetails\n")
            return 400
        else:
            print("Error")

    def userJobs():
        open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-User-get_api_User_jobs")))
        open_tab_button.click()

        try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
        try_it_out_button.click()

        execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
        execute_button.click()

        status_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr.response")))
        
        status_text = status_element.get_attribute('textContent')
        #print(status_text) #line for debugging
        #print 200
        print("Status for user details: " + status_text[0:3])
        status_num = int(status_text[0:3])

        close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-User-get_api_User_jobs']/div/button[1]")))
        close_tab.click()

        if status_num == 200:
            print("API call successful (Status 200) for /api/User/jobs\n")
            return 200
        elif status_num == 401:
            print("Unauthorized access (Status 401) for /api/User/jobs\n")
            return 401
        elif status_num == 400:
            print("Bad request (Status 400) for /api/User/jobs\n")
            return 400
        else:
            print("Error")


    def userJobOverviews():
        open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-User-get_api_User_joboverviews")))
        open_tab_button.click()

        try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
        try_it_out_button.click()

        execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
        execute_button.click()

        status_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr.response")))
        
        status_text = status_element.get_attribute('textContent')
        #print(status_text) #line for debugging
        #print 200
        print("Status for user details: " + status_text[0:3])
        status_num = int(status_text[0:3])

        close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-User-get_api_User_joboverviews']/div/button[1]")))
        close_tab.click()

        if status_num == 200:
            print("API call successful (Status 200) for /api/User/joboverview\n")
            return 200
        elif status_num == 401:
            print("Unauthorized access (Status 401) for /api/User/joboverview\n")
            return 401
        elif status_num == 400:
            print("Bad request (Status 400) for /api/User/joboverview\n")
            return 400
        else:
            print("Error")

    def userCategories():
        open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-User-get_api_User_categories")))
        open_tab_button.click()

        try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
        try_it_out_button.click()

        execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
        execute_button.click()

        status_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr.response")))
        
        status_text = status_element.get_attribute('textContent')
        #print(status_text) #line for debugging
        #print 200
        print("Status for user details: " + status_text[0:3])
        status_num = int(status_text[0:3])

        close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-User-get_api_User_categories']/div/button[1]")))
        close_tab.click()

        if status_num == 200:
            print("API call successful (Status 200) for /api/User/categories\n")
            return 200
        elif status_num == 401:
            print("Unauthorized access (Status 401) for /api/User/categories\n")
            return 401
        elif status_num == 400:
            print("Bad request (Status 400) for /api/User/categories\n")
            return 400
        else:
            print("Error")

    def userDisciplines():
        open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-User-get_api_User_disciplines")))
        open_tab_button.click()

        try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
        try_it_out_button.click()

        execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
        execute_button.click()

        status_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr.response")))
        
        status_text = status_element.get_attribute('textContent')
        #print(status_text) #line for debugging
        #print 200
        print("Status for user details: " + status_text[0:3])
        status_num = int(status_text[0:3])

        close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-User-get_api_User_disciplines']/div/button[1]")))
        close_tab.click()

        if status_num == 200:
            print("API call successful (Status 200) for /api/User/disciplines\n")
            return 200
        elif status_num == 401:
            print("Unauthorized access (Status 401) for /api/User/disciplines\n")
            return 401
        elif status_num == 400:
            print("Bad request (Status 400) for /api/User/disciplines\n")
            return 400
        else:
            print("Error")

    def userTemplates():
        open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-User-get_api_User_templates")))
        open_tab_button.click()

        try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
        try_it_out_button.click()

        execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
        execute_button.click()

        status_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr.response")))
        
        status_text = status_element.get_attribute('textContent')
        #print(status_text) #line for debugging
        #print 200
        print("Status for user details: " + status_text[0:3])
        status_num = int(status_text[0:3])

        close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-User-get_api_User_templates']/div/button[1]")))
        close_tab.click()

        if status_num == 200:
            print("API call successful (Status 200) for /api/User/templates\n")
            return 200
        elif status_num == 401:
            print("Unauthorized access (Status 401) for /api/User/templates\n")
            return 401
        elif status_num == 400:
            print("Bad request (Status 400) for /api/User/templates\n")
            return 400
        else:
            print("Error")

    def userLocations():
        open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-User-get_api_User_locations")))
        open_tab_button.click()

        try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
        try_it_out_button.click()

        execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
        execute_button.click()

        status_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr.response")))
        
        status_text = status_element.get_attribute('textContent')
        #print(status_text) #line for debugging
        #print 200
        print("Status for user details: " + status_text[0:3])
        status_num = int(status_text[0:3])

        close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-User-get_api_User_locations']/div/button[1]")))
        close_tab.click()

        if status_num == 200:
            print("API call successful (Status 200) for /api/User/locations\n")
            return 200
        elif status_num == 401:
            print("Unauthorized access (Status 401) for /api/User/locations\n")
            return 401
        elif status_num == 400:
            print("Bad request (Status 400) for /api/User/locations\n")
            return 400
        else:
            print("Error")

    def userDealAnalyzers():
        open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-User-get_api_User_dealanalyzers")))
        open_tab_button.click()

        try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
        try_it_out_button.click()

        execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
        execute_button.click()

        status_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr.response")))
        
        status_text = status_element.get_attribute('textContent')
        #print(status_text) #line for debugging
        #print 200
        print("Status for user details: " + status_text[0:3])
        status_num = int(status_text[0:3])

        close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-User-get_api_User_dealanalyzers']/div/button[1]")))
        close_tab.click()

        if status_num == 200:
            print("API call successful (Status 200) for /api/User/dealanalyzers\n")
            return 200
        elif status_num == 401:
            print("Unauthorized access (Status 401) for /api/User/dealanalyzers\n")
            return 401
        elif status_num == 400:
            print("Bad request (Status 400) for /api/User/dealanalyzers\n")
            return 400
        else:
            print("Error")

    def userCorpDocs():
        open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-User-get_api_User_corpdocuments")))
        open_tab_button.click()

        try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
        try_it_out_button.click()

        execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
        execute_button.click()

        status_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr.response")))
        
        status_text = status_element.get_attribute('textContent')
        #print(status_text) #line for debugging
        #print 200
        print("Status for user details: " + status_text[0:3])
        status_num = int(status_text[0:3])

        close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-User-get_api_User_corpdocuments']/div/button[1]")))
        close_tab.click()

        if status_num == 200:
            print("API call successful (Status 200) for /api/User/usercorpdocuments\n")
            return 200
        elif status_num == 401:
            print("Unauthorized access (Status 401) for /api/User/usercorpdocuments\n")
            return 401
        elif status_num == 400:
            print("Bad request (Status 400) for /api/User/usercorpdocuments\n")
            return 400
        else:
            print("Error")

    def usercorpdocumentsID():
        open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-User-get_api_User_usercorpdocuments__UserID_")))
        open_tab_button.click()

        try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
        try_it_out_button.click()

        text_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='operations-User-get_api_User_usercorpdocuments__UserID_']/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input")))
        text_field.send_keys(globalVars.USER_ID)

        execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
        execute_button.click()

        status_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr.response")))

        status_text = status_element.get_attribute('textContent')
        #print(status_text) #line for debugging
        #print 200
        print("Status for user details: " + status_text[0:3])
        status_num = int(status_text[0:3])

        close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-User-get_api_User_usercorpdocuments__UserID_']/div[1]/button[1]")))
        close_tab.click()

        if status_num == 200:
            print("API call successful (Status 200) for /api/User/usercorpdocuments/ID\n")
            return 200
        elif status_num == 401:
            print("Unauthorized access (Status 401) for /api/User/usercorpdocuments/ID\n")
            return 401
        elif status_num == 400:
            print("Bad request (Status 400) for /api/User/usercorpdocuments/ID\n")
            return 400
        else:
            print("Error")

    def userPrevwork():
        open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-User-get_api_User_prevwork")))
        open_tab_button.click()

        try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
        try_it_out_button.click()

        execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
        execute_button.click()

        status_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr.response")))
        
        status_text = status_element.get_attribute('textContent')
        #print(status_text) #line for debugging
        #print 200
        print("Status for user details: " + status_text[0:3])
        status_num = int(status_text[0:3])

        close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-User-get_api_User_prevwork']/div/button[1]")))
        close_tab.click()

        if status_num == 200:
            print("API call successful (Status 200) for /api/User/prevwork\n")
            return 200
        elif status_num == 401:
            print("Unauthorized access (Status 401) for /api/User/prevwork\n")
            return 401
        elif status_num == 400:
            print("Bad request (Status 400) for /api/User/prevwork\n")
            return 400
        else:
            print("Error")

    def userPrevworkID():
        open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-User-get_api_User_userprevwork__UserID_")))
        open_tab_button.click()

        try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
        try_it_out_button.click()

        text_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='operations-User-get_api_User_userprevwork__UserID_']/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input")))
        text_field.send_keys(globalVars.USER_ID)

        execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
        execute_button.click()

        status_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr.response")))

        status_text = status_element.get_attribute('textContent')
        #print(status_text) #line for debugging
        #print 200
        print("Status for user details: " + status_text[0:3])
        status_num = int(status_text[0:3])

        close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-User-get_api_User_userprevwork__UserID_']/div/button[1]")))
        close_tab.click()

        if status_num == 200:
            print("API call successful (Status 200) for /api/User/userprevwork/ID\n")
            return 200
        elif status_num == 401:
            print("Unauthorized access (Status 401) for /api/User/userprevwork/ID\n")
            return 401
        elif status_num == 400:
            print("Bad request (Status 400) for /api/User/userprevwork/ID\n")
            return 400
        else:
            print("Error")

    def userAllDocs():
        open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-User-get_api_User_alldocuments")))
        open_tab_button.click()

        try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
        try_it_out_button.click()

        execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
        execute_button.click()

        status_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr.response")))
        
        status_text = status_element.get_attribute('textContent')
        #print(status_text) #line for debugging
        #print 200
        print("Status for user details: " + status_text[0:3])
        status_num = int(status_text[0:3])

        close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-User-get_api_User_alldocuments']/div/button[1]")))
        close_tab.click()

        if status_num == 200:
            print("API call successful (Status 200) for /api/User/alldocuments\n")
            return 200
        elif status_num == 401:
            print("Unauthorized access (Status 401) for /api/User/alldocuments\n")
            return 401
        elif status_num == 400:
            print("Bad request (Status 400) for /api/User/alldocuments\n")
            return 400
        else:
            print("Error")

    def usertoprush():
        open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-User-get_api_User_toprush")))
        open_tab_button.click()

        try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
        try_it_out_button.click()

        execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
        execute_button.click()

        status_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr.response")))
        
        status_text = status_element.get_attribute('textContent')
        #print(status_text) #line for debugging
        #print 200
        print("Status for user details: " + status_text[0:3])
        status_num = int(status_text[0:3])

        close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-User-get_api_User_toprush']/div/button[1]")))
        close_tab.click()

        if status_num == 200:
            print("API call successful (Status 200) for /api/User/toprush\n")
            return 200
        elif status_num == 401:
            print("Unauthorized access (Status 401) for /api/User/toprush\n")
            return 401
        elif status_num == 400:
            print("Bad request (Status 400) for /api/User/toprush\n")
            return 400
        else:
            print("Error")

    def userOnline():
        open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-User-get_api_User_Online__userid_")))
        open_tab_button.click()

        try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
        try_it_out_button.click()

        text_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='operations-User-get_api_User_Online__userid_']/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input")))
        text_field.send_keys(globalVars.USER_ID)

        execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
        execute_button.click()

        status_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr.response")))

        status_text = status_element.get_attribute('textContent')
        #print(status_text) #line for debugging
        #print 200
        print("Status for user details: " + status_text[0:3])
        status_num = int(status_text[0:3])

        close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-User-get_api_User_Online__userid_']/div/button[1]")))
        close_tab.click()

        if status_num == 200:
            print("API call successful (Status 200) for /api/User/Online\n")
            return 200
        elif status_num == 401:
            print("Unauthorized access (Status 401) for /api/User/Online\n")
            return 401
        elif status_num == 400:
            print("Bad request (Status 400) for /api/User/Online\n")
            return 400
        else:
            print("Error")

    def userGenerateSetupSubPaymentLink():
        open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-User-get_api_User_GenerateSetupSubscriptionPaymentLink")))
        open_tab_button.click()

        try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
        try_it_out_button.click()

        execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
        execute_button.click()

        status_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='operations-User-get_api_User_GenerateSetupSubscriptionPaymentLink']/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]")))
        
        status_text = status_element.get_attribute('textContent')
        #print(status_text) #line for debugging
        #print 200
        print("Status for user details: " + status_text[0:3])
        status_num = int(status_text[0:3])

        close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-User-get_api_User_GenerateSetupSubscriptionPaymentLink']/div/button[1]")))
        close_tab.click()

        if status_num == 200:
            print("API call successful (Status 200) for /api/User/GenerateSetupSubscriptionPaymentLink\n")
            return 200
        elif status_num == 401:
            print("Unauthorized access (Status 401) for /api/User/GenerateSetupSubscriptionPaymentLink\n")
            return 401
        elif status_num == 400:
            print("Bad request (Status 400) for /api/User/GenerateSetupSubscriptionPaymentLink\n")
            return 400
        else:
            print("Error")

    def userGenerateSetupStripeConnectedAccount():
        open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-User-get_api_User_GenerateSetupStripeConnectedAccount")))
        open_tab_button.click()

        try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
        try_it_out_button.click()

        execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
        execute_button.click()

        status_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='operations-User-get_api_User_GenerateSetupStripeConnectedAccount']/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]")))
        
        status_text = status_element.get_attribute('textContent')
        #print(status_text) #line for debugging
        #print 200
        print("Status for user details: " + status_text[0:3])
        status_num = int(status_text[0:3])

        close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='operations-User-get_api_User_GenerateSetupStripeConnectedAccount']/div[1]/button[1]")))
        close_tab.click()

        if status_num == 200:
            print("API call successful (Status 200) for /api/User/GenerateSetupStripeConnectedAccount\n")
            return 200
        elif status_num == 401:
            print("Unauthorized access (Status 401) for /api/User/GenerateSetupStripeConnectedAccount\n")
            return 401
        elif status_num == 400:
            print("Bad request (Status 400) for /api/User/GenerateSetupStripeConnectedAccount\n")
            return 400
        else:
            print("Error")


    try:
        # Navigate to the Swagger UI
        #driver.get("https://wsmanybuild.azurewebsites.net/Swagger/index.html") #uncomment to run on own

        # Wait for the Swagger UI element to be present
        wait = WebDriverWait(driver, 20)  # Adjust timeout as needed
        def authorize():
            # Click the login button
            time.sleep(1)
            login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.opblock-summary-control")))
            login_button.click()

            # Click the "Try it out" button
            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            # Enter login details
            time.sleep(1)
            text_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[class*='body-param']")))
            text_field.clear()
            text_to_write = ''
            text_field.send_keys(text_to_write)
            #print("Text written to the text field: ", text_to_write)

            # Execute login
            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            # Wait for the response
            time.sleep(.5)
            download = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.download-contents")))
            download.click()

            # Open the new file to get the key
            key = newFileOpen.openNewFile()
            #print(key)

            # Authorize with the obtained key
            authorize_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.authorize.unlocked")))
            authorize_button.click()

            time.sleep(1)
            key_input_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input")))
            key_input_field.send_keys("Bearer " + key)

            final_press_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.modal-btn.auth.authorize.button")))
            final_press_button.click()

            # Check if authorization was successful
            try:
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.authorize.locked")))

                close = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.btn.modal-btn.auth.btn-done.button")))
                close.click()

                close_open_tab = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.opblock-summary-control")))
                close_open_tab.click()
                time.sleep(2)
            except Exception as e:
                print("Authorization was not granted")
                SystemExit()

        #authorize()
        #prints the 200 or 401 status of each user field; 200 is good, 401 is bad
        userDetailsNum = userDetails()
        userDocsNum = userDocs()
        userProfileNum = userProfile()
        userProjectsNum = userProjects()
        userSummaryNum = userSummary()
        userToolimagesNum = userToolImages()
        userToolImagesIDNum = userToolImagesID()
        userAvailablejobsNum = userAvailablejobs()
        userBudgetsNum = userBudgets()
        userProjectDetailsNum = userProjectDetails()
        userJobsNum = userJobs()
        userJobOverviewsNum = userJobOverviews()
        userCategoriesNum = userCategories()
        userDisciplinesNum = userDisciplines()
        userTemplatesNum = userTemplates()
        userLocationsNum = userLocations()
        userDealAnalyzersNum = userDealAnalyzers()
        userCorpDocsNum = userCorpDocs()
        usercorpdocumentsIDNum = usercorpdocumentsID()
        userPrevworkNum = userPrevwork()
        userPrevworkIDNum = userPrevworkID()
        userAllDocsNum = userAllDocs()
        usertoprushNum = usertoprush()
        userOnlineNum = userOnline()
        userGenerateSetupSubPaymentLinkNum = userGenerateSetupSubPaymentLink()
        userGenerateSetupStripeConnectedAccountNum = userGenerateSetupStripeConnectedAccount()
        

    except Exception as e:
        print(e)
        # driver.quit()