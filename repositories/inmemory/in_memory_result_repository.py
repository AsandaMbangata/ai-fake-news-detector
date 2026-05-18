from repositories.result_repository import ResultRepository

class InMemoryResultRepository(ResultRepository):

    def __init__(self):
        self._storage = {}

    def save(self, result):
        self._storage[result.result_id] = result

    def find_by_id(self, entity_id):
        return self._storage.get(entity_id)

    def find_all(self):
        return list(self._storage.values())

    def delete(self, entity_id):
        if entity_id in self._storage:
            del self._storage[entity_id]


    def update(self, result_id, updated_result):
        self._storage[result_id] = updated_result


    def delete(self, result_id):
        if result_id in self._storage:
            del self._storage[result_id]         