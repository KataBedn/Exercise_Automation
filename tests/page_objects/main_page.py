from tests.helpers.support_functions import *


my_account_dropdown = '//a[normalize-space()="My Account"]'
dropdown_list = 'div[x-placement="bottom-end"]'
search_container = 'search'
sign_in_link = '//a[normalize-space()="Login"]'
sign_up_link = '//a[normalize-space()="Sign Up"]'


def search_container_displayed(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, search_container)
    return elem.is_displayed()


def show_my_account_options(driver_instance):
    elem = wait_for_visibility_of_element_xpath(driver_instance,my_account_dropdown)
    elem.click()


def my_account_options_displayed(driver_instance):
    elem = wait_for_visibility_of_element_css_selector(driver_instance, dropdown_list, time_to_wait=1)
    return elem.is_displayed()


def go_to_sign_in_page(driver_instance):
    elem = driver_instance.find_element_by_xpath(sign_in_link)
    elem.click()


def go_to_sign_up_page(driver_instance):
    elem = driver_instance.find_element_by_xpath(sign_up_link)
    elem.click()