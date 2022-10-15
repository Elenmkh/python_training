from group import Contact
import pytest
from application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_add_contact(app):
    app.login(username="admin", password="secret")
    app.add_contact(Contact(firstname="Sergey", middlename="Aleksandrovich", lastname="Ivanov", nickname="s.ivanov",
                title="111", company="ivanov_co", address="Moscow", home_phone="99", mobile_phone="7910", work_phone="5516",
                fax="111", email="i.serg@mail.ru", email2="ttt", email3="eee", homepage="wewe", b_day="16",
                b_month="August", b_year="1978", a_day="16", a_month="December", a_year="2000", address2="russia",
                phone2="ggg", notes="gfjsk"))
    app.logout()

def test_test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.add_contact(Contact(firstname="", middlename="", lastname="", nickname="",
                title="", company="", address="", home_phone="", mobile_phone="", work_phone="",
                fax="", email="", email2="", email3="", homepage="", b_day="0",
                b_month="-", b_year="", a_day="0", a_month="-", a_year="", address2="",
                phone2="", notes=""))
    app.logout()

