from selenium import webdriver

chrome_driver_path = "/Users/dani/Documents/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

li_elements = driver.find_elements_by_css_selector(".event-widget li")

event_times = {}

for i in range(len(li_elements)):
    time = li_elements[i].find_element_by_tag_name("time")
    name = li_elements[i].find_element_by_tag_name("a")
    event_times[i] = {"time": time.text, "name": name.text}

print(event_times)

driver.quit()