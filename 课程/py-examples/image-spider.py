# image-spider

# author = evan

import requests
import os

url = "http://image.nationalgeographic.com.cn/2017/1113/20171113035359678.jpg"

root = "D://pics//"

path = root + url.split('/')[-1]

try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print('success')
    else:
        print('already exist')
except:
    print('error')
    
