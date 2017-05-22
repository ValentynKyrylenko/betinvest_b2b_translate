"""Defines URL patterns for learning_logs."""
from django.conf.urls import url
from . import views


from contacts.views import ContactsTableView

urlpatterns = [

    # Contacts URL
    url(r'^contacts/$', views.contacts, name='contacts'),
    # Detail page for a single contact
    url(r'^contact/(?P<contact_id>\d+)/$', views.contact, name='contact'),
    # Page for adding a new contact
    url(r'^new_contact/$', views.new_contact, name='new_contact'),

    # Page for adding a new comment
    url(r'^new_comment/(?P<contact_id>\d+)/$', views.new_comment, name='new_comment'),
    # Page for editing an comment
    url(r'^edit_comment/(?P<comment_id>\d+)/$', views.edit_comment, name='edit_comment'),
    # Page for deleting a comment
    url(r'^delete_comment/(?P<comment_id>\d+)/$', views.delete_comment, name='delete_comment'),

    # Delete Contact

    url(r'^delete_contact/(?P<contact_id>\d+)/$', views.delete_contact, name='delete_contact'),

    # Display all contacts in a table
    url(r'^contacts_table/$', ContactsTableView.as_view(), name='contacts_table'),

    # Editinng contact
    url(r'^edit_contact/(?P<record_id>\d+)/$', views.edit_contact, name='edit_contact'),
]
