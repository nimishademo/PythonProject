import  pytest
@pytest.fixture()
def setup():
    print("setup created")
    yield
    print("teardown")