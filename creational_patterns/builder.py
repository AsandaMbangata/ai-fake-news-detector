
class Report:
    def __init__(self):
        self.sections = []

    def show(self):
        return self.sections

class ReportBuilder:
    def __init__(self):
        self.report = Report()

    def add_section(self, section):
        self.report.sections.append(section)
        return self

    def build(self):
        return self.report