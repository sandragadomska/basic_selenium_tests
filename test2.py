from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://bandcamp.com")

driver.find_element_by_class_name("play-btn").click()

driver.close()
