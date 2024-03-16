from collections import deque
import requests


class Item:
    def __init__(self, url, tries=0):
        self.url = url
        self.start = None
        self.tries = tries


class Runner:
    def __init__(self, parser, sink, logger, seed_urls, rate=100, max_tries=5):
        self._parser = parser
        self._sink = sink
        self._logger = logger
        self._seed_urls = seed_urls
        self._rate = rate
        self._max_tries = max_tries
        self._seen = set()
        self._to_process = deque()
        for url in seed_urls:
            self._to_process.append(Item(url))
            self._seen.add(url)
    
    def _filter(self, urls):
        return

    def _process(self, item):
        resp = requests.get(item.url)
        resp.raise_for_status()
        content = resp.content

    def _write(self, item, result, error):
        self._logger.info(f'Writing for {item.url}, result={result}, error={error}')
        if error is not None:
            self._sink.write({'error': str(error), 'result': None})
            return
        self._sink.write({'error': None, 'result': result, 'url': item.url})

    def run(self):
        while self._to_process:
            item = self._to_process.popleft()
            result = None
        