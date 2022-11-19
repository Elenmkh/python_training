from model.contact import Contact
from random import randrange


def test_test_modify_contact(app, json_contact):
    if app.contact.count() == 0:
        app.contact.add()
        app.contact.fill_contact_form(json_contact)
        app.contact.aply_create()
    old_contacts = app.contact.get_contact_list()
    contacts = json_contact
    index = randrange(len(old_contacts))
    contacts.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contacts)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index]=contacts
    assert sorted(delete_symbols(old_contacts), key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def clear(contact):
    for i in [contact.firstname, contact.lastname, contact.address]:
        if i is not None:
            i = ' '.join(i.split())
            i = i.strip()
    return contact

def delete_symbols(contact):
    return list(map(lambda x: clear(x), contact))