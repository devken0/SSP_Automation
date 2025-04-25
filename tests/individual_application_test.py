import time
import os
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from config.locators import locators
from config.locators import branches
from config.locators import application_types
from config.settings import BASE_URL

logging.basicConfig(filename="../logs/test_logs.log", level=logging.INFO)
fake_email = input("\nPlease enter your email: ")
fake_tin = input("TIN: ")

def test_loan_application(browser, fake_user, fake_spouse, fake_mother):
    # Unpack returned values
    '''
    profile, first_name, last_name, gender, company, formatted_birthdate,
    phone, sss_number, branch, application_type, salutation,
    civil_status, province, city, years_in_operation, website,
    nature_of_business, business_reg_type, date_of_registration,
    date_of_expiry, business_reg_number, firm_size, loan_amount,
    tenor, payment_freq, loan_facility, loan_type
    '''
    (fake_profile, fake_fname, fake_lname, fake_gender, fake_company, fake_dob, fake_phone, fake_sss, fake_branchChoice,
     fake_application_type, fake_salutation,fake_civilStatus, fake_province, fake_city, fake_yrsInOps, fake_website,
     fake_nob, fake_regType, fake_dateOfReg, fake_dateOfExp, fake_regNum, fake_firmSize, fake_loanAmount,
     fake_tenor, fake_paymentFreq, fake_loanFacility, fake_loanType) = fake_user
    (fake_spouse_fname, fake_spouse_lname, fake_spouse_dob, fake_spouse_email) = fake_spouse
    (fake_mother_fname, fake_mother_lname) = fake_mother
    driver, wait, longwait = browser

    driver.get(BASE_URL)

    #logging.info("Starting test...")

    start_application(driver, wait, fake_branchChoice)

    get_application_otp(driver, wait, fake_fname, fake_lname, fake_gender, fake_dob, fake_sss, fake_email, fake_phone) 

    input("\nPress Enter to continue")
    
    submit_sblaf_form(
        driver, wait, longwait, fake_application_type, fake_salutation, fake_company, fake_tin, fake_civilStatus, fake_province, fake_city,
        fake_yrsInOps, fake_website, fake_nob, fake_regType, fake_dateOfReg, fake_dateOfExp, fake_regNum, fake_firmSize, fake_loanAmount,
        fake_tenor, fake_paymentFreq, fake_loanFacility, fake_loanType, fake_spouse_fname, fake_spouse_lname, fake_spouse_dob, fake_spouse_email,
        fake_mother_fname, fake_mother_lname
        )
    
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

def click_element(driver, by, elementType, wait=False, scrollIntoView=False, branch=False):
    if wait != False:
        try:
            element = wait.until(EC.presence_of_element_located((by, elementType)))
            
            if scrollIntoView:
                driver.execute_script("arguments[0].scrollIntoView(true);", element)

            element.click()
            return 
        except Exception as e:
            print(f"Error clicking element: {e}")
            return
    try:
        element = driver.find_element(by, elementType)
        if scrollIntoView:
            driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
    except Exception as e:
        print(f"Error clicking element: {e}")
        
def send_keys_to_element(driver, by, elementType, keys, wait=False, scrollIntoView=False):
    if wait != False:
        try:
            element = wait.until(EC.presence_of_element_located((by, elementType)))
            if scrollIntoView:
                driver.execute_script("arguments[0].scrollIntoView(true);", element)
            element.send_keys(keys)
            return
        except Exception as e:
            print(f"Error sending keys to element: {e}")
            return
    try:
        element = driver.find_element(by, elementType)
        if scrollIntoView:
            driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.send_keys(keys)
    except Exception as e:
        print(f"Error sending keys to element: {e}")
    
def start_application(driver, wait, fake_branchChoice):  
    click_element(driver, By.XPATH, locators["startApplicationBtn"], wait=wait)
    click_element(driver, By.XPATH, locators["branchList"], wait=wait)
    time.sleep(1)
    click_element(driver, By.XPATH, branches[f"{fake_branchChoice}"], wait=wait, scrollIntoView=True, branch=fake_branchChoice)
    driver.execute_script("displayForm(5, 'NEXT');")
    click_element(driver, By.ID, locators["creditProgramChoice"], wait=wait)
    driver.execute_script("displayForm(2, 'NEXT');")
    click_element(driver, By.ID, locators["customerTypeChoice"], wait=wait)
    driver.execute_script("displayForm(3, 'NEXT');")
    click_element(driver, By.ID, locators["consentCheckboxChoice"], wait=wait)
    driver.execute_script("displayForm(6, 'NEXT');")

def get_application_otp(driver, wait, fake_fname, fake_lname, fake_gender, fake_dob, fake_sss, fake_email, fake_phone):
    #send_keys_to_element(driver, wait, fake_fname, fake_lname, fake_gender, fake_dob, fake_sss, fake_email, fake_phone)
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

    '''
    profile, first_name, last_name, gender, company, formatted_birthdate,
    phone, sss_number, branch, application_type, salutation,
    civil_status, province, city, years_in_operation, website,
    nature_of_business, business_reg_type, date_of_registration,
    date_of_expiry, business_reg_number, firm_size, loan_amount,
    tenor, payment_freq, loan_facility, loan_type
    '''
    
def submit_sblaf_form(
    driver, wait, longwait, application_type, salutation, company, tin, civilStatus, province, city,
    years_in_operation, website, nature_of_business, business_reg_type, date_of_registration,
    date_of_expiry, business_reg_number, firm_size, loan_amount, tenor, payment_freq,
    loan_facility, loan_type, spouse_fname, spouse_lname, spouse_dob, spouse_email,
    mother_fname, mother_lname
    ):
    
    iframe = longwait.until(EC.presence_of_element_located((By.ID, "productDetailsFrame")))
    driver.switch_to.frame(iframe)
    
    applicationType = driver.find_element(By.XPATH, application_types[f"{application_type}"])
    applicationType.click()

    salutationList = driver.find_element(By.XPATH, locators["salutationList"])
    select = Select(salutationList)
    select.select_by_visible_text(salutation)
    
    civilStatusList = driver.find_element(By.XPATH, locators["civilStatusList"])
    select = Select(civilStatusList)
    select.select_by_visible_text(civilStatus)
    
    pobProvinceList = driver.find_element(By.XPATH, locators["pobProvinceList"])
    select = Select(pobProvinceList)
    select.select_by_visible_text(province)
    
    pobCityList = driver.find_element(By.XPATH, locators["pobCityList"])
    select = Select(pobCityList)
    select.select_by_visible_text(city)
    
    tinField = wait.until(EC.presence_of_element_located((By.XPATH, locators["tinField"])))
    
    driver.execute_script("arguments[0].scrollIntoView(true);", tinField)
    #time.sleep(1)
    tinField.send_keys(tin)
    
    send_keys_to_element(driver, By.XPATH, locators["spouseFirstNameField"], spouse_fname, scrollIntoView=True)
    send_keys_to_element(driver, By.XPATH, locators["spouseLastNameField"], spouse_lname)
    send_keys_to_element(driver, By.XPATH, locators["spouseDob"], spouse_dob)
    send_keys_to_element(driver, By.XPATH, locators["spouseEmail"], spouse_email)
    
    send_keys_to_element(driver, By.XPATH, locators["motherFirstNameField"], mother_fname, scrollIntoView=True)
    send_keys_to_element(driver, By.XPATH, locators["motherLastNameField"], spouse_lname)


    
    input("Press Enter to continue")
    
    send_keys_to_element(driver, By.XPATH, locators["spouseEmail"], fake_)
    
    driver.switch_to.default_content() # switch back to the main page once done
    
    #upload_sblaf_docs()
    
    #submit()
    
def upload_sblaf_docs():
    input("Press Enter to continue")
    


