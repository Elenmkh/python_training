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


    def completation_form(self, contact):
        wd = self.app.wd
        #fill name form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        #fill extra information
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        #fill address form
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        # fill phone form
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_phone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        #fill email form
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        #fill birth date form
        wd.find_element_by_name("bday").click()
        wd.find_element_by_xpath(f"//option[@value='{contact.b_day}']").click()
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_xpath(f"//option[@value='{contact.b_month}']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.b_year)
        #fill Anniversary form
        wd.find_element_by_name("aday").click()
        wd.find_element_by_xpath(f'//select[@name ="aday"]/option[@value="{contact.a_day}"]').click()
        wd.find_element_by_name("amonth").click()
        wd.find_element_by_xpath(f'//select[@name ="amonth"]/option[@value="{contact.a_month}"]').click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").send_keys(contact.a_year)
        #fill secondary form
        #wd.find_element_by_name("new_group").click()
        #wd.find_element_by_xpath("//option[@value='[none]']").click()
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        #wd.find_element_by_name("theform").click()
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)


    def aply_create(self):
        wd = self.app.wd
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.return_to_home_page()


    def aply_edit(self):
        wd = self.app.wd
        # submit contact creation
        wd.find_element_by_name("Update").click()
        self.app.return_to_home_page()


    def delete_first_contact(self):
        wd = self.app.wd
        # delete
        wd.find_element_by_xpath('//*[@value="Delete"]').click()


    def modify_first_contact(self):
        wd = self.app.wd
        self.open_contact_page(wd)
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit delition
        wd.find_element_by_xpath('//*[@title = "Edit"]').click()
        wd.find_element_by_name("firstname")



