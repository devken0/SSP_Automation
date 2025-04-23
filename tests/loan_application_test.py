import time
import os
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from config.locators import locators
from config.locators import branches
from config.settings import BASE_URL

logging.basicConfig(filename="../logs/test_logs.log", level=logging.INFO)

fake_email = input("\nPlease enter your email: ")

def test_loan_application(browser, fake_user):
    fake_profile, fake_fname, fake_lname, fake_gender, fake_company, fake_dob, fake_phone, fake_sss = fake_user
    logging.info("Starting test...")
    driver, wait = browser # Unpack returned values

    driver.get(BASE_URL)

    startApplicationBtn = wait.until(EC.presence_of_element_located((By.XPATH, locators["startApplicationBtn"])))
    startApplicationBtn.click()

    branchList = wait.until(EC.presence_of_element_located((By.XPATH, locators["branchList"])))
    branchList.click()

    branchChoice = wait.until(EC.presence_of_element_located((By.XPATH, branches["CEBU BUSINESS PARK"])))

    driver.execute_script("arguments[0].scrollIntoView(true);", branchChoice)
    time.sleep(1)
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

    firstNameField = wait.until(EC.presence_of_element_located((By.ID, locators["firstNameField"])))
    firstNameField.send_keys(fake_fname)

    lastNameField = wait.until(EC.presence_of_element_located((By.ID, locators["lastNameField"])))
    lastNameField.send_keys(fake_lname)

    idTypeList = wait.until(EC.presence_of_element_located((By.XPATH, locators["idTypeList"])))
    idTypeList.click()

    idTypeChoice = wait.until(EC.presence_of_element_located((By.XPATH, locators["idTypeChoice"])))
    driver.execute_script("arguments[0].scrollIntoView(true);", idTypeChoice)
    idTypeChoice.click()
    time.sleep(1)

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

    input("\nPress Enter to close the browser")
    '''
    try:
        assert 1 == 1
        logging.info("Test passed!")
        print("Test passed!")
    except AssertionError:
        logging.error("Test failed!")
        print("Test failed!")
    '''
