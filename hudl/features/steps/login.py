from behave import*
from selenium import webdriver
from selenium.webdriver.common.by import By
from features.steps import locators
from features.steps.locators import locator


@given(u'user is on the login page')
def step_impl(context):
    context.browser.get('hudl.com/login/')
    context.browser.find_element(By.XPATH,locator.landing)

@when(u'user is successfully logged in as "{email}"')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.form_login)
    context.browser.find_element(By.ID,locator.form_username).send_keys('vlad.serbu@icloud.com')
    context.browser.find_element(By.ID,locator.form_password).send_keys('vladpass')
    context.browser.find_element(By.XPATH,locator.button_login).click()

@then(u'user is redirected to the profile dashboard')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.top_header)
    context.browser.find_element(By.XPATH,locator.avatar)

@when('user signs in with "{email}" and "{password}"')
def invalid_password_and_email_inputs(context, email, password):
    pass

@when ('user signs in without email and password')
def missing_fields_login(context):
    pass 


@then ('an error message "{error_message}" will be displayed')
def validate_error(context, error_message):
    pass
