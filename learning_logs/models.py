from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

import django_tables2 as tables
import django_filters
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import InlineCheckboxes
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field, Div

from django_tables2.utils import A
from django_countries.widgets import CountrySelectWidget


# A topic a user is learning about

# Managers / Manager methods


class TopicManager (models.Manager):
    def event_finder(self, keyword):
        # Self refers to the manager itself
        return self.filter(event__icontains=keyword)

# Modifying Initial Manager QuerySets


class MaleManager(models.Manager):
    def get_queryset(self):
        return super(MaleManager, self).get_queryset().filter(gender='M')


class FemaleManager(models.Manager):
    def get_queryset(self):
        return super(FemaleManager, self).get_queryset().filter(gender='F')


class Topic(models.Model):
    sport = models.CharField(max_length=200, default='')
    event = models.CharField(max_length=200)
    asoc = models.CharField(max_length=200, blank=True)
    league = models.CharField(max_length=200, blank=True)
    devision = models.CharField(max_length=200, blank=True,)
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), blank=True)
    country = CountryField(blank=True, null=True)
    region = models.CharField(max_length=200, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)
    managers = TopicManager()
    objects = models.Manager()
    man = MaleManager()
    female = FemaleManager()

    def __str__(self):
        return u'Sport is %s | Event is %s | Association is  %s | League is %s | Devision is %s | Gender is %s | Country is %s | Region is %s' % (self.sport, self.event, self.asoc, self.league, self.devision, self.gender, self.country, self.region)


class Entry(models.Model):
    '''Something specific about topic'''
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.URLField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

        def __str__(self):
            """Return a string representation of the model."""
            return self.text

# Table


class TopicTable(tables.Table):
    sport = tables.LinkColumn('learning_logs:topic', args=[A('pk')])

    class Meta:
        model = Topic
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}
        fields = (
            'sport',
            'event',
            'asoc',
            'league',
            'devision',
            'gender',
            'country',
            'region',
        )


# Filters
class TopicFilter(django_filters.FilterSet):
    sport = django_filters.CharFilter(lookup_expr='icontains')
    event = django_filters.CharFilter(lookup_expr='icontains')
    asoc = django_filters.CharFilter(lookup_expr='icontains')
    league = django_filters.CharFilter(lookup_expr='icontains')
    devision = django_filters.CharFilter(lookup_expr='icontains')
    # country = django_filters.CharFilter(lookup_expr='icontains')
    region = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Topic
        fields = ['sport', 'event', 'asoc', 'league', 'devision', 'gender', 'country']


class TopicFilterFormHelper(FormHelper):
    form_method = 'GET'
    form_class = 'form-inline'
    layout = Layout(
        Div(
            Div('sport', css_class='col-sm-3'),
            Div('event', css_class='col-sm-3'),
            Div('asoc', css_class='col-sm-3'),
            Div('league', css_class='col-sm-3'),
            css_class='row'),
        Div(
            Div('gender', css_class='col-sm-3'),
            Div('devision', css_class='col-sm-3'),
            Div('country', css_class='col-sm-6'),
            css_class='row'),

        Div(Div(Submit('submit', 'Apply Filter', css_class='btn btn-warning btn-sm'), css_class='col-sm-3 pull-left', style='margin-top: 10px;'), css_class='row')
    )
