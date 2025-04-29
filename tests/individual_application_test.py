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
from config.locators import iframes
from config.settings import BASE_URL

logging.basicConfig(filename="../logs/test_logs.log", level=logging.INFO)
fake_email = input("\nPlease enter your email: ")
fake_tin = input("TIN: ")

def test_loan_application(browser, generate_fake_user, generate_fake_spouse, generate_fake_mother, generate_fake_file):
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
     fake_nob, fake_specific_business, fake_business_addr_ownership, fake_regType, fake_regTypeOthers, fake_dateOfReg, fake_dateOfExp, fake_regNum, fake_firmSize, fake_loanAmount,
     fake_tenor, fake_paymentFreq, fake_loanFacility, fake_loanType) = generate_fake_user
    (fake_spouse_fname, fake_spouse_lname, fake_spouse_dob, fake_spouse_email) = generate_fake_spouse
    (fake_mother_fname, fake_mother_lname) = generate_fake_mother
    fake_attachment_name, fake_file_name = generate_fake_file
    driver, wait, longwait = browser

    driver.get(BASE_URL)

    #logging.info("Starting test...")

    start_application(driver, wait, fake_branchChoice)

    get_application_otp(driver, wait, fake_fname, fake_lname, fake_gender, fake_dob, fake_sss, fake_email, fake_phone)
    
    submit_sblaf_form(
        driver, wait, longwait, fake_application_type, fake_salutation, fake_company, fake_tin, fake_civilStatus, fake_province, fake_city,
        fake_yrsInOps, fake_website, fake_nob, fake_specific_business, fake_business_addr_ownership, fake_regType, fake_regTypeOthers, fake_dateOfReg, fake_dateOfExp, fake_regNum, fake_firmSize, fake_loanAmount,
        fake_tenor, fake_paymentFreq, fake_loanFacility, fake_loanType, fake_spouse_fname, fake_spouse_lname, fake_spouse_dob, fake_spouse_email,
        fake_mother_fname, fake_mother_lname, fake_attachment_name, fake_file_name
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
            if scrollIntoView: scroll_into_view(driver, element)
            element.click()
            return 
        except Exception as e:
            print(f"Error clicking element: {e}")
            return
    try:
        element = driver.find_element(by, elementType)
        if scrollIntoView: scroll_into_view(driver, element)
        element.click()
    except Exception as e:
        print(f"Error clicking element: {e}")
        
def send_keys_to_element(driver, by, elementType, keys, wait=False, scrollIntoView=False):
    if wait != False:
        try:
            element = wait.until(EC.presence_of_element_located((by, elementType)))
            if scrollIntoView: scroll_into_view(driver, element)
            element.send_keys(keys)
            return
        except Exception as e:
            print(f"Error sending keys to element: {e}")
            return
    try:
        element = driver.find_element(by, elementType)
        if scrollIntoView: scroll_into_view(driver, element)
        element.send_keys(keys)
    except Exception as e:
        print(f"Error sending keys to element: {e}")

def select_element(driver, by, elementType, selectText, wait=False, scrollIntoView=False):
    if wait != False:
        try:
            element = wait.until(EC.presence_of_element_located((by, elementType)))
            if scrollIntoView: scroll_into_view(driver, element)
            select = Select(element)
            select.select_by_visible_text(selectText)
            return
        except Exception as e:
            print(f"Error sending keys to element: {e}")
            return
    try:
        element = driver.find_element(by, elementType)
        if scrollIntoView: scroll_into_view(driver, element)
        select = Select(element)
        select.select_by_visible_text(selectText)
    except Exception as e:
        print(f"Error sending keys to element: {e}")

def switch_to_iframe(driver, by, elementType, wait=False, scrollIntoView=False):
    if wait != False:
        try:
            element = wait.until(EC.presence_of_element_located((by, elementType)))
            if scrollIntoView: scroll_into_view(driver, element)
            driver.switch_to.frame(element)
            return
        except Exception as e:
            print(f"Error sending keys to element: {e}")
            return
    try:
        element = driver.find_element(by, elementType)
        if scrollIntoView: scroll_into_view(driver, element)
        driver.switch_to.frame(element)
    except Exception as e:
        print(f"Error sending keys to element: {e}")
        
def scroll_into_view(driver, element=False, by=False, elementType=False):
    if not element:
        element = driver.find_element(by, elementType)
    driver.execute_script("arguments[0].scrollIntoView(true);", element)

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
    years_in_operation, website, nature_of_business, specific_business, business_addr_ownership,
    business_reg_type, business_reg_type_others, date_of_registration,
    date_of_expiry, business_reg_number, firm_size, loan_amount, tenor, payment_freq,
    loan_facility, loan_type, spouse_fname, spouse_lname, spouse_dob, spouse_email,
    mother_fname, mother_lname, attachment_name, file_name
    ):
    
    switch_to_iframe(driver, By.ID, iframes["sblaf_main_iframe"], wait=longwait)
    
    click_element(driver, By.XPATH, application_types[f"{application_type}"], wait=wait)
    select_element(driver, By.XPATH, locators["salutationList"], salutation, wait=wait, scrollIntoView=True)
    select_element(driver, By.XPATH, locators["civilStatusList"], civilStatus, wait=wait)
    select_element(driver, By.XPATH, locators["pobProvinceList"], province, wait=wait)
    select_element(driver, By.XPATH, locators["pobCityList"], city, wait=wait)
    send_keys_to_element(driver, By.XPATH, locators["tinField"], tin, wait=wait)
    send_keys_to_element(driver, By.XPATH, locators["spouseFirstNameField"], spouse_fname, wait=wait, scrollIntoView=True)
    send_keys_to_element(driver, By.XPATH, locators["spouseLastNameField"], spouse_lname, wait=wait)
    send_keys_to_element(driver, By.XPATH, locators["spouseDob"], spouse_dob, wait=wait)
    send_keys_to_element(driver, By.XPATH, locators["spouseEmail"], spouse_email, wait=wait)
    send_keys_to_element(driver, By.XPATH, locators["motherFirstNameField"], mother_fname, wait=wait, scrollIntoView=True)
    send_keys_to_element(driver, By.XPATH, locators["motherLastNameField"], spouse_lname, wait=wait)
    select_element(driver, By.XPATH, locators["provinceList"], province, wait=wait, scrollIntoView=True)
    select_element(driver, By.XPATH, locators["cityList"], city, wait=wait)
    click_element(driver, By.XPATH, locators["homeOwnershipButton"], wait=wait)
    send_keys_to_element(driver, By.XPATH, locators["businessNameField"], company, wait=wait, scrollIntoView=True)
    send_keys_to_element(driver, By.XPATH, locators["yearBusinessField"], years_in_operation, wait=wait)
    send_keys_to_element(driver, By.XPATH, locators["socialMediaField"], website, wait=wait)
    select_element(driver, By.XPATH, locators["natureBusinessList"], nature_of_business, wait=wait)
    select_element(driver, By.XPATH, locators["specifyBusinessList"], specific_business, wait=wait)
    click_element(driver, By.XPATH, locators["similarhomeAddressButton"], wait=wait, scrollIntoView=True)
    select_element(driver, By.XPATH, locators["businessaddressOwnership"], business_addr_ownership, wait=wait)
    select_element(driver, By.XPATH, locators["businessRegistrationList"], business_reg_type, wait=wait)
    send_keys_to_element(driver, By.XPATH, locators["businessRegistrationOthers"], business_reg_type_others, wait=wait)
    send_keys_to_element(driver, By.XPATH, locators["dateRegistrationField"], date_of_registration, wait=wait)
    send_keys_to_element(driver, By.XPATH, locators["expiryRegistrationField"], date_of_expiry, wait=wait)
    send_keys_to_element(driver, By.XPATH, locators["registrationNumberField"], business_reg_number, wait=wait)
    click_element(driver, By.XPATH, locators["firmSizeButton"], wait=wait, scrollIntoView=True)
    click_element(driver, By.XPATH, locators["repaymentofLoans"], wait=wait, scrollIntoView=True)
    click_element(driver, By.XPATH, locators["addROLButton"], wait=wait)
    send_keys_to_element(driver, By.XPATH, locators["loanAmountField"], loan_amount, wait=wait, scrollIntoView=True)
    send_keys_to_element(driver, By.XPATH, locators["tenorField"], tenor, wait=wait)
    select_element(driver, By.XPATH, locators["proposedRepaymentList"], payment_freq, wait=wait)
    select_element(driver, By.XPATH, locators["loanFacilityList"], loan_facility, wait=wait)
    click_element(driver, By.XPATH, locators["loanPurposeList"], wait=wait)
    click_element(driver, By.XPATH, locators["addloanPurposeButton"], wait=wait)
    click_element(driver, By.XPATH, locators["typeofLoanButton"], wait=wait)
    
    scroll_into_view(driver, by=By.XPATH, elementType=locators["documentChecklist"])
    
    driver.execute_script("createAmlKyc('CTY000000253');")
    switch_to_iframe(driver, By.XPATH, iframes["upload_document_iframe"], wait=wait)
    time.sleep(2)
    send_keys_to_element(driver, By.NAME, locators["attachmentNameField"], attachment_name, wait=wait)
    send_keys_to_element(driver, By.ID, locators["fileUploadButton"], file_name, wait=wait)
    driver.execute_script("performAction('create_document_checklist_att');")
    time.sleep(1)
    driver.switch_to.parent_frame()

    driver.execute_script("createAmlKyc('CTY000000255');")
    switch_to_iframe(driver, By.XPATH, iframes["upload_document_iframe"], wait=wait)
    time.sleep(2)
    send_keys_to_element(driver, By.NAME, locators["attachmentNameField"], attachment_name, wait=wait)
    send_keys_to_element(driver, By.ID, locators["fileUploadButton"], file_name, wait=wait)
    driver.execute_script("performAction('create_document_checklist_att')")
    time.sleep(1)
    driver.switch_to.parent_frame()

    driver.execute_script("createAmlKyc('CTY000000257');")
    switch_to_iframe(driver, By.XPATH, iframes["upload_document_iframe"], wait=wait)
    time.sleep(2)
    send_keys_to_element(driver, By.NAME, locators["attachmentNameField"], attachment_name, wait=wait)
    send_keys_to_element(driver, By.ID, locators["fileUploadButton"], file_name, wait=wait)
    driver.execute_script("performAction('create_document_checklist_att')")
    time.sleep(1)
    driver.switch_to.parent_frame()

    driver.execute_script("createAmlKyc('CTY000000015');")
    switch_to_iframe(driver, By.XPATH, iframes["upload_document_iframe"], wait=wait)
    time.sleep(2)
    send_keys_to_element(driver, By.NAME, locators["attachmentNameField"], attachment_name, wait=wait)
    send_keys_to_element(driver, By.ID, locators["fileUploadButton"], file_name, wait=wait)
    driver.execute_script("performAction('create_document_checklist_att')")
    time.sleep(1)
    driver.switch_to.parent_frame()
    
    driver.execute_script("createAmlKyc('CTY000000243');")
    switch_to_iframe(driver, By.XPATH, iframes["upload_document_iframe"], wait=wait)
    time.sleep(2)
    send_keys_to_element(driver, By.NAME, locators["attachmentNameField"], attachment_name, wait=wait)
    send_keys_to_element(driver, By.ID, locators["fileUploadButton"], file_name, wait=wait)
    driver.execute_script("performAction('create_document_checklist_att')")
    time.sleep(1)
    driver.switch_to.parent_frame()
    
    driver.execute_script("createAmlKyc('CTY000000256');")
    switch_to_iframe(driver, By.XPATH, iframes["upload_document_iframe"], wait=wait)
    time.sleep(2)
    send_keys_to_element(driver, By.NAME, locators["attachmentNameField"], attachment_name, wait=wait)
    send_keys_to_element(driver, By.ID, locators["fileUploadButton"], file_name, wait=wait)
    driver.execute_script("performAction('create_document_checklist_att')")
    time.sleep(1)
    driver.switch_to.parent_frame()
    
    driver.execute_script("performHpForm('Save');")
    click_element(driver, By.XPATH, locators["okayButton"], wait=wait)
    click_element(driver, By.XPATH, locators["previewButton"], wait=wait)
    
    if auto_submit:
        click_element(driver, By.XPATH, locators["submitButton"], wait=wait, scrollIntoView=True)
    else:
        click_element(driver, By.XPATH, locators["submitButton"], wait=longwait, scrollIntoView=True)
    
    click_element(driver, By.XPATH, locators["showESGButton"], wait=wait)
    click_element(driver, By.XPATH, locators["submitESGButton"], wait=wait, scrollIntoView=True)
    
    time.sleep(2)
        
    #send_keys_to_element(driver, By.XPATH, locators["spouseEmail"], fake_)
    
    #driver.switch_to.default_content() # exit all frames completely
    
    #upload_sblaf_docs()
    
    #submit()
    #driver.execute_script("submitPage();")

def login_form():
    print(f"\n")
    input("Press Enter to close...")


def upload_sblaf_docs():
    input("Press Enter to continue")
    


