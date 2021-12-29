import re
from lxml import html
import requests
import time


class Analysis:
    """分析类"""

    def __init__(self):
        self.host_url = ''  # 网站域名
        self.xpath_to_chapter = ''  # 获取目录信息的xpath表达式
        self.xpath_to_text = ''  # 获取章节文本的xpath表达式
        self.xpath_to_next_page = ''  # 获取下一页元素表达式
        self.chapter_list = []  # 存放目录元素的列表
        self.headers = {}

    #  获取目录列表
    def _get_chapter_list(self, html_data):
        selector = html.fromstring(html_data)
        name_list = selector.xpath(self.xpath_to_chapter)
        for chapter in name_list:
            self.chapter_list.append(
                {'title': chapter.xpath('@title')[0], 'link': 'http://www.zxcsx.com' + chapter.xpath('@href')[0]})

    #  获取每章节的内容
    def _get_chapter_text(self, text_begin, links):
        selector2 = html.fromstring(requests.get(links).text)
        text_result = text_begin
        body = selector2.xpath(self.xpath_to_text)
        for line in body:
            line = re.sub('\s+', '\r\n\t', line).strip('\r\n')
            text_result = text_result + line

        next_page = selector2.xpath(self.xpath_to_next_page)  # 翻页按钮
        if next_page[0].xpath('text()')[0] == '下一页':
            link = self.host_url + next_page[0].xpath('@href')[0]
            #   递归调用方法，获取下一页内容
            text_result = self._get_chapter_text(text_result, link)
        return re.sub('	+', '', text_result).replace('-->>', '')

    def _show_chapter_content(self, chapter_num, param1, param2):
        print(self.chapter_list[chapter_num][param1])
        print(self._get_chapter_text('', self.chapter_list[chapter_num][param2]))
        time.sleep(5)
        print('---------------------------------')

    # 展示章节文本内容
    def _read_chapter(self):
        if len(self.chapter_list) == 0:
            print('未获取到列表')
            return
        chapter_num = 0
        self._show_chapter_content(chapter_num, 'title', 'link')
        while chapter_num <= len(self.chapter_list):
            choose = input("操作：1.下一章 2.上一章 3.选择章节 4.刷新章节 5.显示目录 6.退出 \n")
            if choose == '1':
                chapter_num += 1
                self._show_chapter_content(chapter_num, 'title', 'link')
            elif choose == '2':
                if chapter_num <= 0:
                    print('当前已在第一章')
                    continue
                chapter_num -= 1
                self._show_chapter_content(chapter_num, 'title', 'link')
            elif choose == '3':
                num_id = input('输入要跳转的章节: \n')
                chapter_num = int(num_id) - 1
                self._show_chapter_content(chapter_num, 'title', 'link')
            elif choose == '4':
                print('正在刷新本章')
                self._show_chapter_content(chapter_num, 'title', 'link')
            elif choose == '5':
                num = 1
                for i in self.chapter_list:
                    print(str(num) + ' 标题：' + i['title'])
                    num += 1
            elif choose == '6':
                break
            else:
                print('格式错误')
                continue

    def analysis(self, html_data):
        self._get_chapter_list(html_data)
        self._read_chapter()
