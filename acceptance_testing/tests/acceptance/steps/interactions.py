from behave import *
from acceptance_testing.tests.acceptance.page_model.home_page import HomePage

use_step_matcher('re')

@when('I click the "(.*)" button')
def step_impl(context, button_text): # i don't think button text matters here
    print('this also should fire')
    page = HomePage(context.driver)
    if page.button: # i dont know if you need the if else here but I'll keep it
        page.button.click()
    else:
        raise Exception("There was no page found")

