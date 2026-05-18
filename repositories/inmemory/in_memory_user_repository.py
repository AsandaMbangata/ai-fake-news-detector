from repositories.user_repository import UserRepository

class InMemoryUserRepository(UserRepository):

    def __init__(self):
        self._storage = {}

    def save(self, user):
        self._storage[user.user_id] = user

    def find_by_id(self, entity_id):
        return self._storage.get(entity_id)

    def find_all(self):
        return list(self._storage.values())

    def delete(self, entity_id):
        if entity_id in self._storage:
            del self._storage[entity_id]


    def update(self, user_id, updated_user):
        self._storage[user_id] = updated_user


    def delete(self, user_id):
        if user_id in self._storage:
           del self._storage[user_id]        