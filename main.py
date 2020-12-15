from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/dani/Documents/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")


def get_biggest_upgrade():
    store = driver.find_elements_by_css_selector("#store div")
    store.reverse()
    for item in store:
        if item.get_attribute("class") != "grayed":
            item.click()
            break


timeout = time.time() + 60*5
click_counter = 0
while True:
    click_counter += 1
    if click_counter > 100:
        get_biggest_upgrade()
        click_counter = 0
    cookie.click()
    if time.time() > timeout:
        break

cookies_per_second = driver.find_element_by_id("cps")
print(cookies_per_second.text)
