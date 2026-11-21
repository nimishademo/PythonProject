import pytest

#approach 1 order tests by position

# @pytest.mark.order(1)
# def test_login():
#     print("This is login test")
# @pytest.mark.order(3)
# def test_add_item():
#     print("This is add item test")
#
# @pytest.mark.order(2)
# def test_logout():
#     print("This is logout")


#approach 2 using before,after

# @pytest.mark.order(1)
# def test_login():
#     print("This is login test")
#
# @pytest.mark.order(before ="test_logout")
# def test_add_item():
#     print("This is add item test")
#
# @pytest.mark.order(after ="test_add_item")
# def test_logout():
#     print("This is logout")

#approach 3 using marker string

@pytest.mark.order("first")
def test_login():
    print("This is login test")

@pytest.mark.order("last")
def test_add_item():
    print("This is add item test")

@pytest.mark.order()
def test_logout():
    print("This is logout")


