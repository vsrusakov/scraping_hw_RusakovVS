from bs4 import BeautifulSoup
from urllib.parse import urljoin

class CssSelectorParser:

    def parse(self, content, base_url):
        soup = BeautifulSoup(content)

        tags = soup.select("#mw-content-text > div.mw-content-ltr.mw-parser-output > table.standard.sortable > tbody > tr")
        t = tags[11].find("td").find_all("a")[-1]
        
        return result, next_urls