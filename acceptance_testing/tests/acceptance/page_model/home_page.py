from acceptance_testing.tests.acceptance.locators.home_page import HomePageLocators

class HomePage:
    def __init__(self, driver):
        self.driver = driver


    @property
    def url(self):
        return 'https://www.carruslearn.com/'

    @property
    def button(self):
        return self.driver.find_element(*HomePageLocators.BUTTON)

    @property
    def form(self):
        return self.driver.find_element(*HomePageLocators.FORM)
