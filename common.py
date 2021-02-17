from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.wait import WebDriverWait as ww
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from Page_login import Page_login
import time


def open_driver(url):
    driver = webdriver.Chrome()
    driver.get(url)
    return driver


def driver_get(driver, url):
    driver.get(url)


def driver_close(driver):
    driver.close()


def sleep(sec):
    time.sleep(sec)


def wait_until(driver, method, sec=10):
    return ww(driver, sec).until(method)


def get_type2(type_):
    type2 = None
    if type_ == 'by.XPATH':
        type2 = by.XPATH
    elif type_ == 'by.PARTIAL_LINK_TEXT':
        type2 = by.PARTIAL_LINK_TEXT
    return type2


def is_show(driver, xpath, type_='by.XPATH'):
    return ec.visibility_of_element_located(locator=(get_type2(type_), xpath))


def wait_until_show(driver, xpath, type_='by.XPATH', sec=10):
    return ww(driver, sec).until(ec.visibility_of_element_located((get_type2(type_), xpath)))


def s_wait_until_show(driver, xpath, type_='by.XPATH', sec=10):
    return ww(driver, sec).until(ec.visibility_of_all_elements_located((get_type2(type_), xpath)))


def click(ele):
    ele.click()


def context_click(driver, ele):
    ActionChains(driver).context_click(ele).perform()


def clean_input(ele, str1):
    clean(ele)
    ele.send_keys(str1)


def add_input(ele, str1):
    ele.send_keys(str1)


def clean(ele):
    ele.clear()


def assert_text_in(driver, str1, xpath):
    return str1 in wait_until_show(driver, xpath).text


def login(driver, dict1):
    ele = wait_until_show(driver, xpath=Page_login.xpath_usernameinput)
    clean_input(ele, dict1['username'])
    ele = wait_until_show(driver, xpath=Page_login.xpath_passwdinput)
    clean_input(ele, dict1['passwd'])
    ele = wait_until_show(driver, xpath=Page_login.xpath_loginbutton)
    click(ele)
