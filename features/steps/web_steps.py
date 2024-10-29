from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

######################################################################
# Task 7a - Step Definition for the Button Click
######################################################################
@when('I press the "{button}" button')
def step_impl(context, button):
    button_id = button.lower() + '-btn'
    context.driver.find_element(By.ID, button_id).click()

######################################################################
# Task 7b - Step Definition for verifying a specific name or text to be present
######################################################################
@then('I should see "{name}" in the results')
def step_impl(context, name):
    found = WebDriverWait(context.driver, context.wait_seconds).until(
        EC.text_to_be_present_in_element(
            (By.ID, 'search_results'),
            name
        )
    )
    assert found, f"Expected to see '{name}' in the results, but it was not found."

######################################################################
# Task 7c - Step Definition for verifying a specific name or text NOT to be present
######################################################################
@then('I should not see "{name}" in the results')
def step_impl(context, name):
    element = context.driver.find_element(By.ID, 'search_results')
    assert name not in element.text, f"Expected not to see '{name}' in the results, but it was found."

######################################################################
# Task 7d - Step Definition for verifying a specific message is present
######################################################################
@then('I should see the message "{message}"')
def step_impl(context, message):
    found = WebDriverWait(context.driver, context.wait_seconds).until(
        EC.text_to_be_present_in_element(
            (By.ID, 'flash_message'),
            message
        )
    )
    assert found, f"Expected to see the message '{message}', but it was not found."
