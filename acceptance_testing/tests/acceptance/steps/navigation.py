from behave import *
from selenium import webdriver

from acceptance_testing.tests.acceptance.page_model.home_page import HomePage

use_step_matcher('re')

@given('I am on the homepage')
def step_impl(context):
    print('this should fire')
    context.driver = webdriver.Chrome(r"C:\Users\kshie\Documents\testing\selenium-drivers\chromedriver.exe")
    page = HomePage(context.driver)
    context.driver.get(page.url)

@then('I can see the "Let\'s Connect" popup') # this is weird because i have the single quote in Let's
def step_impl(context):
    page = HomePage(context.driver)
    assert page.form.is_displayed()






