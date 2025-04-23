### 🚀 **Step 1: Install Selenium**
Before writing tests, you need to install Selenium.

```bash
pip install selenium
```

You also need a **WebDriver** (Chrome, Firefox, Edge) for Selenium to interact with browsers. Download **ChromeDriver** for Chrome from [here](https://chromedriver.chromium.org/downloads) and place it in your project folder.

---

### 📁 **Step 2: Create a Basic Project Structure**
```
/loan_tests
    ├── main.py                 # Central file to run tests
    ├── loan_application_test.py # Test case for the loan application
    ├── locators.py              # Stores element locators (IDs, XPaths)
    ├── config.py                # Stores base URL and settings
```

---

### 🏗 **Step 3: Write a Simple Test**
Here’s a basic **Selenium script** to test loan form submission.

#### `config.py` (Website Settings)
```python
BASE_URL = "https://bank-loan-application.com"
```

#### `locators.py` (Element Locators)
```python
LOAN_AMOUNT_INPUT = "loan_amount"  # ID of loan input field
BUSINESS_NAME_INPUT = "business_name"  # ID of business name field
SUBMIT_BUTTON = "submit"  # ID of submit button
```

#### `loan_application_test.py` (Selenium Test)
```python
from selenium import webdriver
from config import BASE_URL
from locators import LOAN_AMOUNT_INPUT, BUSINESS_NAME_INPUT, SUBMIT_BUTTON

# Start WebDriver
driver = webdriver.Chrome()  # Open Chrome browser
driver.get(BASE_URL)  # Go to loan application page

# Fill out the form
driver.find_element("id", LOAN_AMOUNT_INPUT).send_keys("500000")  # Enter loan amount
driver.find_element("id", BUSINESS_NAME_INPUT).send_keys("XYZ Corporation")  # Enter business name

# Submit the application
driver.find_element("id", SUBMIT_BUTTON).click()

# Verify success message
assert "Application submitted successfully" in driver.page_source

print("✅ Loan application test passed!")

driver.quit()  # Close the browser
```

---

### 🎯 **Step 4: Run the Test**
Run this command in your terminal:

```bash
python loan_application_test.py
```

If everything is correct, the browser will open, fill out the loan application, submit it, and close.

---

### ✅ **Next Steps**
1. **Enhance Tests** ➝ Add more checks for error messages, form validation.  
2. **Use Pytest** ➝ Automate multiple test cases easily.  
3. **Add Logging & Reporting** ➝ Track results in a structured format.  
