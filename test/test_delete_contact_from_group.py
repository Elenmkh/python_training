from model.contact import Contact
from model.group import Group
import random



def test_add_contact_to_group(app, json_contact, orm_db):
    groups = orm_db.get_group_list()
    if len(groups) == 0:
        app.group.create(Group(name="test"))
        groups = orm_db.get_group_list()
    random_group = random.choice(groups)
    contacts = orm_db.get_contacts_in_group(random_group)
    if len(contacts) == 0:
        if len(orm_db.get_contact_list())== 0:
            app.contact.add()
            app.contact.fill_contact_form(json_contact)
            app.contact.aply_create()
        old_contacts = orm_db.get_contacts_in_group(random_group)
        random_contact = random.choice(old_contacts)
        app.contact.add_contact_to_group_by_id(random_contact.id, random_group.id)
    else:
        old_contacts = orm_db.get_contacts_in_group(random_group)
        random_contact = random.choice(old_contacts)
    app.contact.delete_contact_from_group(random_contact.id, random_group.id)
    new_contacts = orm_db.get_contacts_in_group(random_group)
    old_contacts.remove(random_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)