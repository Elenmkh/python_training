from model.contact import Contact


def test_test_modify_contact(app):
    app.contact.modify_first_contact(Contact(firstname="Ivan", middlename="Ivanovovich", lastname="Ivanov", nickname="iv",
                            title="p", company="company", address="NY", home_phone="11", mobile_phone="000", work_phone="22",
                            fax="666", email="iv.iv@gmail.ru", email2="ish@", email3="p", homepage="contact", b_day="13",
                            b_month="April", b_year="1966", a_day="13", a_month="july", a_year="1999", address2="Moscow",
                            phone2="**", notes="коллега"))


def test_test_modify_contact_name(app):
    app.contact.modify_first_contact(Contact(firstname="Grisha", notes="к"))