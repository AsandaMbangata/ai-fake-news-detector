class ResultService:

    def __init__(self, repository):
        self.repository = repository

    def create_result(self, result):

        if result.classification not in ["Real", "Fake"]:
            raise ValueError("Invalid classification")
        self.repository.save(result)
        return result

    def get_all_results(self):
        return self.repository.find_all()
    
    def update_result(self, result_id, result):
        self.repository.update(result_id, result)
        return result

    def delete_result(self, result_id):
        self.repository.delete(result_id)
        return {"message": "Result deleted"}