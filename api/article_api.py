from fastapi import APIRouter

from services.article_service import ArticleService
from repositories.inmemory.in_memory_article_repository import InMemoryArticleRepository
from src.news_article import NewsArticle

router = APIRouter()

repo = InMemoryArticleRepository()

service = ArticleService(repo)


@router.get("/api/articles")
def get_articles():

    return service.get_all_articles()


@router.post("/api/articles")
def create_article():

    article = NewsArticle("1", "Fake news article")

    service.create_article(article)
    return {"message": "Article created"}

@router.put("/api/articles/{article_id}")
def update_article(article_id: str):

    updated_article = NewsArticle(article_id, "Updated article")

    service.update_article(article_id, updated_article)

    return {"message": "Article updated"}


@router.delete("/api/articles/{article_id}")
def delete_article(article_id: str):

    service.delete_article(article_id)

    return {"message": "Article deleted"}


@router.post("/api/articles/{article_id}/analyze")
def analyze_article(article_id: str):

    return {
        "article_id": article_id,
        "classification": "Fake",
        "credibility_score": 25
    }