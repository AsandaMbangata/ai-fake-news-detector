from repositories.inmemory.in_memory_user_repository import InMemoryUserRepository
from repositories.inmemory.in_memory_article_repository import InMemoryArticleRepository
from repositories.inmemory.in_memory_result_repository import InMemoryResultRepository

from src.user import User
from src.news_article import NewsArticle
from src.result import Result

def test_save_user():

    repo = InMemoryUserRepository()

    user = User("1", "Kelly", "Admin")

    repo.save(user)

    assert repo.find_by_id("1") == user


def test_find_all_users():

    repo = InMemoryUserRepository()

    user1 = User("1", "Kelly", "Admin")
    user2 = User("2", "John", "User")

    repo.save(user1)
    repo.save(user2)

    assert len(repo.find_all()) == 2


def test_delete_user():

    repo = InMemoryUserRepository()

    user = User("1", "Kelly", "Admin")

    repo.save(user)

    repo.delete("1")

    assert repo.find_by_id("1") is None


def test_save_article():

    repo = InMemoryArticleRepository()

    article = NewsArticle("1", "Fake news detected")

    repo.save(article)

    assert repo.find_by_id("1") == article


def test_find_all_articles():

    repo = InMemoryArticleRepository()

    article1 = NewsArticle("1", "Article 1")
    article2 = NewsArticle("2", "Article 2")

    repo.save(article1)
    repo.save(article2)

    assert len(repo.find_all()) == 2


def test_delete_article():

    repo = InMemoryArticleRepository()

    article = NewsArticle("1", "Fake news")

    repo.save(article)

    repo.delete("1")

    assert repo.find_by_id("1") is None


def test_save_result():

    repo = InMemoryResultRepository()

    result = Result("1", 85, "Fake")

    repo.save(result)

    assert repo.find_by_id("1") == result


def test_find_all_results():

    repo = InMemoryResultRepository()

    result1 = Result("1", 85, "Fake")
    result2 = Result("2", 92, "Real")

    repo.save(result1)
    repo.save(result2)

    assert len(repo.find_all()) == 2


def test_delete_result():

    repo = InMemoryResultRepository()

    result = Result("1", 85, "Fake")

    repo.save(result)

    repo.delete("1")

    assert repo.find_by_id("1") is None