from data.projects import random_string as rnd_str


def test_signup_new_account(app, check_ui):
    username = rnd_str("user_", 7, spaces=False)
    email = username + "@localhost"
    password = "test"
    app.james.ensure_user_exists(username, password)
    app.signup.new_user(username, email, password)
    assert app.soap.can_login(username, password)
    if check_ui:
        app.session.login(username, password)
        assert app.session.is_logged_in_as(username)
        app.session.logout()
