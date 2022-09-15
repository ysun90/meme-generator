"""Ingestor class realizes the IngestorInterface abstract base class.

It encapsulate all ingestor classes and implement logic to select
the appropriate ingestor for a given file, based on filetype.
"""

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .TXTIngestor import TXTIngestor


class Ingestor(IngestorInterface):
    """An ingestor class to encapsulate all specific ingestors."""

    Ingestors = [DocxIngestor, CSVIngestor, PDFIngestor, TXTIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse contents of files.

        param path: location of the file
        return: a collection of QuoteModel
        """
        for Ingestor in cls.Ingestors:
            if Ingestor.can_ingest(path):
                return Ingestor.parse(path)
