from helpers.taps_helpers import move_to_element_by_xpath, make_screenshot

PAWEL_PICTURE = '/html/body/div/main/div/div/div/div/div/div/div/section[9]/div[2]/div/' \
                    'div/div/div/section/div/div/div[1]/div/div/div[1]/div/div/img'


def move_to_photo_and_make_screenshot(driver_instance):
    move_to_element_by_xpath(driver_instance, PAWEL_PICTURE)
    make_screenshot(driver_instance, "test")