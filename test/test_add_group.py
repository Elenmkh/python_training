from model.group import Group




def test_test_add_group(app, data_groups):
    group = data_groups
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups)+1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert clear(sorted(old_groups, key=Group.id_or_max)) == sorted(new_groups, key=Group.id_or_max)


def clear(group):
    for i in group:
        if i.name is not None:
            i.name = ' '.join(i.name.split())
            i.name = i.name.strip()
    return group

