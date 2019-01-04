import pytest

@pytest.mark.skip("Test is n/a")
def test_login(app):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
