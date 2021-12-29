import requests
from lxml import html
import re
import spider

result_list = []
search_url = 'http://www.zxcsx.com/home/search/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67 '
}


def search_book(book_name):
    data = {
        'action': 'search',
        'q': book_name
    }
    html_data = requests.post(search_url, data=data, headers=headers).text
    selector = html.fromstring(html_data)
    return selector


def get_list():
    book_name = input('查找书名: ')
    selector = search_book(book_name)
    books = selector.xpath('/html/body/div[1]/div/div')
    num = 0
    for book in books:
        result_list.append({'id': str(num), 'name': book.xpath('div/div[1]/a/h3/text()')[0],
                            'author': re.sub('\s+', '', book.xpath('div/text()')[2]),
                            'last_chapter': book.xpath('div/span[2]/a/text()')[0],
                            'link': 'http://www.zxcsx.com' + book.xpath('a/@href')[0]})
        num += 1


def select_book():
    for name in result_list:
        print('id:{id}   书名：{name}   作者：{author}   最新章节:{last_chapter}'.format(**name))

    book_id = int(input('输入书名id：'))
    book = spider.Spider(result_list[book_id]['link'], 'BOOK')
    book.run()


if __name__ == '__main__':
    get_list()
    select_book()
