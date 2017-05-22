from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import Customer, Comment
from .forms import CustomerForm
from .forms import CommentForm
# Create your views here.

# Counting objects
from django.db.models import Count

# Tables
from django_tables2 import RequestConfig
from django.views.generic import TemplateView
from django_tables2 import SingleTableView
from .models import ContactsTable, ContactsFilter, ContactsFilterFormHelper

# Pagination
from django.core.paginator import Paginator


@login_required
def contacts(request):
    contacts = Customer.objects.all()
    context = {'contacts': contacts}
    return render(request, 'contacts/contacts.html', context)


@login_required
def contact(request, contact_id):
    '''Show one topic'''
    contact = Customer.objects.get(id=contact_id)
    comments = contact.comment_set.order_by('-createdOn')
    context = {'contact': contact, 'comments': comments}
    return render(request, 'contacts/contact.html', context)


#@login_required
def new_contact(request):
    """Add a new contact."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = CustomerForm()
    else:
        # POST data submitted; process data.
        form = CustomerForm(request.POST)
        if form.is_valid():
            new_customer = form.save(commit=False)
            new_customer.save()
            # unction determines the URL from a named URL pattern
            return HttpResponseRedirect(reverse('contacts:contacts'))
    context = {'form': form}
    return render(request, 'contacts/new_contact.html', context)


@login_required
def new_comment(request, contact_id):
    """Add a new comment for a particular Contact."""
    contact = Customer.objects.get(id=contact_id)
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = CommentForm()
    else:
        # POST data submitted; process data.
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.posted_by = request.user
            new_entry.customer = contact
            new_entry.save()
            return HttpResponseRedirect(reverse('contacts:contact', args=[contact_id]))
    context = {'contact': contact, 'form': form}
    return render(request, 'contacts/new_comment.html', context)


@login_required
def edit_comment(request, comment_id):
    """Edit an existing comment."""
    comment = Comment.objects.get(id=comment_id)
    contact = comment.customer
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = CommentForm(instance=comment)
    else:
        # POST data submitted; process data.
        form = CommentForm(instance=comment, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('contacts:contact',
                                                args=[contact.id]))
    context = {'comment': comment, 'contact': contact, 'form': form}
    return render(request, 'contacts/edit_comment.html', context)


@login_required
def delete_comment(request, comment_id):
   # delete an object and send a confirmation response
    item = Comment.objects.get(id=comment_id)
    contact = item.customer
    item.delete()
    return HttpResponseRedirect(reverse('contacts:contact', args=[contact.id]))


@login_required
def delete_contact(request, contact_id):
   # delete an object and send a confirmation response
    item = Customer.objects.get(id=contact_id)
    item.delete()
    return HttpResponseRedirect(reverse('contacts:contacts'))


class PagedFilteredTableView(SingleTableView):
    filter_class = None
    formhelper_class = None
    context_filter_name = 'filter'

    def get_queryset(self, **kwargs):
        qs = super(PagedFilteredTableView, self).get_queryset()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs

    # def get_table(self, **kwargs):
        #table = super(PagedFilteredTableView, self).get_table()
        #RequestConfig(self.request, paginate={'per_page': 5}).configure(table)
        # return table

    def get_context_data(self, **kwargs):
        context = super(PagedFilteredTableView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        return context


class ContactsTableView(PagedFilteredTableView):
    model = Customer
    table_class = ContactsTable
    template_name = 'contacts/contacts_table.html'
    paginate_by = 5
    filter_class = ContactsFilter
    formhelper_class = ContactsFilterFormHelper
