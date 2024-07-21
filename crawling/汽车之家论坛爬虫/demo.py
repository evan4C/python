import requests
from bs4 import BeautifulSoup
import re


def main():
    plist = []
    nlist = []
    url = 'https://sou.autohome.com.cn/luntan?order=score&q=%C8%D9%CD%FE&page=1&class=0&ClassId=0&entry=41'
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    dl = soup.find_all('dl', {'class': 'list-dl'})
    for i in dl[1:]:
        a = i.find('a')
        plist.append(a.attrs['href'])
        nlist.append(a.get_text())

    print(plist, str(nlist))
    s1 = 'asd'
    s2 = 'ccc'
    i =123
    cs = s1 + str(i)+ s2
    print(cs)








main()
