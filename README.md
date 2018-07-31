# 使用requests+lxml爬取网站
  ![crawler](https://raw.githubusercontent.com/shuizhubocai/crawler/master/assets/screen.png)

# 爬取的网站
- 爬取的是董伟明博客

# 爬虫包含5个模块
- url管理器
- download下载器
- parser解析器
- outpu导出数据
- crawler爬虫调度器

# 使用项目
- 建议使用virtualenv在独立的环境中运行项目
- pip3 install -r requirements.txt
- python crawler.py

# 注意事项
- lsxm版本使用3.5.0。目前高于3.5.0会不兼容
- python版本使用3.6.0
- pip3版本使用10.0.1
