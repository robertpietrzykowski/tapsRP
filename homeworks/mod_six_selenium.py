from selenium import webdriver
from helpers.taps_helpers import move_to_element_by_xpath, make_screenshot


class Data:
    #CONST
    WEBDRIVER_PATH = "/Users/rpietrzykowski/PycharmProjects/tapsRP/drivers/chromedriver"
    URL = "https://fabrykatestow.pl"

    #ELEMENTS REGION
    TAPS_COURSE_MENU = "#menu-item-506 > a"
    PAWEL_PICTURE = '/html/body/div/main/div/div/div/div/div/div/div/section[9]/div[2]/div/' \
                    'div/div/div/section/div/div/div[1]/div/div/div[1]/div/div/img'
    #ENDREGION


def find_pawel_picture():
    driver = webdriver.Chrome(Data.WEBDRIVER_PATH)
    driver.get(Data.URL)
    driver.find_element_by_css_selector(Data.TAPS_COURSE_MENU).click()
    move_to_element_by_xpath(driver, Data.PAWEL_PICTURE)
    make_screenshot(driver, "test")


find_pawel_picture()



