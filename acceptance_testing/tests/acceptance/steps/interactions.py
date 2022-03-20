from behave import *

from acceptance_testing.tests.acceptance.page_model.contact_form import ContactForm
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

@when('I enter "(.*)" in the "(.*)" field')
def step_impl(context, content, field_name):
    page = ContactForm(context.driver)
    page.form_field(field_name).send_keys(content)

@when('I press the "(.*)" button') # I think i can replace the regex with just Get Started and remove the parameter
def step_imp(context, content):
    page = ContactForm(context.driver)
    page.get_started.click()

@then('I see "(.*)"')
def step_imp(context, message):
    page = ContactForm(context.driver)
    # AttributeError: 'WebElement' object has no attribute 'thank_you' but i dont want to keep submitting
    # It's probably something with the chaining
    assert(page.form_submitted.thank_you.text == message)
