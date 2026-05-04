
from creational_patterns.prototype import Article

def test_clone():
    a1 = Article("news")
    a2 = a1.clone()
    assert a1.text == a2.text