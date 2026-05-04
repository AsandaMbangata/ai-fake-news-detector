
class NewsClassifier:
    def classify(self):
        pass

class RealNews(NewsClassifier):
    def classify(self):
        return "Real"

class FakeNews(NewsClassifier):
    def classify(self):
        return "Fake"

class NewsFactory:
    @staticmethod
    def create_news(type):
        if type == "real":
            return RealNews()
        elif type == "fake":
            return FakeNews()