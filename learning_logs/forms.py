from django import forms
from .models import Topic, Entry
from django.forms.widgets import SelectDateWidget, Select, CheckboxSelectMultiple
from django_countries.widgets import CountrySelectWidget

GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = [
            'sport',
            'event',
            'asoc',
            'league',
            'devision',
            'gender',
            'country',
            'region',
        ]

        labels = {
            'sport': 'Sport:',
            'event': 'Event:',
            'asoc': 'Association:',
            'league': 'League:',
            'devision': 'Division',
            'gender': 'Gender',
            'country': 'Country',
            'region': 'Region',
        }
        widgets = {'country': CountrySelectWidget()}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'URL:'}
