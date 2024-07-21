from requests import get
from requests.sessions import Session
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

def shanxi():
    base = "http://sxwjw.shaanxi.gov.cn/"
    response = get(base)
    soup = BeautifulSoup(response.content.decode(), features="html.parser")
    node = soup.find('ul', class_='list_same').find('a')
    with open('data/陕西.txt', 'w') as f:
        print('title: ', node.text, file=f)
        print('html: ', urljoin(base, node['href']), file=f)


def beijing():
    base = 'http://wjw.beijing.gov.cn/xwzx_20031/wnxw/'
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15'
    response = get(base, headers={"User-Agent": user_agent})
    data = response.text
    soup = BeautifulSoup(data, features="html.parser")
    node = soup.find('div', class_='weinei_left_con_line_text').find('a')
    print(node['title'])
    print(urljoin(base, node['href']))


def guizhou():
    base = "http://www.gzhfpc.gov.cn/xwzx_500663/yqtb/"
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15"
    response = get(base, headers={"User-Agent": user_agent})
    data = response.content.decode()
    data = ''.join(data.split())
    url, title = re.search('str_1="(.*?)".*?str_3="(.*?)"', data).groups()
    print(title)
    print(urljoin(base, url))
    print(urljoin())


if __name__ == '__main__':
    guizhou()

