from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        tmp = f'./tmp/{random.randint(0, 1000000)}.txt'

        call = subprocess.call(['pdftotext', '-layout', path, tmp])

        infile = open(tmp, 'r')
        quotes = []

        for line in infile.readlines():
            line = line.strip('\n')
            if len(line) > 1:
                parsed = line.split(' - ')
                new_quote = QuoteModel(parsed[0], parsed[1])
                quotes.append(new_quote)

        infile.close()

        os.remove(tmp)

        return quotes
