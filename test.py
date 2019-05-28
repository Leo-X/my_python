# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from time import sleep
import os


#不加载图片,不缓存在硬盘(内存)
SERVICE_ARGS = ['--load-images=false', '--disk-cache=false']
chrome_options = Options()
chrome_options.add_argument("--headless")
# 创建浏览器, 添加参数设置为无界面浏览器
# driver = webdriver.Chrome(service_args=SERVICE_ARGS, chrome_options=chrome_options)
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")
#设置等待时间
waite = WebDriverWait(driver, 8)

driver.get('https://btsow.pw/search/1080p')
text01=driver.find_element_by_css_selector(".data-list .row hidden-xs .col-sm-8.col-lg-9.field").text
print('\n')
print('\n')
print('\n')
print('text01:', text01)
print('\n')
print('\n')
print('\n')
driver.close()


def main():
    # data = get_page_num()
    data = 3
    print('总页数是=', data)
    for page in range(2, int(data) + 1):
        print('key:', page)
    # 退出浏览器
    driver.quit()


# if __name__ == '__main__':
#     print('执行main:')
#     main()

# url01 = "https://btsow.pw/search/1080p"
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# driver = webdriver.Chrome(chrome_options=chrome_options,
#                           executable_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")

# driver.get(url01)
# data = driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[2]/a/div[1]/em").text
# print('\n')
# print('\n')
# print('\n')
# print('data:', data)
# print('\n')
# print('\n')
# print('\n')
# driver.close()
