from model.contact import Contact
import pytest
from data.contact import testdata


def test_test_add_contact(app, json_contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add()
    app.contact.fill_contact_form(json_contact)
    app.contact.aply_create()
    assert len(old_contacts)+1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(json_contact)
    assert sorted(delete_symbols(old_contacts), key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def clear(contact):
    for i in [contact.firstname, contact.lastname, contact.address]:
        if i is not None:
            i = ' '.join(i.split())
            i = i.strip()
    return contact

def delete_symbols(contact):
    return list(map(lambda x: clear(x), contact))

