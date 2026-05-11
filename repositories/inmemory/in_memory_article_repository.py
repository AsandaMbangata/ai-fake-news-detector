from repositories.article_repository import ArticleRepository

class InMemoryArticleRepository(ArticleRepository):

    def __init__(self):
        self._storage = {}

    def save(self, article):
        self._storage[article.article_id] = article

    def find_by_id(self, entity_id):
        return self._storage.get(entity_id)

    def find_all(self):
        return list(self._storage.values())

    def delete(self, entity_id):
        if entity_id in self._storage:
            del self._storage[entity_id]