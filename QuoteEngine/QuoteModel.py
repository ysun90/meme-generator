"""QuoteMode module encapsulate text fields for body and author."""


class QuoteModel:
    """A simple model put text and author together."""

    def __init__(self, body: str, author: str):
        """Instantiate the class.

        param body: body of quote
        param suthor: author of quote
        return: None
        """
        self.body = body
        self.author = author

    def quote(self):
        """Print the model contents as: ”body text” - author."""
        return f"{self.body} - {self.author}"
