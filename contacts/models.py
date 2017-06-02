from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User

import django_tables2 as tables

import django_filters

from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import InlineCheckboxes
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit


from django.http import HttpResponse

from multiselectfield import MultiSelectField
PRODUCT_CHOICES = (
    ('SportsBook Live', 'SportsBook Live'),
    ('SportsBook Prematch', 'SportsBook Prematch'),
    ('WhiteLabel', 'WhiteLabel'),
    ('LandBased', 'LandBased'),
    ('Other', 'Other'),
)

from django_tables2.utils import A


# Create your models here.


class Customer(models.Model):
    business_type = models.CharField(max_length=80, verbose_name='Type of the contact')
    person_name = models.CharField(max_length=80, verbose_name='Name and Surname')
    company_name = models.CharField(max_length=80, blank=True, unique=True, verbose_name='Company')
    website = models.URLField(blank=True, verbose_name='WWW')
    country = CountryField()
    email = models.EmailField(blank=True, null=True, verbose_name='E-mail')
    skype = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    product = MultiSelectField(choices=PRODUCT_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)
    notes = models.CharField(max_length=300, blank=True)
    exibition = models.CharField(max_length=50, blank=True, verbose_name='Met on...')
    contacted_on = models.DateField(blank=True, null=True, verbose_name='Last contact')
    action_date = models.DateField(blank=True, null=True)
    account_manager = models.ForeignKey(User)

    def __str__(self):
        return u'%s  %s' % (self.company_name, self.person_name)

    class Meta:
        verbose_name_plural = 'customers'
        ordering = ['company_name']
        permissions = (
            ("view_customer", "Can see individual contact"),
            ("view_all_customers", "Can view a table with all contacts"),
        )


class Comment(models.Model):
    comment = models.CharField(max_length=3000)
    posted_by = models.ForeignKey(User)
    customer = models.ForeignKey(Customer)
    createdOn = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'comments'
        ordering = ['createdOn']


class ContactsTable(tables.Table):
    person_name = tables.LinkColumn('contacts:contact', args=[A('pk')])

    #view = tables.TemplateColumn('<a href="/contact/{{record.id}}"><span class="glyphicon glyphicon-user"></span></a>')
    #edit = tables.TemplateColumn('<a href="/edit_contact/{{record.id}}"><span class="glyphicon glyphicon-pencil"></a>')

    class Meta:
        model = Customer
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}
        fields = (
            'id',
            'person_name',
            'business_type',
            'company_name',
            'email',
            'skype',
            'phone',
            'product',
            'notes',
            'exibition',
            'contacted_on',
            'action_date',
        )


class ContactsFilter(django_filters.FilterSet):
    business_type = django_filters.CharFilter(lookup_expr='icontains')
    company_name = django_filters.CharFilter(lookup_expr='icontains')
    person_name = django_filters.CharFilter(lookup_expr='icontains')
    product = django_filters.CharFilter(lookup_expr='icontains')
    exibition = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Customer
        fields = ['business_type', 'company_name', 'person_name', 'product', 'exibition']


class ContactsFilterFormHelper(FormHelper):
    form_method = 'GET'
    form_class = 'form-inline'
    layout = Layout(
        'business_type',
        'company_name',
        'person_name',
        'product',
        'exibition',
        Submit('submit', 'Apply Filter', css_class='btn btn-warning btn-sm'),
    )
