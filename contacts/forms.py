from django import forms
from django.forms.widgets import SelectDateWidget, Select, CheckboxSelectMultiple
from django_countries.widgets import CountrySelectWidget
from .models import Customer, Comment

YEAR_CHOICES = ('2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020')
PRODUCT_CHOICES = (
    ('SportsBook Live', 'SportsBook Live'),
    ('SportsBook Prematch', 'SportsBook Prematch'),
    ('WhiteLabel', 'WhiteLabel'),
    ('LandBased', 'LandBased'),
)

CONTACT_TYPES = (
    ('Prospect', 'Prospect'),
    ('Competitor', 'Competitor'),
    ('Existing Customer', 'Existing Customer'),
    ('Product Provider', 'Product Provider'),
    ('Other', 'Other'),
)


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'business_type',
            'person_name',
            'company_name',
            'website',
            'country',
            'email',
            'skype',
            'phone',
            'product',
            'notes',
            'exibition',
            'contacted_on',
            'action_date',
            'account_manager',
        ]
        labels = {
            'business_type': 'Type of business',
            'person_name': 'Full name',
            'company_name': 'Company legal name',
            'website': 'WWW',
            'email': 'Contact email',
            'skype': 'Skype',
            'phone': 'Mobile phone',
            'product': 'Products ordered',
            'notes': 'Comments',
            'exibition': 'Place of first meeting',
            'contacted_on': 'Date of the last contact',
            'action_date': 'Next date we should contact',
            'account_manager': 'Account manager',
        }
        widgets = {
            'notes': forms.Textarea(attrs={'cols': 80}),
            'contacted_on': SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"), years=YEAR_CHOICES),
            'action_date': SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"), years=YEAR_CHOICES),
            'product': CheckboxSelectMultiple(choices=PRODUCT_CHOICES),
            'business_type': Select(choices=CONTACT_TYPES),
            'country': CountrySelectWidget(),
        }
        initial = {
            'action_date': 'Specify when the next contact should be made',
        }
       # Custome validator

        def clean_business_type(self):
            business_type = self.cleaned_data['business_type']
            num_words = len(business_type.split())
            if num_words < 2:
                raise forms.ValidationError("Please write more information about the type of business!")
            return business_type


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', ]
        labels = {'comments': 'Comments'}
        widgets = {'comment': forms.Textarea(attrs={'cols': 80})}
    # Custome validator

    def clean_comment(self):
        comment = self.cleaned_data['comment']
        num_words = len(comment.split())
        if num_words < 5:
            raise forms.ValidationError("Please write more information!")
        return comment
