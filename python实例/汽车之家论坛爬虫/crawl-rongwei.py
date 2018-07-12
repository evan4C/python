# encoding = 'utf-8'

# author = evan

import requests
from bs4 import BeautifulSoup
import time
import sys

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('error')

def findPost(url, fpath):
    plist = []
    nlist = []
    html = getHTMLText(url)
    soup = BeautifulSoup(html, 'html.parser')
    dl = soup.find_all('dl', {'class': 'list-dl'})
    for i in dl[1:]:
        a = i.find('a')
        plist.append(a.attrs['href'])
        nlist.append(a.get_text())
    with open(fpath, 'a') as f:
        f.write(str(nlist) + '\n')
    return plist

def getContent(plist, fpath):
    type1 = sys.getfilesystemencoding()
    for i0 in range(len(plist)):
        clist = []
        url = plist[i0]
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
        r = requests.get(url, headers=headers)
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text, 'html.parser')
        divs = soup.find_all('div', {'class': 'tz-paragraph'})
        for i in divs:
            clist.append(i.get_text())
        print('post number'+ str(i0))
        time.sleep(15)
        with open(fpath, 'a', encoding=type1) as f1:
            f1.write(str(clist) + '\n')


def main():
    pagenumber = 100
    Cpath = 'ConRW.txt'
    Npath = 'NameRW.txt'
    for i in range(pagenumber):
        s1_url = 'https://sou.autohome.com.cn/luntan?order=score&q=%C8%D9%CD%FE&page='
        s2_url = '&class=0&ClassId=0&entry=41'
        start_url = s1_url + str(i+56) + s2_url
        plist = findPost(start_url, Npath)
        getContent(plist, Cpath)
        time.sleep(1)
        print('page number'+str(i+1))

main()
