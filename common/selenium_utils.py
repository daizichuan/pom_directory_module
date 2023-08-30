# coding=utf-8
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def byTagName(driver, tagName):
    var = driver.find_element(By.TAG_NAME, tagName)
    return var


def byTagNames(driver, tagName):
    var = driver.find_elements(By.TAG_NAME, tagName)
    return var


def byId(driver, value_id):
    var = driver.find_element(By.ID, value_id)
    return var


def byXpath(driver, value_xpath):
    try:
        var = driver.find_element_by_xpath(value_xpath)
    except AttributeError:
        var = driver.find_element(By.XPATH, value_xpath)
    return var


def byXpaths(driver, value_xpath):
    try:
        var = driver.find_elements_by_xpath(value_xpath)
    except AttributeError:
        var = driver.find_elements(By.XPATH, value_xpath)
    time.sleep(1)
    return var


def byClassName(driver, value_class, class_index):
    try:
        var = driver.find_elements_by_class_name(value_class)[class_index]
    except Exception:
        var = driver.find_elements(By.CLASS_NAME, value_class)[class_index]
    return var


def byClassNames(driver, value_class):
    try:
        var = driver.find_elements_by_class_name(value_class)
    except AttributeError:
        var = driver.find_elements(By.CLASS_NAME, value_class)
    return var


def byCssSelectors(driver, valueCss, css_id):
    try:
        var = driver.find_elements_by_css_selector(valueCss)[css_id]
    except AttributeError:
        var = driver.find_elements(By.CSS_SELECTOR, valueCss)[css_id]
    return var


def byCssSelector(driver, valueCss):
    try:
        var = driver.find_element_by_css_selector(valueCss)
    except AttributeError:
        var = driver.find_element(By.CSS_SELECTOR, valueCss)
    return var


#   js 点击操作
def byJS_classname(driver, classname, index):
    while True:
        bar = 0
        if bar > 3:
            break
        try:
            byClassNames(driver, classname)
            break
        except Exception:
            time.sleep(0.5)
            bar += 0.5
    js = "var js=document.getElementsByClassName('" + classname + "')[" + str(index) + "].click()"
    driver.execute_script(js)
    time.sleep(1)


#   js 清空操作
def byJS_classname_clear(driver, classname, index):
    js = "var js=document.getElementsByClassName('" + classname + "')[" + index + "].value=''"
    driver.execute_script(js)
    time.sleep(1)


def by_linkText(driver, text):
    try:
        var = driver.find_element_by_link_text(text)
    except AttributeError:
        var = driver.find_element(By.LINK_TEXT, text)
    return var


def byJS_click(driver, link_text, index):
    ele = driver.find_elements(By.LINK_TEXT, link_text)[index]
    driver.execute_script("arguments[0].click();", ele)
    time.sleep(1)


def byJS_xpath_click(driver, xpath_value):
    ele = driver.find_element(By.XPATH, xpath_value)
    driver.execute_script("arguments[0].click();", ele)
    time.sleep(1)


def byJS_class_click(driver, class_name, index):
    ele = driver.find_elements(By.CLASS_NAME, class_name)[index]
    driver.execute_script("arguments[0].click();", ele)
    time.sleep(1)


def wait_util_class(driver, class_name):
    return WebDriverWait(driver, 10, 0.1).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, class_name)))


def wait_util_xpath(driver, xpath_name):
    return WebDriverWait(driver, 10, 0.1).until(
        EC.presence_of_all_elements_located((By.XPATH, xpath_name)))
