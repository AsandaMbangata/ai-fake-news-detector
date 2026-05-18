from services.user_service import UserService
from services.article_service import ArticleService
from services.result_service import ResultService

from repositories.inmemory.in_memory_user_repository import InMemoryUserRepository
from repositories.inmemory.in_memory_article_repository import InMemoryArticleRepository
from repositories.inmemory.in_memory_result_repository import InMemoryResultRepository

from src.user import User
from src.news_article import NewsArticle
from src.result import Result

def test_create_user():

    repo = InMemoryUserRepository()

    service = UserService(repo)

    user = User("1", "Kelly", "Admin")

    created_user = service.create_user(user)

    assert created_user.name == "Kelly"


def test_create_article():

    repo = InMemoryArticleRepository()

    service = ArticleService(repo)

    article = NewsArticle("1", "Fake news article")

    created_article = service.create_article(article)

    assert created_article.text == "Fake news article"


def test_create_result():

    repo = InMemoryResultRepository()

    service = ResultService(repo)

    result = Result("1", 90, "Fake")

    created_result = service.create_result(result)

    assert created_result.classification == "Fake"