from bs4 import BeautifulSoup
from urllib.parse import urljoin

class CssSelectorParser:

    def parse(self, content, base_url):
        return