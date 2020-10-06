import unittest
from selenium import webdriver
from homeworks.page_objects import main_page, kurs_taps_page

class Data:
    # CONST
    WEBDRIVER_PATH = "/Users/rpietrzykowski/PycharmProjects/tapsRP/drivers/chromedriver"
    URL = "https://fabrykatestow.pl"


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = Data.URL
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_make_pawel_screenshot(self):
        main_page.click_taps_page_from_menu(self.driver)
        kurs_taps_page.move_to_photo_and_make_screenshot(self.driver)


