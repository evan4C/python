import requests
from bs4 import BeautifulSoup
import time

url = 'https://club.autohome.com.cn/bbs/thread/58593f293f149d85/72680583-1.html'

headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36",
            'host': 'club.autohome.com.cn'
        }
clist = []
r = requests.get(url, headers=headers)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text, 'html.parser')
divs = soup.find_all('div', {'class': 'tz-paragraph'})

for i in divs:
    clist.append(i.get_text())


print(clist)
