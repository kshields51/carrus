from acceptance_testing.tests.acceptance.locators.home_page import HomePageLocators
from acceptance_testing.tests.acceptance.page_model.base_page import BasePage


class HomePage(BasePage):


    @property
    def button(self):
        return self.driver.find_element(*HomePageLocators.BUTTON)

    @property
    def form(self):
        return self.driver.find_element(*HomePageLocators.FORM)
