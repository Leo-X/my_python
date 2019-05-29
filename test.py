# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # 等待
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from time import sleep
import os


# 不加载图片,不缓存在硬盘(内存)
SERVICE_ARGS = ['--load-images=false', '--disk-cache=false']
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--disable-gpu')
# 创建浏览器, 添加参数设置为无界面浏览器
# driver = webdriver.Chrome(service_args=SERVICE_ARGS, chrome_options=chrome_options)
driver = webdriver.Chrome(chrome_options=chrome_options,
                          executable_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")


driver.implicitly_wait(2)  # 隐式等待 纯等待2秒

# driver.get('https://btsow.pw/search/1080p')
driver.get('https://study.163.com/category/480000003121024')


# driver.execute_script("window.scrollTo(100, document.body.scrollHeight);")
# print('开始计时')
# sleep(2)
# driver.find_element(By.ID,"find").send_keys(Keys.END)
# sleep(2)
# print('结束计时')
sleep(5)


driver.implicitly_wait(5)  # 查找元素的全局等待时间
# 设置等待时间
# WebDriverWait(driver, 5)
# wait = WebDriverWait(driver, 5)
try:
    wait = WebDriverWait(driver, 2)
    tt = wait.until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, '.ux-category-breadcrumb-cat2-item.cat_item a[data-id="480000003121024"]'))
    )
    print('a 个数:', len(tt))
    for item in tt:
        # print('href:', item.get_attribute("href"))
        print('item.text:', item.text)

    print('当前窗口:', driver.current_window_handle)  # 输出当前窗口句柄
    js01 = 'window.open("https://study.163.com/category/480000003124027");'
    driver.execute_script(js01)
    sleep(2)
    windows = driver.window_handles  # 获取窗口列表
    for cur_window in windows:
        if cur_window != driver.current_window_handle:
            print('准备切换窗口')
            sleep(2)
            driver.switch_to_window(cur_window)
            dd = wait.until(EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, '.ux-category-breadcrumb-cat2-item.cat_item a[data-id="480000003123036"]'))
            )
            for item in dd:
                print('item.text:', item.text)

finally:
    driver.quit()

# tt=driver.find_elements_by_css_selector('.uc-recomend-ykt-img')
# tt=driver.find_elements_by_css_selector(".uc-recomend-ykt-img")


# text01=driver.find_element_by_css_selector(".data-list .row hidden-xs .col-sm-8.col-lg-9.field").text

# driver.close()
