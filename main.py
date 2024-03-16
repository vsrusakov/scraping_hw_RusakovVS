import logging
import time

from utils.runner import Runner
from utils.css_selector_parser import CssSelectorParser
from utils.file_sink import FileSink

def main():
    logging.basicConfig(
        format='[%(asctime)s] %(name)s %(levelname)s: %(message)s',
        datefmt='%d-%m-%y %H:%M:%S',
        level='INFO',
    )
    logger = logging.getLogger('Runner')
    
    seed_urls = ['https://ru.wikipedia.org/wiki/Чемпионат_Европы_по_футболу_2024']
    parser = CssSelectorParser()
    
    sink = FileSink('./result.jsonl')
    runner = Runner(parser, sink, logger, seed_urls)
    
    start = time.time()
    runner.run()
    logger.info(f'Total duration is {time.time() - start}')

if __name__ == '__main__':
    main()