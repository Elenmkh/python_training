from model.group import Group


def test_test_add_group(app):
    app.group.create(Group(name="ffff", header="ggg", footer="hghg"))


def test_test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

