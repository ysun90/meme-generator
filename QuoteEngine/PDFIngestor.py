"""DOCXIngestor moduel ingest .pdf files."""

from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """An ingestor for .pdf files."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse contents of files.

        Call pdftotext to convert pdf to text before parsing.

        param path: location of the file
        return: a collection of QuoteModel
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        # Create a random text
        tmp = f'./tmp/{random.randint(0, 1000000)}.txt'

        # Use pdftotext -layout *.pdf *.txt
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

        # Delete temporary files
        os.remove(tmp)

        return quotes
