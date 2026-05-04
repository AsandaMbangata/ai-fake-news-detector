
class NewsArticle:
    def __init__(self, article_id, text):
        self.article_id = article_id
        self.text = text
        self.status = "Submitted"

    def preprocess(self):
        self.text = self.text.lower()
        self.status = "Processed"