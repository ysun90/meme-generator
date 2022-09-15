"""DOCXIngestor moduel ingest .txt files."""

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TXTIngestor(IngestorInterface):
    """An ingestor for txt files."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse contents of files.

        param path: location of the file
        return: a collection of QuoteModel
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        with open(path, 'r') as infile:
            for line in infile.readlines():
                line = line.split(' - ')
                new_quote = QuoteModel(line[0], line[1])
                quotes.append(new_quote)

        return quotes
