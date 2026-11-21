import pytest
@pytest.fixture
def setup():
    print ("setup running")
    return  "chrome"
def test_one(setup):
    print("this is my test1")
    print(setup)
def test_two():
    print("this is my test2")