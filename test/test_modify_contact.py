from model.contact import Contact
from random import randrange


def test_test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.add()
        app.contact.fill_contact_form(Contact(firstname="test"))
        app.contact.aply_create()
    old_contacts = app.contact.get_contact_list()
    contacts = Contact(firstname="Ivan", middlename="Ivanovovich", lastname="Sergeev", nickname="iv",
                            title="p", company="company", address="NY", home_phone="11", mobile_phone="000", work_phone="22",
                            fax="666", email="iv.iv@gmail.ru", email2="ish@", email3="p", homepage="contact", b_day="13",
                            b_month="April", b_year="1966", a_day="13", a_month="july", a_year="1999", address2="Moscow",
                            phone2="**", notes="коллега")
    index = randrange(len(old_contacts))
    contacts.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contacts)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index]=contacts
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.add()
        app.contact.fill_contact_form(Contact(middlename="test"))
        app.contact.aply_create()
    old_contacts = app.contact.get_contact_list()
    contacts = Contact(firstname="Grisha", notes="к")
    contacts.id = old_contacts[0].id
    app.contact.modify_first_contact(contacts)
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contacts
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)