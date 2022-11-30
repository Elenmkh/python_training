from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group
import random



def test_add_contact_to_group(app, json_contact, orm_db):
    #db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    groups = orm_db.get_group_list()
    if len(groups) == 0:
        app.group.create(Group(name="test"))
    group = random.choice(groups)
    contact = json_contact
    old_contacts = orm_db.get_contacts_in_group(group)
    app.contact.add()
    app.contact.fill_contact_form(contact)
    app.contact.change_group_value(group.id)
    app.contact.aply_create()
    new_contacts = orm_db.get_contacts_in_group(group)
    old_contacts.append(contact)
    assert old_contacts == new_contacts
