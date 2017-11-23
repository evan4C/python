# 股票数据爬虫

1. 建立工程和spider模板

	- D:\>cd codes
	- D:\codes>scrapy startproject baiduStocks
	- D:\codes>cd baiduStocks
	- D:\codes\baiduStocks>scrapy genspider stocks baidu.com

2. 编写spider

	- 配置stocks.py文件
	- 修改对返回页面的处理
	- 修改对新增url爬取请求的处理

3. 编写item pipelines

	- 配置pipelines.py
	- 定义对爬取项(scraped item)的处理类
	- 配置ITEM_PIPELINES选项(settings.py)

