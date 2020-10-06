TAPS_COURSE_MENU = "#menu-item-506 > a"


def click_taps_page_from_menu(driver_instance):
    elem = driver_instance.find_element_by_css_selector(TAPS_COURSE_MENU)
    elem.click()