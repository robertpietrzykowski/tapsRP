from selenium.webdriver.common.action_chains import ActionChains


def move_to_element_by_xpath(driver, selector):
    actions = ActionChains(driver)
    elem = driver.find_element_by_xpath(selector)
    actions.move_to_element(elem)
    actions.perform()

