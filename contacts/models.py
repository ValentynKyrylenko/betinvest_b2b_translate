from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    business_type = models.CharField(max_length=80, verbose_name='Type of the contact')
    person_name = models.CharField(max_length=80, verbose_name='Name and Surname of the Person')
    company_name = models.CharField(max_length=80, blank=True, verbose_name='Legal Company name')
    website = models.URLField(blank=True, verbose_name='Official WWW')
    country = models.CharField(max_length=80, verbose_name='Country of registering')
    email = models.EmailField(blank=True, null=True, verbose_name='E-mail address')
    skype = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    product = models.CharField(max_length=50, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    notes = models.CharField(max_length=300, blank=True)
    exibition = models.CharField(max_length=50, blank=True, verbose_name='Met on...')
    contacted_on = models.DateField(blank=True, null=True, verbose_name='Date of last contact')
    action_date = models.DateField(blank=True, null=True)
    account_manager = models.ForeignKey(User)

    def __str__(self):
        return u'%s %s' % (self.company_name, self.person_name)

    class Meta:
        verbose_name_plural = 'customers'
        ordering = ['company_name']


class Comment(models.Model):
    comment = models.CharField(max_length=300)
    posted_by = models.ForeignKey(User)
    customer = models.ForeignKey(Customer)
    createdOn = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'comments'
        ordering = ['createdOn']
