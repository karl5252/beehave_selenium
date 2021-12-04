from behave import given, when, then
from selenium import webdriver
import allure


@given('launch Chrome browser')
def startup_browser(context):
    context.driver = webdriver.Chrome(executable_path='C:\\Users\\karlm\\Documents\\Browser_Drivers\\Chrome'
                                                      '\\chromedriver.exe')


@when('open onet.pl homepage')
def open_page(context):
    context.driver.get('https://www.onet.pl/')


@then('verify logo is present on the homepage')
def check_if_el_present(context):
    context.driver.save_screenshot('onet_main_page.png')
    allure.attach.file('onet_main_page.png', 'opening url')
    assert True, context.driver.find_element_by_xpath("//*[@id='logoOnet']").is_displayed()


@then('close browser')
def teardown(context):
    context.driver.quit()
