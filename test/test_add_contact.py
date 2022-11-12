from model.contact import Contact


def test_test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contacts = Contact(firstname="Sergey", middlename="Aleksandrovich", lastname="Ivanov", nickname="s.ivanov",
                       title="111", company="ivanov_co", address="Moscow", home_phone="99", mobile_phone="7910", work_phone="5516",
                       fax="111", email="i.serg@mail.ru", email2="ttt", email3="eee", homepage="wewe", b_day="16",
                       b_month="August", b_year="1978", a_day="16", a_month="December", a_year="2000", address2="russia",
                       secondaryphone="ggg", notes="gfjsk")
    app.contact.add()
    app.contact.fill_contact_form(contacts)
    app.contact.aply_create()
    assert len(old_contacts)+1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def _add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contacts = Contact(firstname="", middlename="", lastname="", nickname="",
                       title="", company="", address="", home_phone="", mobile_phone="", work_phone="",
                       fax="", email="", email2="", email3="", homepage="", b_day="0",
                       b_month="-", b_year="", a_day="0", a_month="-", a_year="", address2="",
                       secondaryphone="", notes="")
    app.contact.add()
    app.contact.fill_contact_form(contacts)
    app.contact.aply_create()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

