#coding:utf-8
from django.apps import AppConfig


class ZhihuConfig(AppConfig):
    name = 'zhihu'

class ApiConfig():
    last = 'https://news-at.zhihu.com/api/4/news/latest'
    before = 'https://news-at.zhihu.com/api/4/news/before/'
    news = 'https://news-at.zhihu.com/api/4/news/'
class ua():
    UserAgent = 'Mozilla/5.0 (compatible; Baiduspider-render/2.0; +http://www.baidu.com/search/spider.html)'
    # UserAgent = Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0)'
    cookie = '*'