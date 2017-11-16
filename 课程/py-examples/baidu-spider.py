# baidu-spider

# author = evan

import requests


keyword = 'python'
url = "http://www.baidu.com/s"

try:
    kv = {'wd':keyword}
    r = requests.get(url,params=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print('error')
