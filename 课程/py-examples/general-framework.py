import requests

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.appearant_encoding
        return r.text
    except:
        print ("出现异常")
    
    
    
