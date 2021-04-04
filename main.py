from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time

# TODO 1 UPDATE FILEPATH
chrome_driver_path = r"XXX"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# TODO 2 UPDATE JOB FILTERS AND LOCATION
final_url = "https://www.linkedin.com/jobs/search/?f_AL=true&geoId=90000049&keywords=walmart&location=Los%20Angeles%20Metropolitan%20Area"
starting_url = "https://www.linkedin.com/"

# TODO 3 UPDATE CREDENTIALS
my_email = "XXX"
my_password = "XXX"

driver.get(url=starting_url)
time.sleep(1)
driver.find_element_by_xpath('/html/body/nav/div/a[2]').click()
time.sleep(1)
driver.find_element_by_id("username").send_keys(my_email)
driver.find_element_by_id("password").send_keys(my_password)
driver.find_element_by_id("password").send_keys(Keys.ENTER)
driver.get(url=final_url)
driver.fullscreen_window()
time.sleep(2)
driver.fullscreen_window()

# OBOSOLETE ALGORITHM
# driver.find_element_by_class_name("job-card-list__title").click()
# time.sleep(2)
# driver.find_element_by_class_name("jobs-apply-button").click()
# time.sleep(2)
# for i in range(10):
#     driver.find_element_by_class_name("ember-text-field").send_keys(Keys.BACK_SPACE)
# driver.find_element_by_class_name("ember-text-field").send_keys("123456123", Keys.ENTER)
# time.sleep(2)

counter = 0
job_list = driver.find_element_by_class_name("jobs-search-results__list").find_elements_by_tag_name("li")
for item in job_list:
    driver.fullscreen_window()
    job_list = driver.find_element_by_class_name("jobs-search-results__list").find_elements_by_tag_name("li")
    time.sleep(2)
    try:
        job_list[counter].find_element_by_class_name("job-card-list__title").click()
    except NoSuchElementException or StaleElementReferenceException:
        counter += 1
        continue
    time.sleep(2)
    driver.find_element_by_class_name("jobs-apply-button").click()
    time.sleep(2)
    for i in range(10):
        driver.find_element_by_class_name("ember-text-field").send_keys(Keys.BACK_SPACE)
    driver.find_element_by_class_name("ember-text-field").send_keys("123456123", Keys.ENTER)
    time.sleep(2)
    counter += 1
    driver.get(url=final_url)
    time.sleep(2)
