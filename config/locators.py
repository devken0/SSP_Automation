locators = {
        "startApplicationBtn":'//*[@id="customerIDRow"]/div[2]/div[1]/div[2]/a',
        "branchList":'//*[@id="mdcBranch"]/div[1]',
        "creditProgramChoice":'creditProgram2',
        "customerTypeChoice":'customerType1',
        "customerTypeChoice":'customerType1',
        "consentCheckboxChoice":'cbxConsent',
        "firstNameField":'firstCustomerName',
        "lastNameField":'lastCustomerName',
        "idTypeList":'//*[@id="mdcCusIdType"]/div[1]',
        "idTypeChoice":'//*[@id="idTypeListCus"]/li[45]',
        "idNumberField":'//*[@id="customerIdNum"]',
        "birthDateField":'customerDob',
        "sexList":'//*[@id="mdcCustomerSex"]/div[1]',
        "sexChoice":'[data-value="M"]',
        "mobileNoField":'mobileNumber',
        "emailField":'email',
        "otpField":'/html/body/div/h3',
        "salutationList":'//*[@id="UDF_SSP_CUST_INDIVIDUAL_GENERAL_PROFILE_SSP_CUST_INDIVIDUAL_SALUTATION"]',
        "civilStatusList":'//*[@id="UDF_SSP_CUST_INDIVIDUAL_GENERAL_PROFILE_SSP_CUST_INDIVIDUAL_CIVIL_STATUS"]',
        "pobProvinceList":'//*[@id="UDF_SSP_CUST_INDIVIDUAL_GENERAL_PROFILE_SSP_CUST_INDIVIDUAL_POB_PROVINCE"]',
        'pobCityList':'//*[@id="UDF_SSP_CUST_INDIVIDUAL_GENERAL_PROFILE_SSP_CUST_INDIVIDUAL_POB_CITY"]',
        "tinField":'//*[@id="UDF_SSP_CUST_INDIVIDUAL_GENERAL_PROFILE_SSP_CUST_INDIVIDUAL_TIN"]',
        'governmentIDTypeList':'//*[@id="UDF_SSP_CUST_INDIVIDUAL_GENERAL_PROFILE_SSP_CUST_INDIVIDUAL_GOVT_ID_TYPE"]',
        'govermentIDTypeField':'//*[@id="UDF_SSP_CUST_INDIVIDUAL_GENERAL_PROFILE_SSP_CUST_INDIVIDUAL_GOVT_ID_NUMBER"]',
        'spouseFirstNameField':'//*[@id="UDF_SSP_CUST_INDIVIDUAL_SPOUSE_DETAILS_SSP_CUST_INDIVIDUAL_SPOUSE_FIRST_NAME"]',
        'spouseLastNameField':'//*[@id="UDF_SSP_CUST_INDIVIDUAL_SPOUSE_DETAILS_SSP_CUST_INDIVIDUAL_SPOUSE_LAST_NAME"]',
        'spouseDob':'//*[@id="UDF_SSP_CUST_INDIVIDUAL_SPOUSE_DETAILS_SSP_CUST_INDIVIDUAL_SPOUSE_DOB"]',
        'spouseEmail':'//*[@id="UDF_SSP_CUST_INDIVIDUAL_SPOUSE_DETAILS_SSP_CUST_INDIVIDUAL_SPOUSE_EMAIL_ADDRESS"]',
        'motherFirstNameField':'//*[@id="UDF_SSP_CUST_INDIVIDUAL_MOTHER_MAIDEN_NAME_SSP_CUST_INDIVIDUAL_MDN_FIRST_NAME"]',
        'motherLastNameField':'//*[@id="UDF_SSP_CUST_INDIVIDUAL_MOTHER_MAIDEN_NAME_SSP_CUST_INDIVIDUAL_MDN_LAST_NAME"]',
        'provinceList':'//*[@id="UDF_SSP_CUST_INDIVIDUAL_HOME_ADDRESS_SSP_CUST_INDIVIDUAL_RESIDENTIAL_ADDRESS_PROVINCE"]',
        'cityList':'//*[@id="UDF_SSP_CUST_INDIVIDUAL_HOME_ADDRESS_SSP_CUST_INDIVIDUAL_RESIDENTIAL_ADDRESS_CITY"]',
        'homeOwnershipButton':'//*[@id="tbody_UDFBlock_SSP_CUST_INDIVIDUAL_HOME_ADDRESS"]/tr[5]/td[2]/span[2]/div/label',
        'businessNameField':'//*[@id="UDF_SSP_CUST_INDIVIDUAL_BIZ_GENERAL_PROFILE_SSP_CUST_INDIVIDUAL_BIZ_BUSINESS_NAME"]',
        'yearBusinessField':'//*[@id="UDF_SSP_CUST_INDIVIDUAL_BIZ_GENERAL_PROFILE_SSP_CUST_INDIVIDUAL_BIZ_OPERATION_YEARS"]',
        'socialMediaField':'//*[@id="UDF_SSP_CUST_INDIVIDUAL_BIZ_GENERAL_PROFILE_SSP_CUST_INDIVIDUAL_BIZ_MEDIA"]',
        'natureBusinessList':'//*[@id="UDF_SSP_CUST_INDIVIDUAL_BIZ_GENERAL_PROFILE_SSP_CUST_INDIVIDUAL_BIZ_NATURE_OF_BUSINESS"]',
        'specifyBusinessList':'//*[@id="UDF_SSP_CUST_INDIVIDUAL_BIZ_GENERAL_PROFILE_SSP_CUST_INDIVIDUAL_BIZ_BUSINESS_ACTIVITIES"]',
        'similarhomeAddressButton':'//*[@id="tbody_UDFBlock_SSP_CUST_INDIVIDUAL_BIZ_PRINCIPAL_BUSINESS_ADDRESS"]/tr[1]/td[2]/span[1]/div/label',
        'businessaddressOwnership':'//*[@id="UDF_SSP_CUST_INDIVIDUAL_BIZ_PRINCIPAL_BUSINESS_ADDRESS_SSP_CUST_INDIVIDUAL_BIZ_ADDR_OWNERSHIP"]',
        'businessRegistrationList':'//*[@id="UDF_SSP_CUST_INDIVIDUAL_BIZ_REGISTRATION_DETAILS_SSP_CUST_INDIVIDUAL_BIZ_BUSINESS_REGISTRATION0"]',
        'businessRegistrationOthers':'//*[@id="UDF_SSP_CUST_INDIVIDUAL_BIZ_REGISTRATION_DETAILS_SSP_CUST_INDIVIDUAL_BIZ_BUSINESS_REGISTRATION_OTHERS0"]',
        'dateRegistrationField':'//*[@id="UDF_SSP_CUST_INDIVIDUAL_BIZ_REGISTRATION_DETAILS_SSP_CUST_INDIVIDUAL_BIZ_BUSINESS_REGISTRATION_DATE0"]',
        'expiryRegistrationField':'//*[@id="UDF_SSP_CUST_INDIVIDUAL_BIZ_REGISTRATION_DETAILS_SSP_CUST_INDIVIDUAL_BIZ_BUSINESS_EXPIRY_DATE0"]',
        'registrationNumberField':'//*[@id="UDF_SSP_CUST_INDIVIDUAL_BIZ_REGISTRATION_DETAILS_SSP_CUST_INDIVIDUAL_BIZ_BUSINESS_REGISTRATION_NO0"]',
        'firmSizeButton':'//*[@id="tbody_UDFBlock_SSP_CUST_INDIVIDUAL_BIZ_FIRM_SIZE_EMPLOYMENT_DETAILS"]/tr[1]/td[2]/span[2]/div/label',
        'repaymentofLoans':'//*[@id="available_UDF_SSP_CUST_INDIVIDUAL_SOURCE_OF_FUNDS_SSP_CUST_INDIVIDUAL_SOURCE_OF_FUNDS_REPAYMENT"]/option[1]',
        'addROLButton':'//*[@id="addBtn_UDF_SSP_CUST_INDIVIDUAL_SOURCE_OF_FUNDS_SSP_CUST_INDIVIDUAL_SOURCE_OF_FUNDS_REPAYMENT"]',
        'loanAmountField':'//*[@id="UDF_SSP_CUST_LOAN_APPLICATION_INFO_SSP_CUST_LOAN_APPLICATION_LOAN_AMOUNT"]',
        'tenorField':'//*[@id="UDF_SSP_CUST_LOAN_APPLICATION_INFO_SSP_CUST_LOAN_APPLICATION_LOAN_TENOR"]',
        'proposedRepaymentList':'//*[@id="UDF_SSP_CUST_LOAN_APPLICATION_INFO_SSP_CUST_LOAN_APPLICATION_LOAN_REPAYMENT_FREQUENCY"]',
        'loanFacilityList':'//*[@id="UDF_SSP_CUST_LOAN_APPLICATION_INFO_SSP_CUST_LOAN_APPLICATION_LOAN_FACILITY"]',
        'loanPurposeList':'//*[@id="available_UDF_SSP_CUST_LOAN_APPLICATION_INFO_SSP_CUST_LOAN_APPLICATION_LOAN_PURPOSE"]/option[2]',
        'addloanPurposeButton':'//*[@id="addBtn_UDF_SSP_CUST_LOAN_APPLICATION_INFO_SSP_CUST_LOAN_APPLICATION_LOAN_PURPOSE"]',
        'typeofLoanButton':'//*[@id="udf_table_SSP_CUST_LOAN_APPLICATION_INFO"]/tbody/tr[4]/td[2]/span[2]/div/label',
        'documentChecklist':'//*[@id="documentChecklistLegend"]',
        'attachmentNameField':'documentName',
        'fileUploadButton':''
}

branches = {
        "ANTIQUE-T.A. FORNIER":'//*[@id="branchList"]/li[21]',
        "CEBU BUSINESS PARK":'//*[@id="branchList"]/li[152]',
        "GREENHILLS-ORTIGAS AVE.":'//*[@id="branchList"]/li[245]',
        "HEAD OFFICE CENTER":'//*[@id="branchList"]/li[246]'
}

application_types = {
        "New Application": '//*[@id="udf_table_SSP_CUST_CUSTOMER_TYPES"]/tbody/tr[1]/td[4]/span[1]/div/label'
}

iframes = {
    "sblaf_main_iframe":"productDetailsFrame",
    "upload_document_iframe":"//iframe[contains(@class, 'fancybox-iframe')]"
}





