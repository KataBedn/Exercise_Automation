
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


def wait_for_visibility_of_element_id(driver_instance, id, time_to_wait=10):
   try:
       elem = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located((By.ID, id)))
   except TimeoutException:
       elem = False
   return elem


def wait_for_visibility_of_element_css_selector(driver_instance, CSS_SELECTOR, time_to_wait=10):
   try:
     elem = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located((By.CSS_SELECTOR, CSS_SELECTOR)))
   except TimeoutException:
       elem = False
   return elem


def wait_for_visibility_of_element_name(driver_instance, NAME, time_to_wait=10):
   try:
       elem = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located((By.NAME, NAME)))
   except TimeoutException:
       elem = False
   return elem


def wait_for_visibility_of_element_xpath(driver_instance, XPATH, time_to_wait=10):
   try:
       elem = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located((By.XPATH, XPATH)))
   except TimeoutException:
       elem = False
   return elem


def wait_for_visibility_of_element_class_name(driver_instance, CLASS_NAME, time_to_wait=10):
   try:
       elem = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located((By.CLASS_NAME, CLASS_NAME)))
   except TimeoutException:
       elem = False
   return elem