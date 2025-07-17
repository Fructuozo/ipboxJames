from selenium.webdriver.common.by import By
from xpaths import authentication
from time import sleep

def login(driver):
    driver.find_element(By.XPATH, authentication["username_path"]).send_keys("****")
    driver.find_element(By.XPATH, authentication["password_path"]).send_keys("*****")
    driver.find_element(By.XPATH, authentication["login_button_path"]).click()
    sleep(2)