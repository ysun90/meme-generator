"""A general interface for ingesting different types of documents.

Separate strategy objects should realize IngestorInterface for each file
type (csv, docx, pdf, txt).

A final Ingestor class should realize the IngestorInterface abstract base
class and encapsulate your helper classes. It should implement logic to
select the appropriate helper for a given file based on filetype.
"""

from abc import ABC, abstractmethod
from typing import List

from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """An abstract base class for different ingestors."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Decide if the document can be ingested.

        param path: loaction of the file
        return: True / False
        """
        # Get extension name of the file
        ext = path.split('.')[-1]

        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the document.

        param path: location of the file
        return: a collection of QuoteModel
        """
        # To be defined in children classes
        pass
