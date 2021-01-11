from tests.helpers.support_functions import *
from tests.page_objects.sign_up_page import gen_email

email = 'username'
password = 'password'
login_button = '//*[@id="loginfrm"]/button'
login_header = '//h3[normalize-space()="Login"]'


def sign_in_header_displayed(driver_instance):
    elem = wait_for_visibility_of_element_xpath(driver_instance, login_header)
    return elem.is_displayed()


def email_input_correct_credentials(driver_instance):
    elem = driver_instance.find_element_by_name(email)
    elem.send_keys(gen_email)


def password_input_correct_credentials(driver_instance):
    elem = driver_instance.find_element_by_name(password)
    elem.send_keys('testtest')


def press_login_button(driver_instance):
    elem = driver_instance.find_element_by_xpath(login_button)
    elem.click()
