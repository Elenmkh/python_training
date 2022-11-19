import string
import random
from model.contact import Contact


testdata = [Contact(firstname="firstname1", middlename="middlename1", lastname='lastname1', nickname='nickname1',
                    title='title1', company='company1', address='address1', home_phone='home_phone1',
                    mobile_phone='mobile_phone1', work_phone='work_phone1', fax='fax1', email='email1', email2='email12',
                    email3='email13', homepage='homepage1', b_day='1', b_month='January',
                    b_year='year1', a_day='1', a_month='January', a_year='year1', address2='address12',
                    secondaryphone='secondaryphone1', notes='notes1')] +\
           [Contact(firstname="firstname2", middlename="middlename2", lastname='lastname2', nickname='nickname2',
                    title='title2', company='company2', address='address2', home_phone='home_phone2',
                    mobile_phone='mobile_phone2', work_phone='work_phone2', fax='fax2', email='email2', email2='email22',
                    email3='email23', homepage='homepage2', b_day='2', b_month='February',
                    b_year='year2', a_day='2', a_month='February', a_year='year2', address2='address22',
                    secondaryphone='secondaryphone2', notes='notes2')]