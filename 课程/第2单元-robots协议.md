# 网络爬虫尺寸

- requests库 小规模，数据量小

- scrapy库 中规模，数据量较大

- 搜索引擎，定制开发 大规模，爬取速度很关键

# 网络爬虫的限制

- 来源审查 判断user-agent进行限制

- 发布公告 robots协议
告知所有爬虫可爬取的策略，要求爬虫遵守 

# robots协议

形式：在网站根目录下的robots.txt文件

- user-agnet: *
- disallow: /

- 网络爬虫应该自动或人工识别robots.txt，再进行内容爬取

- 类人行为的小规模爬取可以不受限制robots协议

