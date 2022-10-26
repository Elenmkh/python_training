class ContactHelper():
    def __init__(self, app):
        self.app = app

    def open_contact_page(self, wd):
        wd = self.app.wd
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
        self.change_date_value("amonth", contact.a_month)
        self.change_field_value("ayear", contact.a_year)
        # fill secondary form
        # wd.find_element_by_name("new_group").click()
        # wd.find_element_by_xpath("//option[@value='[none]']").click()
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def aply_create(self):
        wd = self.app.wd
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.return_to_home_page()

    def apply_edit(self):
        wd = self.app.wd
        # submit contact creation
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.edit_first_contact()
        # delete
        wd.find_element_by_xpath('//*[@value="Delete"]').click()

    def edit_first_contact(self):
        wd = self.app.wd
        self.open_contact_page(wd)
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit delition
        wd.find_element_by_xpath('//*[@title = "Edit"]').click()
        wd.find_element_by_name("firstname")

    def modify_first_contact(self, new_contact):
        self.edit_first_contact()
        wd = self.app.wd
        self.fill_contact_form(new_contact)
        self.apply_edit()

    def count(self):
        wd = self.app.wd
        self.open_contact_page(wd)
        return len(wd.find_elements_by_name("selected[]"))

