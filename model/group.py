class Group:

    def __init__(self,name,header,footer):
        self.name = name
        self.header = header
        self.footer = footer

class Contact:

    def __init__(self, firstname, middlename, lastname, nickname,
                    title, company, address, home_phone, mobile_phone, work_phone, fax, email, email2, email3,
                    homepage, b_day, b_month, b_year, a_day, a_month, a_year, address2, phone2, notes):
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