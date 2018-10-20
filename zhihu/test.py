import requests

s = requests.session()
s.verify = False
s.headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
url = 'https://www.zhihu.com/people/5daokou/following'
html = s.get(url=url).text
print(url,html)