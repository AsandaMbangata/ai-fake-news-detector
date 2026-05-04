
class Result:
    def __init__(self, result_id, score, classification):
        self.result_id = result_id
        self.score = score
        self.classification = classification

    def display(self):
        return f"{self.classification} ({self.score}%)"