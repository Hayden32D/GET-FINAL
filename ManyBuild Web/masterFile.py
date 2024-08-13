import userForHomeComputer
import profileTests
import jigxTest
import chatTests
import lookupTests
import healthTests
import BidTests
import changeOrderTests
import ContractTests
import DealAnalyzerTests
import Discipline
import project_bid_tests
import document_tests
import milestoneTests
import termsheetTest
import transactionTest
import jobTests
import projectTests
import projectJobTests
import supportTests
import tasksTests

import time
import newFileOpen
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import os

# Initialize the WebDriver
chrome_driver_path = r'C:/webdrivers/chromedriver.exe'  # Adjust the path as necessary
service = Service(chrome_driver_path)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # Uncomment for headless mode
#chrome_options.add_argument('--start-maximized')

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://wsmanybuild.azurewebsites.net/Swagger/index.html")

# Function to perform authorization
def authorize(driver, timeout=15):
    wait = WebDriverWait(driver, timeout)
    
    try:
        # Click the login button
        time.sleep(.25)
        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.opblock-summary-control")))
        login_button.click()

        # Click the "Try it out" button
        try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
        try_it_out_button.click()

        # Enter login details
        text_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[class*='body-param']")))
        text_field.clear()
        text_to_write = '{"userName": "HDouglas+doer3@method-automation.com", "password": "#########"}'
        text_field.send_keys(text_to_write)

        # Execute login
        execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
        execute_button.click()

        # Wait for the response and download the key
        download = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"download-contents")))
        download.click()

        download = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='operations-Auth-post_api_Auth_Login']/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[2]/div[1]/div/button")))
        download.click()

        # Open the new file to get the key
        key = newFileOpen.openNewFile()

        # Authorize with the obtained key
        authorize_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.authorize.unlocked")))
        authorize_button.click()

        time.sleep(1)
        key_input_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input")))
        key_input_field.send_keys("Bearer " + key)

        final_press_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.modal-btn.auth.authorize.button")))
        final_press_button.click()

        # Check if authorization was successful
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.authorize.locked")))

        close = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.modal-btn.auth.btn-done.button")))
        close.click()

        close_open_tab = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.opblock-summary-control")))
        close_open_tab.click()
        time.sleep(2)

        print("Authorization was successful")
        return True

    except TimeoutException:
        print("Element not found within the given time frame")
        return False
    except Exception as e:
        print("Authorization failed: ", str(e))
        return False

# Main script execution
try:
    # Authorize once
    if authorize(driver):
        print("Authorization successful, running tests...")
        # Run the tests for the user GETs
        
        try:
            userCheck = userForHomeComputer.userTests(driver)  # Pass the driver instance
        except Exception as e:
            print(f"An error occurred during userForHomeComputer.userTests: {e}")

        # Run profile tests
        try:
            profileCheck = profileTests.runProfile(driver)  # Pass the driver instance
        except Exception as e:
            print(f"An error occurred during profileTests.runProfile: {e}")
        
        # Run jigx get test
        try:
            jixCheck = jigxTest.runJigTest(driver)  # Pass the driver instance
        except Exception as e:
            print(f"An error occurred during jigxTest.runJigTest: {e}")

        try:
            chatCheck = chatTests.chatGET_Tests(driver)  # Pass the driver instance
        except Exception as e:
            print(f"An error occurred during chatTests.chatGET_Tests: {e}")

        try:    
            lookupCheck = lookupTests.lookupTests(driver)  # Pass the driver instance
        except Exception as e:
            print(f"An error occurred during lookupTests.lookupTests: {e}")

        try:
            healthCheck = healthTests.healthTestRun(driver)
        except Exception as e:
            print(f"An error occurred during healthTests.healthTestRun: {e}")

        try:
            BidCheck = BidTests.bidTestsRunner(driver)
        except Exception as e:
            print(f"An error occurred during BidTests.bidTestsRunner: {e}")
            
        try:
            changeOrderCheck = changeOrderTests.change_order_runner(driver)
        except Exception as e:
            print(f"An error occurred during changeOrderTests.change_order_runner: {e}")

        try:
            contractCheck = ContractTests.contract_tests_runner(driver)
        except Exception as e:
            print(f"An error occurred during ContractTests.contract_tests_runner: {e}")

        try:
            dealACheck = DealAnalyzerTests.DealRunner(driver)
        except Exception as e:
            print(f"An error occurred during DealAnalyzerTests.DealRunner: {e}")

        try:
            disciplineCheck = Discipline.Disicpline_runner(driver)
        except Exception as e:
            print(f"An error occurred during Discipline.discipline_runner: {e}")

        try:
            pbCheck = project_bid_tests.project_bid_runner(driver)
        except Exception as e:
            print(f"An error occurred during project_bid_tests.project_bid_runner: {e}")
        
        try:
            docCheck = document_tests.doc_runner(driver)
        except Exception as e:
            print(f"An error occurred during document_tests.doc_runner: {e}")

        try:
            milestoneCheck = milestoneTests.milestone_runner(driver)
        except Exception as e:
            print(f"An error occurred during milestoneTests.milestone_runner")

        try:
            termsheetCheck = termsheetTest.terms_runner(driver)
        except Exception as e:
            print(f"An error occurred during termsheetTest.terms_runner")
        
        try:
            transactionCheck = transactionTest.transaction_runner(driver)
        except Exception as e:
            print(f"An error occurred during transactionTest.transaction_runner")
        
        try:
            jobCheck = jobTests.Job_runner(driver)
        except Exception as e:
            print(f"An error occurred during JobTests.Job_runner")
        
        try:
            projectTests.project_runner(driver)
        except Exception as e:
            print(f"An error occurred during projectTests.project_runner")

        try:
            projectJobTests.project_job_runner(driver)
        except Exception as e:
            print(f"An error occurred during projectJobTests.project_job_runner")

        try:
            supportTests.support_runner(driver)
        except Exception as e:
            print(f"An error occurred during supportTests.support_runner")
        
        try:
            tasksTests.task_runner(driver)
        except Exception as e:
            print(f"An error occurred during tasksTests.task_runner")


        '''
        #Use for next version

        if(userCheck == 200 and profileCheck == 200 and jixCheck == 200 and chatCheck == 200 and lookupCheck == 200 and healthCheck == 200 and BidCheck == 200 and changeOrderCheck == 200 and contractCheck == 200 and dealACheck == 200 and disciplineCheck == 200 and pbCheck == 200 and docCheck == 200 and milestoneCheck == 200 and termsheetCheck == 200 and transactionCheck == 200 and jobCheck == 200):
            print("All tests passed")
        else:
            print("Some tests failed, rerun or fix code before deployment")
        
        '''


    else:
        print("Authorization failed, tests will not be run.")

finally:
    # Close the driver
    driver.quit()
