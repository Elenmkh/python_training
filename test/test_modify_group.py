from model.group import Group
import random


def test_modify_group_name(app, json_groups, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = json_groups
    random_group = random.choice(old_groups)
    app.group.modify_group_by_id(random_group.id, json_groups)
    new_groups = db.get_group_list()
    old_groups = repl(old_groups, random_group, group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert clear(sorted(new_groups, key=Group.id_or_max)) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def repl(old_group, random_group, group):
    for i in range(len(old_group)):
        if old_group[i].id == random_group.id:
            old_group[i] = group
            old_group[i].id = random_group.id
    return old_group


def clear(group):
    for i in group:
        if i.name is not None:
            i.name = ' '.join(i.name.split())
            i.name = i.name.strip()
    return group
