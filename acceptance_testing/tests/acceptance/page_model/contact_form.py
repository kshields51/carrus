from selenium.webdriver.common.by import By

from acceptance_testing.tests.acceptance.locators.contact_form import ContactFormLocators
from acceptance_testing.tests.acceptance.page_model.base_page import BasePage


class ContactForm(BasePage):

    # @property
    # def first_name(self):
    #     return self.driver.find_element(*ContactFormLocators.FIRST_NAME)
    #
    # @property
    # def last_name(self):
    #     return self.driver.find_element(*ContactFormLocators.LAST_NAME)
    #
    # @property
    # def work_email(self):
    #     return self.driver.find_element(*ContactFormLocators.WORK_EMAIL)
    #
    # @property
    # def telephone(self):
    #     return self.driver.find_element(*ContactFormLocators.TELEPHONE)
    #
    # @property
    # def company_name(self):
    #     return self.driver.find_element(*ContactFormLocators.COMPANY_NAME)

    def form_field(self, name):
        return self.driver.find_element(By.NAME, name)

    @property
    def get_started(self):
        return self.driver.find_element(*ContactFormLocators.GET_STARTED)

    @property
    def form_submitted(self):
        return self.driver.find_element(*ContactFormLocators.FORM_SUBMITTED)

    @property
    def thank_you(self):
        return self.driver.find_element(*ContactFormLocators.THANK_YOU)
