from model.contact import Contact


def test_all_info_on_home_page(app, db):
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_from_db = sorted(map(clean, db.get_contact_list()), key=Contact.id_or_max)
    for item in contact_from_db:
        phones = [item.home_phone, item.mobile_phone, item.work_phone, item.secondaryphone]
        emails = [item.email, item.email2, item.email3]
        item.all_phones_from_homepage = merge_phone_like_on_home_page(phones)
        item.all_email_from_homepage = merge_email_like_on_home_page(emails)
    assert contact_from_home_page == contact_from_db
    assert_f(contact_from_home_page, contact_from_db)

def assert_f(hp, db):
    for i in range(len(hp)):
        assert hp[i].all_phones_from_homepage == db[i].all_phones_from_homepage
        assert hp[i].all_email_from_homepage == db[i].all_email_from_homepage


def clean(contact):
    return Contact(id=contact.id, firstname= names(contact.firstname), lastname=names(contact.lastname),
                   address=names(contact.address), home_phone=phones(contact.home_phone),
                   work_phone=phones(contact.work_phone), mobile_phone=phones(contact.mobile_phone),
                   secondaryphone = phones(contact.secondaryphone), email=names(contact.email),
                   email2=names(contact.email2), email3=names(contact.email3))

def names(contact):
    return ' '.join(contact.split())

def phones(contact):
    return ''.join(contact.split())


def merge_phone_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x !="", filter(lambda x: x is not None, contact)))

def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x !="", filter(lambda x: x is not None, contact)))

