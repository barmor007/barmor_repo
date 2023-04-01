import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def get_driver():
    # get chromedriver
    driver = webdriver.Chrome()
    # open demosite
    driver.get('https://www.saucedemo.com/')
    driver.maximize_window()
    return driver

def log_in(driver, user_name_txt, user_password_txt):
    # enter username
    write_to_field(driver, '#user-name', user_name_txt)
    time.sleep(1)
    # enter password
    write_to_field(driver, '#password', user_password_txt)
    time.sleep(1)
    # click on sign in
    click_butten(driver,'#login-button')
    time.sleep(2)

def check_if_logged_in(driver):
    current_url = driver.current_url
    if(current_url == 'https://www.saucedemo.com/'):
        #we are still in the start/entry page
        return False
    else:
        return True

def add_to_cart(driver):
    click_butten(driver,'#add-to-cart-sauce-labs-backpack')

def go_to_cart(driver):
    click_butten(driver,'#shopping_cart_container > a')

def check_out(driver):
    click_butten(driver,'#checkout')

def fill_details_in_check_out(driver, fitst_name, last_name, postal_code):
    write_to_field(driver, '#first-name', fitst_name)
    write_to_field(driver, '#last-name', last_name)
    write_to_field(driver, '#postal-code', postal_code)
    time.sleep(3)

def continue_after_check_out(driver):
    click_butten(driver,'#continue')

def finish_check_out(driver):
    click_butten(driver,'#finish')
    time.sleep(2)


def click_butten(driver, css_selector):
    butten = driver.find_element(By.CSS_SELECTOR, css_selector)
    butten.click()
    time.sleep(1)

def write_to_field(driver, css_selector, data):
    element = driver.find_element(By.CSS_SELECTOR, css_selector)
    element.send_keys(data)

def check_if_check_out_successfully_completed(driver):
    complete_indication = driver.find_element(By.CSS_SELECTOR, '#checkout_complete_container > h2')
    complete_indication = complete_indication.text
    if(complete_indication == 'Thank you for your order!'):
        return True
    else:
        return False