from repositories.inmemory.in_memory_user_repository import InMemoryUserRepository
from repositories.inmemory.in_memory_article_repository import InMemoryArticleRepository
from repositories.inmemory.in_memory_result_repository import InMemoryResultRepository


class RepositoryFactory:

    @staticmethod
    def get_user_repository(storage_type):

        if storage_type == "MEMORY":
            return InMemoryUserRepository()

        raise ValueError("Invalid storage type")


    @staticmethod
    def get_article_repository(storage_type):

        if storage_type == "MEMORY":
            return InMemoryArticleRepository()

        raise ValueError("Invalid storage type")


    @staticmethod
    def get_result_repository(storage_type):

        if storage_type == "MEMORY":
            return InMemoryResultRepository()

        raise ValueError("Invalid storage type")