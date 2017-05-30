"""Defines URL patterns for learning_logs."""
from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

from learning_logs.views import TopicsTableView

urlpatterns = [
    # Home view
    url(r'^$', views.index, name='index'),
    # Tipics URL
    url(r'^topics/$', views.topics, name='topics'),
    # Detail page for a single topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # Page for adding a new topic
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    # Page for adding a new entry
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # Page for editing an entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
    # Page for deleting an entry
    url(r'^delete_entry/(?P<delete_id>\d+)/$', views.delete_entry, name='delete_entry'),
    # Delete Topic
    url(r'^delete_topic/(?P<delete_id>\d+)/$', views.delete_topic, name='delete_topic'),
    # Display all topics in a table
    url(r'^topics_table/$', login_required(TopicsTableView.as_view()), name='topics_table'),
    # Editinng topic
    url(r'^edit_topic/(?P<record_id>\d+)/$', views.edit_topic, name='edit_topic'),

]
