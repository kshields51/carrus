from selenium.webdriver.common.by import By

class ContactFormLocators:
    FIRST_NAME = By.NAME, 'firstname'
    LAST_NAME = By.NAME, 'lastname'
    WORK_EMAIL = By.NAME, 'workEmail'
    TELEPHONE = By.NAME, 'phone'
    COMPANY_NAME = By.NAME, 'companyName'
    GET_STARTED = By.CSS_SELECTOR, 'input[value="Get Started"]'
    FORM_SUBMITTED = By.ID, 'submitted'
    THANK_YOU = By.TAG_NAME, 'h5'

