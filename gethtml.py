from urllib import request
from http import cookiejar

from urllib import request


# url = 'http://httpbin.org/ip'
proxy = {'http':'218.18.232.26:80','https':'218.18.232.26:80'}
# 创建代理处理器
proxies = request.ProxyHandler(proxy)
# 创建opener对象


# url = 'https://btsow.pw/search/'
# url = 'http://www.baidu.com'
url = 'https://open.163.com/'


# 创建一个cookiejar对象
cookie = cookiejar.CookieJar()
# 使用HTTPCookieProcessor创建cookie处理器
cookies = request.HTTPCookieProcessor(cookie)
# 并以它为参数创建Opener对象
opener = request.build_opener(proxies)
# 使用这个opener来发起请求
# resp = opener.open(url)

# 将这个opener设置为全局的opener
# request.install_opener(opener)
# 创建opener对象
opener = request.build_opener(proxies)

resp = opener.open(url)
print(resp.read().decode())

# resp = request.urlopen(url)

# 查看之前的cookie对象，则可以看到访问百度获得的cookie
# for i in cookie:
#     print(i)

# headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}

# req = request.Request(url, headers=headers)
# resp = request.urlopen(req)
# print(resp.read().decode())