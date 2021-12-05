import time

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@given('launch browser')
def startup_browser(context):
    context.driver = webdriver.Chrome(executable_path='C:\\Users\\karlm\\Documents\\Browser_Drivers\\Chrome'
                                                      '\\chromedriver.exe')


@when(u'I open Google homepage')
def step_impl(context):
    context.driver.get('https://www.google.com/')


@when(u'click on GMAIL shortcut')
def step_impl(context):
    rodo_button = context.driver.find_element_by_xpath("//*[@id='L2AGLb']/div")
    if rodo_button.is_displayed():
        context.driver.save_screenshot("rodo_obscures_view.png")
        rodo_button.click()
    else:
        pass
    assert True, context.driver.find_element_by_xpath("//*[@id='gb']/div/div[1]/div/div[1]/a").is_displayed()
    context.driver.find_element_by_xpath("//*[@id='gb']/div/div[1]/div/div[1]/a").click()


@when(u'click on login button')
def step_impl(context):
    context.driver.find_element_by_xpath("/html/body/header/div/div/div/a[2]").click()


@when(u'provide as username "{username}"')
def step_impl(context, username):
    context.driver.find_element_by_xpath("//*[@id='identifierId']").send_keys(username)


@when(u'click Next')
def step_impl(context):
    context.driver.find_element_by_xpath("// *[ @ id = 'identifierNext'] / div / button / span").click()
    # time.sleep(5)


@when(u'provide as password "{password}"')
def step_impl(context, password):
    password_input = WebDriverWait(context.driver, 10).until(
        ec.visibility_of_element_located((By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input")))

    assert True, context.driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input").is_displayed()
    password_input.send_keys(password)


@when(u'click login button')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='passwordNext']/div/button/span").click()


@then(u'login into mail is successful')
def step_impl(context):
    time.sleep(5)
    assert context.driver.find_element_by_css_selector("img.gb_tc").is_displayed() == True, "Missing element"
    context.driver.save_screenshot("google_mail_logged_in.png")
