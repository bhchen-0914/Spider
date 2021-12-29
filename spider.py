import requests
import factory


class Spider:
    """
    爬虫类
    """

    def __init__(self, url, web_tag):
        self.url = url
        self.web_tag = web_tag
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67 '
        }

    def _get_html(self):
        html_data = requests.get(self.url, headers=self.headers).text
        return html_data

    def _analysis(self, html_data):
        analyser = factory.CategoryFactory.get_category(self.web_tag)
        analyser.analysis(html_data)

    def run(self):
        """
        启动方法
        """
        html_data = self._get_html()
        self._analysis(html_data)
