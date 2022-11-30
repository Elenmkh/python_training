from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group
import random



def test_add_contact_to_group(app, json_contact, orm_db):
    #db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    groups = orm_db.get_group_list()
    contacts = orm_db.get_contact_list()
    if len(groups) == 0:
        app.group.create(Group(name="test"))
        groups = orm_db.get_group_list()
    if len(contacts) == 0:
        app.contact.add()
        app.contact.fill_contact_form(json_contact)
        app.contact.aply_create()
    random_group = random.choice(groups)
    random_contact = random.choice(contacts)
    old_contacts = orm_db.get_contacts_in_group(random_group)
    app.contact.add_contact_to_group_by_id(random_contact.id, random_group.id)
    new_contacts = orm_db.get_contacts_in_group(random_group)
    old_contacts.append(random_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
