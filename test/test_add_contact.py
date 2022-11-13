from model.contact import Contact
import random
import pytest
import string
import datetime
import re

def random_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits+" "*10#+string.punctuation
    return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_date(date_type):
    if date_type == 'day':
        return str(random.randint(1, 28))
    elif date_type =='month':
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                  'November', 'December']
        return str(random.choice(months))
    elif date_type == 'year':
        year = string.digits
        return "".join([random.choice(year) for i in range(random.randrange(4))])



testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                    home_phone="", mobile_phone="", work_phone="", fax="", email="", email2="", email3="",
                    homepage="", b_day="0", b_month="-", b_year="", a_day="0", a_month="-", a_year="", address2="",
                    secondaryphone="", notes="")] +\
           [Contact(firstname=random_string('firstname', 10), middlename=random_string('middlename', 10),
                    lastname=random_string('lastname', 10), nickname=random_string('nickname', 10),
                    title=random_string('title', 10), company=random_string('company', 10),
                    address=random_string('address', 10), home_phone=random_string('home_phone', 10),
                    mobile_phone=random_string('mobile_phone', 10), work_phone=random_string('work_phone', 10),
                    fax=random_string('fax', 10), email=random_string('email', 10), email2=random_string('email2', 10),
                    email3=random_string('email3', 10), homepage=random_string('homepage', 10),
                    b_day=random_date('day'), b_month=random_date('month'),
                    b_year=random_date('year'), a_day=random_date('day'), a_month=random_date('month'),
                    a_year=random_date('year'), address2=random_string('address2', 10),
                    secondaryphone=random_string('secondaryphone', 10), notes=random_string('notes', 10))]

@pytest.mark.parametrize("contacts", testdata, ids=[repr(x) for x in testdata])
def test_test_add_contact(app, contacts):
    old_contacts = app.contact.get_contact_list()
    app.contact.add()
    app.contact.fill_contact_form(contacts)
    app.contact.aply_create()
    assert len(old_contacts)+1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contacts)
    assert sorted(delete_symbols(old_contacts), key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def clear(contact):
    for i in [contact.firstname, contact.lastname, contact.address]:
        if i is not None:
            i = ' '.join(i.split())
            i = i.strip()
    return contact

def delete_symbols(contact):
    return list(map(lambda x: clear(x), contact))

