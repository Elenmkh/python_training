import random

from model.contact import Contact
from random import randrange


def test_modify_contact(app, json_contact, db, check_ui):
    if app.contact.count() == 0:
        app.contact.add()
        app.contact.fill_contact_form(json_contact)
        app.contact.aply_create()
    old_contacts = db.get_contact_list()
    contacts = json_contact
    random_contact = random.choice(old_contacts)
    app.contact.modify_contact_by_id(random_contact.id, contacts)
    new_contacts = db.get_contact_list()
    old_contacts = repl(old_contacts, random_contact, contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(delete_symbols(new_contacts), key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


def repl(old_contacts, random_contact, contacts):
    for i in range(len(old_contacts)):
        if old_contacts[i].id == random_contact.id:
            old_contacts[i] = contacts
            old_contacts[i].id = random_contact.id
    return old_contacts


def clear(contact):
    for i in [contact.firstname, contact.lastname, contact.address]:
        if i is not None:
            i = ' '.join(i.split())
            i = i.strip()
    return contact

def delete_symbols(contact):
    return list(map(lambda x: clear(x), contact))