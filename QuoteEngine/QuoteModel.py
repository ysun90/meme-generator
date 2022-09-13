
class QuoteModel:
    def __init__(self, body: str, author: str):
        self.body = body
        self.author = author

    def quote(self):
        return f"{self.body} - {self.author}"
