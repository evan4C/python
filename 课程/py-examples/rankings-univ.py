import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[1].string,tds[2].string,tds[3].string])

def printUnivList(ulist,num):
    print("{0:{3}^10}\t{1:{3}^10}\t{2:^10}".format("学校","地址","score",chr(12288))) #使用中文空格填充
    for i in range(num):
        u = ulist[i]
        print("{0:{3}^10}\t{1:{3}^10}\t{2:^10}".format(u[0],u[1],u[2],chr(12288)))

def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html'
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)

main()
