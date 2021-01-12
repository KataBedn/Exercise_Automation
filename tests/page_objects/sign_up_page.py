from tests.helpers.support_functions import *
import random


first_name_input = 'firstname'
last_name_input = 'lastname'
mobile_number_input = 'phone'
email_input = 'email'
password_input = 'password'
confirm_password_input = 'confirmpassword'
sign_up_button = 'form[method="POST"] button[type="submit"]'
sign_up_header = '//h3[normalize-space()="Sign Up"]'
gen_email = str(random.randint(100, 1000))+'@test.com'


def sign_up_header_displayed(driver_instance):
    elem = wait_for_visibility_of_element_xpath(driver_instance, sign_up_header)
    return elem.is_displayed()


def first_name_input_correct_credentials(driver_instance):
    elem = driver_instance.find_element_by_name(first_name_input)
    elem.send_keys('John')


def last_name_input_correct_credentials(driver_instance):
    elem = driver_instance.find_element_by_name(last_name_input)
    elem.send_keys('Smith')


def mobile_number_input_correct_credentials(driver_instance):
    elem = driver_instance.find_element_by_name(mobile_number_input)
    elem.send_keys('123456789')


def email_input_correct_credentials(driver_instance):
    elem = driver_instance.find_element_by_name(email_input)
    elem.send_keys(gen_email)


def password_input_correct_credentials(driver_instance):
    elem = driver_instance.find_element_by_name(password_input)
    elem.send_keys('testtest')


def confirm_password_input_correct_credentials(driver_instance):
    elem = driver_instance.find_element_by_name(confirm_password_input)
    elem.send_keys('testtest')


def press_sign_up(driver_instance):
    elem = driver_instance.find_element_by_css_selector(sign_up_button)
    elem.click()


