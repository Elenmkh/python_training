from model.group import Group


def test_test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="admin", header="ffff", footer="***"))
    app.session.logout()