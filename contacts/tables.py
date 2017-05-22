import django_tables2 as tables
from .models import Customer
import django_filters


class ContactsTable(tables.Table):
    edit_entries = tables.TemplateColumn('<a href="/contact/{{record.id}}">Edit</a>')

    class Meta:
        model = Customer
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}
        fields = [
            'id',
            'business_type',
            'person_name',
            'company_name',
            'email',
            'skype',
            'phone',
            'product',
            'notes',
            'exibition',
            'contacted_on',
            'action_date',
        ]


class ContactsFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Customer
        fields = ['business_type', 'company_name', 'product', 'exibition']
