from bs4 import BeautifulSoup #需要安装
from urllib.request import urlopen

import requests     #需要安装
import webbrowser #自带模块
# if has chinese,apply decode()
# html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')


# url01 = "https://www.huitou51.com/invest/index.html"
url01 = "https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E9%AB%98%E9%80%9F%E7%A3%81%E6%82%AC%E6%B5%AE%E5%88%97%E8%BD%A6/20205729"
website00 = "https://www.baidu.com/s"
website01 = "https://btsow.pw/search/"
# website01 = "https://open.163.com/"
website02 = "https://segmentfault.com/api/user/login?_=df412a87f54ae9dc902c8e7ec6d68a09"
searchText=""
website01+=searchText
result = []
# post_data={'remember':'1','username':'1257543822@qq.com','password':'111aaa'}
# file_data={'uploadFile':open('./image.png','rb')}
# session=requests.Session()
# post01=session.post(website02,data=post_data)  # 先登录 提交信息
# post01=session.get(website02)  #再附带cookie 请求数据，表示登录状态
# post01=session.post(website02,files=file_data)  #提交文件照片
# print('post01.text:', post01.text)  # post 后获得的response 信息

# param={'wd':"python"}
# get01=requests.get(website00,params=param)
get01=requests.get(website01)
print('website01:', website01)
print('key:', get01)

# webbrowser.open(get01.url)
# print('get01.url:', get01.url)
# print('get01.text:', get01.text)
# html = urlopen(website01).read().decode('utf-8')
# dom = BeautifulSoup(html, features='lxml')
# print('dom:', dom)


# print('6666:', website01)
for ii in range(0):
    html = urlopen(website01).read().decode('utf-8')
    dom = BeautifulSoup(html, features='lxml')
    print('dom:', dom)


    val = dom.select('.para a[href]')
    if len(val) != 0:
        print('len:', len(val))
        for item in val:
            print('item:', item['href'])
            # print('a:', item.get_text())
            # print('val:', val)
        # result.append(val[0])
    else:
        pass
