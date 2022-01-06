# content of test_class.py
class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")


# content of test_class_demo.py
class TestClassDemoInstance:
    def test_one(self):
        assert 0

    def test_two(self):
        assert 0