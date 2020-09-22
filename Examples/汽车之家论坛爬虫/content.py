# -*- coding:utf-8 -*-
import requests
from lxml import html
import re
from fontTools.ttLib import TTFont


fontFileName = "autohomeFont.ttf"

# 爬取链接
url = "https://club.autohome.com.cn/bbs/thread/824faeeacd4e4bcb/73225052-1.html"
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

# 获取页面源代码
resp = requests.get(url, headers=headers)

# 用正则表达式提取ttf字体文件的地址
# url('//k3.autoimg.cn/g24/M06/3F/FF/wKgHH1qWFoGATQa3AABhmFKVVrQ43..ttf') format('woff');}
ttfUrlRe = re.search(",url\('(//.*.ttf)'\) format\('woff'\)", resp.text, re.DOTALL)
ttfUrl = ""
if ttfUrlRe:
    ttfUrl = "https:" + ttfUrlRe.group(1)
if ttfUrl:
    # 以文件流的方式，抓取ttf字体文件
    ttfFileStream = requests.get(ttfUrl, stream=True)
    # 将数据流保存在本地的ttf文件中（新创建）
    with open(fontFileName, "wb") as fp:
        for chunk in ttfFileStream.iter_content(chunk_size=1024):
            if chunk:
                fp.write(chunk)
    # 用fontTools模块解析字体库文件
    fontObject = TTFont(fontFileName)
    # 按顺序拿到各个字符的unicode编码
    uniWordList = fontObject['cmap'].tables[0].ttFont.getGlyphOrder()
    #print(111)
    #print(f"自定义字体列表(unicorn编码): {uniWordList}")
    # 将各个字符的unicode编码转换成utf-8编码
    # [b'\xee\xb6\x8f', b'\xee\xb4\xbd', b'\xee\xb7\xb1', …… ]
    utf8WordList = [eval("u'\\u" + uniWord[3:] + "'").encode("utf-8") for uniWord in uniWordList[1:]]
    # print(f"自定义字体列表( utf-8 编码): {utf8WordList}")
    # 获取发帖内容文字
    response = html.fromstring(resp.text)
    contentLst = response.xpath("//div[@class='tz-paragraph']//text()")
    # print(contentLst)


    # 这个部分的逻辑需要特别注意，因为自定义字体，也就是隐藏字符是以utf-8的形式存在的
    # 所有一开始，我们就要以utf-8的编码形式来保持文本内容
    content = ''.encode("utf-8")
    for elem in contentLst:
        content += elem.encode("utf-8")

    # 录入字体文件中的字符。必须要以国际标准的unicode编码，取代汽车之家自己定义的字体编码
    # 这个部分目前是手动输入，但是多次请求，每次拿到的ttf文件可能都不一样，甚至同一个字形，在不同的ttf文件中编码也不同，这个部分需要尤其注意
    # 因为是python3，所以这些字符直接就是Unicode编码
    wordList = ['一', '七', '三', '上', '下', '不', '九', '了', '二', '多', '低', '八',
                '不', '十', '的', '着', '近', '远', '长', '右', '呢', '和', '四', '地', '坏',
                '多', '大', '好', '小', '少', '短', '矮', '高', '左', '很', '得', '是', '更',
                ]
    # print(f"字体文件中字形列表: {wordList}")
    # print(f"contentBefort = {content.decode('utf-8')}")
    # print('--------------- After Convert -----------------')
    # 因为之前提到过，在网页源代码中，这种“&#xec94;” 特殊字符是utf-8编码，所以我们要以utf-8的模式去进行查找替换
    # content 是字符串，是Unicode编码
    for i in range(len(utf8WordList)):
        # 将自定的字体信息，替换成国际标准
        content = content.replace(utf8WordList[i], wordList[i].encode('utf-8'))
    print(content.decode('utf-8'))
