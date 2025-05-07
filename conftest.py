import os
import time
import pytest
import logging
import importlib
import config.settings
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

faker = Faker("en_PH")
profile = faker.profile()
gender = profile["sex"]
settings_file_path = "config/settings.py"
branches_file_path = "data/branches.txt"

def update_config_value(setting_name, new_value):
    with open(settings_file_path, "r") as file:
        lines = file.readlines()
    
    with open(settings_file_path, "w") as file:
        for line in lines:
            if line.startswith(setting_name):
                file.write(f'{setting_name} = "{new_value}"\n')
                print(f"{setting_name} updated successfully.")
            else:
                file.write(line)

def pytest_runtest_setup():
    importlib.reload(config.settings)
    print(f"\n\nUpdated values:\nSpouse Email: {config.settings.DEFAULT_SPOUSE_EMAIL}\nPhone: {config.settings.DEFAULT_PHONE}\nBranch: {config.settings.DEFAULT_BRANCH}")

@pytest.fixture
def new_application():
    os.system("wmctrl -a Terminal")
    email = input("\nPlease enter your email: ")
    password = config.settings.DEFAULT_PASSWORD
    choice = input(f"Use default spouse email {config.settings.DEFAULT_SPOUSE_EMAIL}? (Y/n)").strip().lower()
    if not choice or choice == "y": spouse_email = config.settings.DEFAULT_SPOUSE_EMAIL
    else: 
        spouse_email = input("New spouse email: ").strip()
        update_config_value("DEFAULT_SPOUSE_EMAIL", spouse_email)
    choice = input(f"Use default phone number {config.settings.DEFAULT_PHONE}? (Y/n)").strip().lower()
    if not choice or choice == "y": phone = config.settings.DEFAULT_PHONE
    else: 
        phone = input("New phone number: ").strip()
        update_config_value("DEFAULT_PHONE", phone)
    choice = input(f"Use default branch {config.settings.DEFAULT_BRANCH}? (Y/n)").strip().lower()
    if not choice or choice == "y": branch = config.settings.DEFAULT_BRANCH
    else: 
        os.system(f"cat {branches_file_path}") 
        print("Please find the exact name of your branch above.")
        branch = input("New branch: ").strip()
        update_config_value("DEFAULT_BRANCH", branch)
    #choice = input("Preview SBLAF Form? (Y/n)").strip().lower()
    #if not choice or choice == "y": auto_submit = False
    #else: auto_submit = True; print("Application will be submitted automatically.")
    auto_submit = ""
    print("Starting browser...")
    time.sleep(2)
    return (
        email, password, auto_submit, phone, branch
    )

@pytest.fixture
def browser():
    service = Service(config.settings.CHROMEDRIVER_PATH)
    options = Options()
    options.BinaryLocation = config.settings.CHROMIUM_PATH
    options.add_argument('--ignore-certificate-errors') # Ignore SSL errors
    #options.add_argument('--disable-web-security')  # Optional: Disable web security (use cautiously)
    options.add_argument('--allow-running-insecure-content')  # Allow insecure content

    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, config.settings.WAIT_DURATION)
    longwait = WebDriverWait(driver, 999999)

    yield driver, wait, longwait # Returns both driver and wait
    driver.quit()

@pytest.fixture
def generate_fake_user():
    first_name = faker.first_name_female() if gender == 'F' else faker.first_name_male()
    last_name = faker.last_name_female() if gender == 'F' else faker.last_name_male()
    birthdate = faker.date_of_birth()
    formatted_birthdate = birthdate.strftime("%m/%d/%Y")
    company = profile["company"]
    company = f"ITGOJT {company}"
    phone = "09765104860"
    sss_number = f"{faker.random_int(10, 99)}-{faker.random_int(1000000, 9999999)}-{faker.random_int(0, 9)}"
    tin = f"{faker.random_int(100000000, 999999999)}"
    branch = "BGC-10TH AVENUE"
    application_type = "New Application"
    salutation = "Mister" if gender == "M" else "Miss"
    civil_status = "MARRIED"
    province = "METRO MANILA"
    city = "PASAY CITY"
    years_in_operation = "17"
    website = "www.testingatpnb.com"
    nature_of_business = "Information & Communication"
    specific_business = "Other information technology and computer service activities"
    business_addr_ownership = "Owned (mortgaged)"
    business_reg_type = "Others (Please specify)"
    business_reg_type_others = "SEC"
    date_of_registration = "01/20/2025"
    date_of_expiry = "01/20/2030"
    business_reg_number = "SEC0185762"
    firm_size = ""
    loan_amount = "15000000"
    tenor = "24"
    payment_freq = "Annually"
    loan_facility = "Credit Line"
    loan_type = ""
    
    return (
        first_name, last_name, gender, company, formatted_birthdate,
        sss_number, tin, application_type, salutation,
        civil_status, province, city, years_in_operation, website,
        nature_of_business, specific_business, business_addr_ownership, business_reg_type, business_reg_type_others, date_of_registration,
        date_of_expiry, business_reg_number, firm_size, loan_amount,
        tenor, payment_freq, loan_facility, loan_type
        )

@pytest.fixture
def generate_fake_mother():
    first_name = faker.first_name_female()
    last_name = faker.last_name_female()
    
    return (
        first_name, last_name
        )

@pytest.fixture
def generate_fake_spouse():
    first_name = faker.first_name_female() if gender == 'M' else faker.first_name_male()
    last_name = faker.last_name_female() if gender == 'M' else faker.last_name_male()
    birthdate = faker.date_of_birth()
    formatted_birthdate = birthdate.strftime("%m/%d/%Y")
    email = config.settings.DEFAULT_SPOUSE_EMAIL
    return (
        first_name, last_name, formatted_birthdate, email
        )

@pytest.fixture
def generate_fake_file():
    attachment_name = "TESTING"
    file_name = "/home/user01/Music/Test.pdf"
    return attachment_name, file_name
    



