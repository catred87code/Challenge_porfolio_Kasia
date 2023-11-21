import os
import unittest
import time
from selenium import webdriver

from pages.add_player import AddPlayer
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from pages.login_page import LoginPage
from pages.dashbord import Dashboard


class TestAddPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome()
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_player(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user04@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_sign_in()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        time.sleep(5)
        add_player = AddPlayer(self.driver)
        add_player.click_add_player()
        add_player.title_of_page()
        time.sleep(5)


    def tearDown(self):
        self.driver.quit()


