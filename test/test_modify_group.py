from model.group import Group


def test_test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_group_name(Group(name="New", header="ffff", footer="***"))
    app.session.logout()
