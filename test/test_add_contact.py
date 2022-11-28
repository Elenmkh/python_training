from model.contact import Contact


def test_add_contact(app, db, json_contact, check_ui):
    contact = json_contact
    old_contacts = db.get_contact_list()
    app.contact.add()
    app.contact.fill_contact_form(contact)
    app.contact.aply_create()
    assert len(old_contacts)+1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
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

