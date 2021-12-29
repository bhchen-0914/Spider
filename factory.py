"""
工厂类：
供spider调用，用于返回对应的爬虫对象
"""
from analysis import book1_spider


class CategoryFactory:

    @staticmethod
    def get_category(web_tag):
        if web_tag == 'BOOK':
            return book1_spider.Book1()
