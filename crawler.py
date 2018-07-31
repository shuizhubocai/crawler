import requests
import codecs
from urllib.parse import urljoin
from lxml import etree

# 地址管理器
class Urls(object):

    def __init__(self):
        self.newUrls = set()
        self.oldUrls = set()

    def getNewUrl(self):
        url = self.newUrls.pop()
        self.oldUrls.add(url)
        return url

    def addNewUrl(self, url):
        if url not in self.newUrls and url not in self.oldUrls:
            self.newUrls.add(url)

    def addNewUrls(self, urls):
        for url in urls:
            self.addNewUrl(url)

    def getNewUrlsLength(self):
        return len(self.newUrls)

# 页面下载
class Download(object):

    def __init__(self):
        pass

    def download(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        s = requests.session()
        r = s.request(method='get', url=url, headers=headers)
        if r.status_code == 200:
            print('正在抓取地址:%s' % url)
            return r.content
        return None


# 页面解析
class Parser(object):

    def __init(self):
        pass

    def parserHTML(self, url, content):
        html = etree.HTML(content)
        datas = self.getDatas(url, html)
        urls = self.getUrls(url, html)
        return urls, datas

    def getDatas(self, url, html):
        datas = []
        item = html.xpath("//div[contains(@class, 'container')]//h3//a[@class='post-title-link']")
        for key in item:
            datas.append({
                'title': key.text,
                'url': urljoin(url, key.get('href'))
            })
        return datas

    def getUrls(self, url, html):
        return [urljoin(url, key) for key in html.xpath("//nav[@id='page-nav']//a[contains(@class, 'page-number')]//@href")]

# 导出数据到html
class Output(object):

    def __init__(self):
        self.datas = []

    def storeDatas(self, datas):
        for key in datas:
            self.datas.append(key)

    def outputHTML(self):
        with codecs.open('data.html', 'w') as file:
            file.write('<meta charset="utf-8"/>')
            for key in self.datas:
                file.write('<p><a target="_blank" href="%s">%s</a>,%s</p>\n' % (key['url'], key['title'], key['url']))

# 调度器
class Scheduler(object):

    def __init__(self):
        self.urls = Urls()
        self.download = Download()
        self.parserHTML = Parser()
        self.output = Output()

    def crawler(self, root_url):
        self.urls.addNewUrl(root_url)
        while self.urls.getNewUrlsLength() > 0:
            try:
                url = self.urls.getNewUrl()
                content = self.download.download(url)
                urls, datas = self.parserHTML.parserHTML(url, content)
                self.urls.addNewUrls(urls)
                self.output.storeDatas(datas)
            except Exception as e:
                print('crawler fail')
        self.output.outputHTML()


# 实例化
crawler = Scheduler()
crawler.crawler('http://www.dongwm.com/')