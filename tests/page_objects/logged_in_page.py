from tests.helpers.support_functions import *

header_container = '/html/body/div[2]/div[1]/div[1]'

def header_container_displayed(driver_instance):
    elem = wait_for_visibility_of_element_xpath(driver_instance, header_container)
    return elem.is_displayed()