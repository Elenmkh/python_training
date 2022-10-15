<<<<<<<< HEAD:1_add_contact/fixture/application_contact.py
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


class Application():
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def add_contact(self, Contact):
        wd = self.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        #fill name form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(Contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(Contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(Contact.lastname)
        #fill extra information
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(Contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(Contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(Contact.company)
        #fill address form
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(Contact.address)
        # fill phone form
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(Contact.home_phone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(Contact.mobile_phone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(Contact.work_phone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(Contact.fax)
        #fill email form
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(Contact.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(Contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(Contact.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(Contact.homepage)
        #fill birth date form
        wd.find_element_by_name("bday").click()
        wd.find_element_by_xpath(f"//option[@value='{Contact.b_day}']").click()
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_xpath(f"//option[@value='{Contact.b_month}']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(Contact.b_year)
        #fill Anniversary form
        wd.find_element_by_name("aday").click()
        wd.find_element_by_xpath(f'//select[@name ="aday"]/option[@value="{Contact.a_day}"]').click()
        wd.find_element_by_name("amonth").click()
        wd.find_element_by_xpath(f'//select[@name ="amonth"]/option[@value="{Contact.a_month}"]').click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").send_keys(Contact.a_year)
        #fill secondary form
        wd.find_element_by_name("new_group").click()
        wd.find_element_by_xpath("//option[@value='[none]']").click()
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(Contact.address2)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(Contact.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(Contact.notes)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
========
from contact import Contact
import pytest
from application_contact import Application


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

>>>>>>>> parent of 92f376e (Revert "Перевод тестов на pytest"):1_add_contact/test/test_add_contact.py
