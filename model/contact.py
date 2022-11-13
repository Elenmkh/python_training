from sys import maxsize

class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None,
                 title=None, company=None, address=None, home_phone=None, mobile_phone=None, work_phone=None,
                 fax=None, email=None, email2=None, email3=None, homepage=None, b_day=None, b_month=None,
                 b_year=None, a_day=None, a_month=None, a_year=None, address2=None, secondaryphone=None, notes=None,
                 id=None, all_phones_from_homepage=None, all_email_from_homepage=None):
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
        self.secondaryphone = secondaryphone
        self.notes = notes
        self.id = id
        self.all_phones_from_homepage = all_phones_from_homepage
        self.all_email_from_homepage = all_email_from_homepage

    def __repr__(self):
        return "%s: %s, %s, %s" % (self.id, self.firstname, self.lastname, self.address)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
               (self.lastname is None or other.lastname is None or self.lastname == other.lastname)\
               and (self.firstname is None or other.firstname is None or self.firstname == other.firstname)\
               and (self.address is None or other.address is None or self.address == other.address)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
