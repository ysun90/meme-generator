from abc import ABC, abstractmethod
from typing import List

from .QuoteModel import QuoteModel

class IngestorInterface(ABC):
    """An abstract base class for variuos ingestors.

    Separate strategy objects should realize IngestorInterface for each file
    type (csv, docx, pdf, txt).

    A final Ingestor class should realize the IngestorInterface abstract base
    class and encapsulate your helper classes. It should implement logic to
    select the appropriate helper for a given file based on filetype.
    """

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
