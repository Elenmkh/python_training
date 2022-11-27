from model.contact import Contact
import re

class ContactHelper():
    def __init__(self, app):
        self.app = app

    def open_contact_page(self, wd):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("home").click()

    def add(self):
        wd = self.app.wd
        self.open_contact_page(wd)
        # init contact creation
        wd.find_element_by_link_text("add new").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_date_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_xpath(f'//*[@name ="{field_name}"]/option[@value="{text}"]').click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        # fill group form
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        # fill birth date form
        self.change_date_value("bday", contact.b_day)
        self.change_date_value("bmonth", contact.b_month)
        self.change_field_value("byear", contact.b_year)
        # fill Anniversary form
        self.change_date_value("aday", contact.a_day)
        if len(wd.find_elements_by_name("update")) != 0:
            self.change_date_value("amonth", contact.a_month.lower())
        else:
            self.change_date_value("amonth", contact.a_month)
        self.change_field_value("ayear", contact.a_year)
        # fill secondary form
        # wd.find_element_by_name("new_group").click()
        # wd.find_element_by_xpath("//option[@value='[none]']").click()
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.secondaryphone)
        self.change_field_value("notes", contact.notes)


    def aply_create(self):
        wd = self.app.wd
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def apply_edit(self):
        wd = self.app.wd
        # submit contact creation
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.choose_contact_by_index(index)
        # delete
        wd.find_element_by_xpath('//*[@value="Delete"]').click()
        self.contact_cache = None


    def edit_first_contact(self):
        self.choose_contact_by_index(0)

    def choose_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page(wd)
        # select first contact
        wd.find_elements_by_css_selector('[title = "Edit"]')[index].click()
        wd.find_element_by_name("firstname")

    def modify_first_contact(self, new_contact):
        self.modify_contact_by_index(0, new_contact)


    def modify_contact_by_index(self,index, new_contact):
        self.choose_contact_by_index(index)
        wd = self.app.wd
        self.fill_contact_form(new_contact)
        self.apply_edit()

    def modify_contact_by_id(self, id, new_contact):
        self.choose_contact_by_id(id)
        wd = self.app.wd
        self.fill_contact_form(new_contact)
        self.apply_edit()

    def choose_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contact_page(wd)
        # select first contact
        wd.find_elements_by_css_selector('[href$="id=%s"]' % id)[1].click()
        wd.find_element_by_name("firstname")


    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.choose_contact_by_id(id)
        # delete
        wd.find_element_by_xpath('//*[@value="Delete"]').click()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open_contact_page(wd)
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page(wd)
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_phones = cells[5].text
                all_email = cells[4].text
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname, address=address,
                                                  all_phones_from_homepage=all_phones, all_email_from_homepage=all_email))
        return list(self.contact_cache)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page(wd)
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.choose_contact_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, home_phone=home_phone, mobile_phone=mobile_phone,
                       work_phone=work_phone, secondaryphone=secondaryphone, email=email, email2=email2, email3=email3,
                       address=address)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone, secondaryphone=secondaryphone)







