from model.group import Group
from random import randrange


def test_test_modify_group_name(app, json_groups):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    group = json_groups
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, json_groups)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index]=group
    assert clear(sorted(old_groups, key=Group.id_or_max)) == sorted(new_groups, key=Group.id_or_max)


def clear(group):
    for i in group:
        if i.name is not None:
            i.name = ' '.join(i.name.split())
            i.name = i.name.strip()
    return group
