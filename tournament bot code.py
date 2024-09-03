from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import easygui
import time

driver = webdriver.Firefox()

myvar = easygui.enterbox("Enter link to challonge page for tournament.")

#displays the webpage
driver.get(myvar)

driver.execute_script("window.scrollTo(0, 500)")
driver.save_screenshot('screenshot.png')

#driver.quit()