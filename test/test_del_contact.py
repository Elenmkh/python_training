from model.contact import Contact
import random

def test_delete_some_contact(app, db, check_ui):
    old_contacts = db.get_contact_list()
    if app.contact.count() == 0:
        app.contact.add()
        app.contact.fill_contact_form(Contact(middlename="test"))
        app.contact.aply_create()
    random_contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(random_contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(delete_symbols(new_contacts), key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


def clear(contact):
    for i in [contact.firstname, contact.lastname, contact.address]:
        if i is not None:
            i = ' '.join(i.split())
            i = i.strip()
    return contact

def delete_symbols(contact):
    return list(map(lambda x: clear(x), contact))