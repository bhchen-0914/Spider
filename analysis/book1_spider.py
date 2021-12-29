from analysis.book_analyser import *


class Book1(Analysis):

    def __init__(self):
        super().__init__()
        self.host_url = 'http://www.zxcsx.com'
        self.xpath_to_chapter = '//div[@id="allchapter"]/div[@class="info-chapters flex flex-wrap"]/a'
        self.xpath_to_text = '//div[@id="ss-reader-main"]/article/text()'
        self.xpath_to_next_page = '//*[@id="next_url"]'
        self.chapter_list = []
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67 '
        }