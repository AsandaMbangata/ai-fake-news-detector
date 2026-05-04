
class Processor:
    def process(self):
        pass

class RealProcessor(Processor):
    def process(self):
        return "Processing real news"

class FakeProcessor(Processor):
    def process(self):
        return "Processing fake news"

class ProcessorFactory:
    def create_processor(self):
        pass

class RealFactory(ProcessorFactory):
    def create_processor(self):
        return RealProcessor()