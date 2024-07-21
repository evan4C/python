# encoding = 'utf-8'

# author = evan

import requests
from bs4 import BeautifulSoup
import time
import sys

def getHTMLText(url):
    try:
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36",
            'host': 'www.cheyisou.com'
        }
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('error')

def findPost(url, fpath):
    plist = []
    nlist = []
    html = getHTMLText(url)
    type1 = sys.getfilesystemencoding()
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find_all('div', {'class': 'c-container'})
    for i in divs:
        a = i.find('a')
        plist.append(a.attrs['href'])
        nlist.append(a.attrs['title'])
    print(plist)
    with open(fpath, 'a', encoding=type1) as f:
        f.write(str(nlist) + '\n')
    return plist

def getContent(plist, fpath):
    type1 = sys.getfilesystemencoding()
    for i0 in range(len(plist)):
        clist = []
        url = plist[i0]
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36",
            'host': 'baa.bitauto.com'
        }
        r = requests.get(url, headers=headers)
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text, 'html.parser')
        div = soup.find('div', {'class': 'post_width'})
        if div:
            clist.append(div.get_text())
            print('post number' + str(i0))
            time.sleep(3)
            with open(fpath, 'a', encoding=type1) as f1:
                f1.write(str(clist) + '\n')


def main():
    pagenumber = 100
    Cpath = 'ConRW-Y.txt'
    Npath = 'NameRW-Y.txt'
    for i in range(pagenumber):
        s1_url = 'http://www.cheyisou.com/luntan/%E8%8D%A3%E5%A8%81/'
        s2_url = '.html?cysid=1'
        start_url = s1_url + str(i+1) + s2_url
        plist = findPost(start_url, Npath)
        getContent(plist, Cpath)
        time.sleep(1)
        print('page number'+str(i+1))

main()
