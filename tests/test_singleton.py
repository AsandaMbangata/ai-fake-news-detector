
from creational_patterns.singleton import DatabaseConnection
from creational_patterns.simple_factory import NewsFactory
from creational_patterns.factory_method import RealFactory
from creational_patterns.abstract_factory import WindowsFactory
from creational_patterns.builder import ReportBuilder

def test_singleton():
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    assert db1 is db2

def test_simple_factory_real():
    obj = NewsFactory.create_news("real")
    assert obj.classify() == "Real"


def test_simple_factory_fake():
    obj = NewsFactory.create_news("fake")
    assert obj.classify() == "Fake"    


def test_factory_method():
    factory = RealFactory()
    processor = factory.create_processor()

    assert processor.process() == "Processing real news"


def test_abstract_factory():
    factory = WindowsFactory()
    button = factory.create_button()

    assert button.render() == "Windows Button"


def test_builder():
    report = ReportBuilder().add_section("Intro").add_section("Body").build()

    assert "Intro" in report.sections
    assert "Body" in report.sections   