import re

def test_all_info_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    phones = [contact_from_edit_page.home_phone, contact_from_edit_page.mobile_phone, contact_from_edit_page.work_phone,
              contact_from_edit_page.secondaryphone]
    emails = [contact_from_edit_page.email, contact_from_edit_page.email2, contact_from_edit_page.email3]
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_homepage == merge_info_like_on_home_page(phones)
    assert contact_from_home_page.all_email_from_homepage == merge_info_like_on_home_page(emails)



def clear(s):
    return re.sub("[() -]", "", s)

def merge_info_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x !="", map(lambda x: clear(x), filter(lambda x: x is not None, contact))))
