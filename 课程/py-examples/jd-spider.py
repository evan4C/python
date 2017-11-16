# jd spider

# author = evan

import requests

url = "https://item.jd.com/4772588.html"

try:
    r = requests.get(url)
    r.raise_for_status()       # function 需要带()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("error")
