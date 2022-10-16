from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from argparse import ArgumentParser
import re
from urllib.parse import quote
from urllib import request
import os
import sys
import time
import warnings
import json


def get_card(username, password):

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    print('Driver Launched\n')

    print('登录中...')
    driver.get('https://card.pku.edu.cn/user/user')
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'logon_button')))
    driver.find_element_by_id('user_name').send_keys(username)
    time.sleep(0.1)
    driver.find_element_by_id('password').send_keys(password)
    time.sleep(0.1)
    driver.find_element_by_id('logon_button').click()
    time.sleep(3)
    print('登录结束')

    # search_button = driver.find_element(by=By.NAME, value="btnK")

    driver.find_element_by_link_text('余额查询').click()

    time.sleep(1)

    iframe = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'iframe')))

    driver.switch_to.frame(iframe)

    card = driver.find_element_by_class_name('zongzhichan').text
    card = re.sub('[账户总额: ￥]', '', card)

    driver.quit()

    return card


if __name__ == '__main__':
    username = 'xxxxxxxx'
    password = 'xxxxxxxx'
    card = get_card(username, password)
    print("校园卡账户余额：", card)
