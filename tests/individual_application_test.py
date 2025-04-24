import time
import os
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from config.locators import locators
from config.locators import branches
from config.locators import application_types
from config.settings import BASE_URL

logging.basicConfig(filename="../logs/test_logs.log", level=logging.INFO)

fake_email = input("\nPlease enter your email: ")
fake_tin = input("TIN: ")

def test_loan_application(browser, fake_user):
    # Unpack returned values
    fake_profile, fake_fname, fake_lname, fake_gender, fake_company, fake_dob, fake_phone, fake_sss, fake_branchChoice, fake_application_type, fake_salutation = fake_user
    driver, wait, longwait = browser

    driver.get(BASE_URL)

    #logging.info("Starting test...")

    start_application(driver, wait, fake_branchChoice)

    get_application_otp(driver, wait, fake_fname, fake_lname, fake_gender, fake_dob, fake_sss, fake_email, fake_phone) 

    input("Press enter to close..")
    
    submit_sblaf_form(driver, wait, longwait, fake_application_type, fake_salutation, fake_company, fake_tin)
    
    #submit_application()

    '''
    try:
        assert 1 == 1
        logging.info("Test passed!")
        print("Test passed!")
    except AssertionError:
        logging.error("Test failed!")
        print("Test failed!")
    '''


def start_application(driver, wait, fake_branchChoice):
    startApplicationBtn = wait.until(EC.presence_of_element_located((By.XPATH, locators["startApplicationBtn"])))
    startApplicationBtn.click()

    branchList = wait.until(EC.presence_of_element_located((By.XPATH, locators["branchList"])))
    branchList.click()
    time.sleep(1)

    branchChoice = wait.until(EC.presence_of_element_located((By.XPATH, branches[f"{fake_branchChoice}"])))
    time.sleep(1)

    driver.execute_script("arguments[0].scrollIntoView(true);", branchChoice)
    branchChoice.click()

    driver.execute_script("displayForm(5, 'NEXT');")

    creditProgramChoice = wait.until(EC.presence_of_element_located((By.ID, locators["creditProgramChoice"])))
    creditProgramChoice.click()

    driver.execute_script("displayForm(2, 'NEXT');")

    customerTypeChoice = wait.until(EC.presence_of_element_located((By.ID, locators["customerTypeChoice"])))
    customerTypeChoice.click()

    driver.execute_script("displayForm(3, 'NEXT');")

    consentCheckboxChoice = wait.until(EC.presence_of_element_located((By.ID, locators["consentCheckboxChoice"])))
    consentCheckboxChoice.click()

    driver.execute_script("displayForm(6, 'NEXT');")

def get_application_otp(driver, wait, fake_fname, fake_lname, fake_gender, fake_dob, fake_sss, fake_email, fake_phone): 
    firstNameField = wait.until(EC.presence_of_element_located((By.ID, locators["firstNameField"])))
    firstNameField.send_keys(fake_fname)

    lastNameField = wait.until(EC.presence_of_element_located((By.ID, locators["lastNameField"])))
    lastNameField.send_keys(fake_lname)

    idTypeList = wait.until(EC.presence_of_element_located((By.XPATH, locators["idTypeList"])))
    idTypeList.click()
    
    idTypeChoice = wait.until(EC.presence_of_element_located((By.XPATH, locators["idTypeChoice"])))
    driver.execute_script("arguments[0].scrollIntoView(true);", idTypeChoice)
    idTypeChoice.click()

    idNumberField = driver.find_element(By.XPATH, locators["idNumberField"])
    idNumberField.send_keys(fake_sss)

    birthDateField = wait.until(EC.presence_of_element_located((By.ID, locators["birthDateField"])))
    birthDateField.send_keys(fake_dob)
    
    sexList = wait.until(EC.presence_of_element_located((By.XPATH, locators["sexList"])))
    sexList.click()

    if fake_gender == "F":
        sexChoiceValue = '[data-value="M"]'
    else:
        sexChoiceValue = locators["sexChoice"]
            
    sexChoice = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, sexChoiceValue)))
    driver.execute_script("arguments[0].scrollIntoView(true);", sexChoice) 
    sexChoice.click()

    mobileNoField = driver.find_element(By.ID, locators["mobileNoField"])

    mobileNoField.send_keys(fake_phone)

    emailField = driver.find_element(By.ID, locators["emailField"])
    emailField.send_keys(fake_email)

    driver.execute_script("goManualForm();")

def submit_sblaf_form(driver, wait, longwait, application_type, salutation, company, tin):
    time.sleep(30)
    print(application_types[f"{application_type}"])
    
    applicationType = driver.find_element(By.ID, application_types[f"{application_type}"])
    applicationType.click()
    
    #applicationType = longwait.until(EC.presence_of_element_located((By.XPATH, application_types[f"{application_type}"])))
    
    tinField = wait.until(EC.presence_of_element_located((By.XPATH, locators["tinField"])))
    driver.execute_script("arguments[0].scrollIntoView(true);", tinField)
    time.sleep(1)
    tinField.send_keys(tin)
   
    #dropdown = driver.find_element(By.XPATH, locators["salutationList"])
    #select = Select(dropdown)
    #select.select_by_visible_text(salutation)
    
