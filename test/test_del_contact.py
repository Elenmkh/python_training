from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add()
        app.contact.fill_contact_form(Contact(middlename="test"))
        app.contact.aply_create()
    app.contact.delete_first_contact()
