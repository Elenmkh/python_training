class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None,
                    title=None, company=None, address=None, home_phone=None, mobile_phone=None, work_phone=None,
                 fax=None, email=None, email2=None, email3=None, homepage=None, b_day=None, b_month=None,
                 b_year=None, a_day=None, a_month=None, a_year=None, address2=None, phone2=None, notes=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.b_day = b_day
        self.b_month = b_month
        self.b_year = b_year
        self.a_day = a_day
        self.a_month = a_month
        self.a_year = a_year
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes

    def __repr__(self):
        return "%s, %s : %s" % (self.firstname, self.lastname, self.address)

    def __eq__(self, other):
        return self.firstname == other.firstname and self.lastname == other.lastname and self.address == other.address