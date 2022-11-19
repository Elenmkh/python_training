import jsonpickle
from model.contact import Contact
import random
import string
import os.path
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data\contact.json"

for a, o in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits+" "*10#+string.punctuation
    return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_date(date_type):
    if date_type == 'day':
        return str(random.randint(1, 28))
    elif date_type =='month':
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                  'November', 'December']
        return str(random.choice(months))
    elif date_type == 'year':
        year = string.digits
        return "".join([random.choice(year) for i in range(random.randrange(4))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                    home_phone="", mobile_phone="", work_phone="", fax="", email="", email2="", email3="",
                    homepage="", b_day="0", b_month="-", b_year="", a_day="0", a_month="-", a_year="", address2="",
                    secondaryphone="", notes="")] +\
           [Contact(firstname=random_string('firstname', 10), middlename=random_string('middlename', 10),
                    lastname=random_string('lastname', 10), nickname=random_string('nickname', 10),
                    title=random_string('title', 10), company=random_string('company', 10),
                    address=random_string('address', 10), home_phone=random_string('home_phone', 10),
                    mobile_phone=random_string('mobile_phone', 10), work_phone=random_string('work_phone', 10),
                    fax=random_string('fax', 10), email=random_string('email', 10), email2=random_string('email2', 10),
                    email3=random_string('email3', 10), homepage=random_string('homepage', 10),
                    b_day=random_date('day'), b_month=random_date('month'),
                    b_year=random_date('year'), a_day=random_date('day'), a_month=random_date('month'),
                    a_year=random_date('year'), address2=random_string('address2', 10),
                    secondaryphone=random_string('secondaryphone', 10), notes=random_string('notes', 10))]



file = os.path.join(os.path.dirname(os.path.abspath(__file__)),"..", f)

with open (file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))