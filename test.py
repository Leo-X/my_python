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
executable_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = executable_path
options = webdriver.ChromeOptions()  # 定义配置对象
options.add_argument(
    "--user-data-dir="+r"D:/Users/wangchuang/AppData/Local/Google/Chrome/User Data")
# 指定用户的配置地址，并加载至配置对象中。
options.add_argument("--headless")

SERVICE_ARGS = ['--load-images=false', '--disk-cache=false']
driver = webdriver.Chrome(executable_path, chrome_options=options)
# 设置等待时间
waite = WebDriverWait(driver, 3)
driver.get('https://www.baidu.com/')


def main():
    # data = get_page_num()
    data = 3
    print('总页数是=', data)
    for page in range(2, int(data) + 1):
        print('key:', page)
    # 退出浏览器
    driver.quit()


if __name__ == '__main__':
    main()


# //此处注意，有两个参数，后面那个参数，一定要写成 chrome_options=XX的形式，否则运行报错
# driver = webdriver.Firefox()
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com/")
# data = driver.find_element_by_id("s_mod_weather").text
# 打印数据内容
# print('\n')
# print('\n')
# print('\n')
# print('data:', data)
# print('\n')
# print('\n')
# print('\n')
# driver.close()
