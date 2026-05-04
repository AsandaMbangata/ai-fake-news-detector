
from creational_patterns.singleton import DatabaseConnection

def test_singleton():
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    assert db1 is db2