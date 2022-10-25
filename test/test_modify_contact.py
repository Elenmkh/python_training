from model.contact import Contact

def test_test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact()
    app.contact.completation_form(Contact(firstname="Ivan", middlename="Ivanovovich", lastname="Ivanov", nickname="iv",
                            title="p", company="company", address="NY", home_phone="11", mobile_phone="000", work_phone="22",
                            fax="666", email="iv.iv@gmail.ru", email2="ish@", email3="p", homepage="contact", b_day="13",
                            b_month="April", b_year="1966", a_day="13", a_month="july", a_year="1999", address2="Moscow",
                            phone2="**", notes="коллега"))
    app.session.logout()