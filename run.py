"""
启动类
"""
from config import book_config
import spider


def run():
    book1 = spider.Spider(book_config.Book_Url_frxxz, book_config.Web_Tag_Book)
    # book1.run()
    book2 = spider.Spider(book_config.Book_Url_zx, book_config.Web_Tag_Book)
    book2.run()
    book3 = spider.Spider(book_config.Book_Url_xzhdx, book_config.Web_Tag_Book)
    # book3.run()


if __name__ == '__main__':
    run()
