import unittest
from selenium import webdriver
from config.test_settings import TestSettings
from tests.page_objects import main_page, sign_up_page, sign_in_page, logged_in_page


class Tests(unittest.TestCase):


    def setUp(self):
        if TestSettings.browser == 'chrome':
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Firefox()
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.quit()


    def test1_sign_up_with_correct_credentials(self):
        self.assertTrue(main_page.search_container_displayed(self.driver))
        main_page.show_my_account_options(self.driver)
        self.assertTrue(main_page.my_account_options_displayed(self.driver))
        main_page.go_to_sign_up_page(self.driver)
        self.assertTrue(sign_up_page.sign_up_header_displayed(self.driver))
        sign_up_page.first_name_input_correct_credentials(self.driver)
        sign_up_page.last_name_input_correct_credentials(self.driver)
        sign_up_page.mobile_number_input_correct_credentials(self.driver)
        sign_up_page.email_input_correct_credentials(self.driver)
        sign_up_page.password_input_correct_credentials(self.driver)
        sign_up_page.confirm_password_input_correct_credentials(self.driver)
        sign_up_page.press_sign_up(self.driver)
        self.assertTrue(logged_in_page.header_container_displayed(self.driver))


    def test2_sign_in_with_correct_credentials(self):
        self.assertTrue(main_page.search_container_displayed(self.driver))
        main_page.show_my_account_options(self.driver)
        self.assertTrue(main_page.my_account_options_displayed(self.driver))
        main_page.go_to_sign_in_page(self.driver)
        self.assertTrue(sign_in_page.sign_in_header_displayed(self.driver))
        sign_in_page.email_input_correct_credentials(self.driver)
        sign_in_page.password_input_correct_credentials(self.driver)
        sign_in_page.press_login_button(self.driver)
        self.assertTrue(logged_in_page.header_container_displayed(self.driver))


if __name__ == '__main__':
    unittest.main()