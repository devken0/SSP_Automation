import pytest
import logging
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from config.settings import CHROMEDRIVER_PATH, CHROMIUM_PATH, WAIT_DURATION

faker = Faker("en_PH")
fake_user_gender = ""

@pytest.fixture
def browser():
    service = Service(CHROMEDRIVER_PATH)
    options = Options()
    options.BinaryLocation = CHROMIUM_PATH
    options.add_argument('--ignore-certificate-errors') # Ignore SSL errors
    #options.add_argument('--disable-web-security')  # Optional: Disable web security (use cautiously)
    options.add_argument('--allow-running-insecure-content')  # Allow insecure content

    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, WAIT_DURATION)
    longwait = WebDriverWait(driver, 1000)

    yield driver, wait, longwait # Returns both driver and wait

    driver.quit()

@pytest.fixture
def generate_fake_user():
    profile = faker.profile()
    first_name, last_name = profile["name"].split(" ", 1) 
    gender = profile["sex"]
    fake_user_gender = gender
    birthdate = faker.date_of_birth()
    formatted_birthdate = birthdate.strftime("%m/%d/%Y")
    company = profile["company"]
    phone = "09763853530"
    sss_number = f"{faker.random_int(10, 99)}-{faker.random_int(1000000, 9999999)}-{faker.random_int(0, 9)}"
    branch = "ANTIQUE-T.A. FORNIER"
    application_type = "New Application"
    salutation = "Mister" if gender == "M" else "Miss"
    civil_status = "MARRIED"
    province = "METRO MANILA"
    city = "PASAY CITY"
    years_in_operation = ""
    website = ""
    nature_of_business = ""
    business_reg_type = ""
    date_of_registration = ""
    date_of_expiry = ""
    business_reg_number = ""
    firm_size = ""
    loan_amount = ""
    tenor = ""
    payment_freq = ""
    loan_facility = ""
    loan_type = ""
    
    return (
        profile, first_name, last_name, gender, company, formatted_birthdate,
        phone, sss_number, branch, application_type, salutation,
        civil_status, province, city, years_in_operation, website,
        nature_of_business, business_reg_type, date_of_registration,
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
    gender = fake_user_gender
    first_name = faker.first_name_female() if gender == 'M' else faker.first_name_male()
    last_name = faker.last_name_female() if gender == 'M' else faker.last_name_male()
    birthdate = faker.date_of_birth()
    formatted_birthdate = birthdate.strftime("%m/%d/%Y")
    email = faker.email()
    
    return (
        first_name, last_name, formatted_birthdate, email
        )


    



