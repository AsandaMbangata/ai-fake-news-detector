class ArticleService:

    def __init__(self, repository):
        self.repository = repository

    def create_article(self, article):

        if not article.text:
            raise ValueError("Article content cannot be empty")
        self.repository.save(article)
        return article

    def get_all_articles(self):
        return self.repository.find_all()
    
    def update_article(self, article_id, article):
        self.repository.update(article_id, article)
        return article

    def delete_article(self, article_id):
        self.repository.delete(article_id)
        return {"message": "Article deleted"}