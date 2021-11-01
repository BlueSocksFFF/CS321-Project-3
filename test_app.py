from app import about


def test_about():
    assert about() == "A todo list created by Diane and Hoang"