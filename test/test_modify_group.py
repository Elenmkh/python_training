from model.group import Group


def test_test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="New", header="ffff", footer="***"))
    app.session.logout()
