from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class TXTIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        with open(path, 'r') as infile:
            for line in infile.readlines():
                 line = line.split(' - ')
                 new_quote = QuoteModel(line[0], line[1])
                 quotes.append(new_quote)

        return quotes
