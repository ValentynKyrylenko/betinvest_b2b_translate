from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry
from .forms import TopicForm
from .forms import EntryForm
# Create your views here.

# Counting objects
from django.db.models import Count

# Tables
from django_tables2 import RequestConfig
from django.views.generic import TemplateView
from django_tables2 import SingleTableView
from .models import TopicTable, TopicFilter, TopicFilterFormHelper

# Permission
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator


def index(request):
    '''Home page for learning_log'''
    logged = request.user
    context = {'logged': logged}
    return render(request, 'learning_logs/index.html', context)


@login_required
def topics(request):
    topics = Topic.objects.annotate(n_ent=Count('entry'))
    total_entries = Entry.objects.count()
    context = {'topics': topics, 'total_entries': total_entries}
    return render(request, 'learning_logs/topics.html', context)


@login_required
@permission_required('learning_logs.view_sport')
def topic(request, topic_id):
    '''Show one topic'''
    topic = Topic.objects.get(id=topic_id)
    # Make sure the topic belongs to the current user.
    # if topic.owner != request.user:
    #raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
@permission_required('learning_logs.add_topic')
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            # unction determines the URL from a named URL pattern
            return HttpResponseRedirect(reverse('learning_logs:topics_table'))
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


#@login_required
@permission_required('learning_logs.change_topic')
def edit_topic(request, record_id):
    """Edit an existing topic."""
    topic = Topic.objects.get(id=record_id)
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = TopicForm(instance=topic)
    else:
        # POST data submitted; process data.
        form = TopicForm(instance=topic, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                args=[topic.id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@permission_required('learning_logs.change_entry')
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    # check for user
    # if topic.owner != request.user:
    #raise Http404
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)


@permission_required('learning_logs.delete_entry')
def delete_entry(request, delete_id):
   # delete an object and send a confirmation response
    item = Entry.objects.get(id=delete_id)
    topic = item.topic
    item.delete()
    return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))


@permission_required('learning_logs.delete_topic')
def delete_topic(request, delete_id):
   # delete an object and send a confirmation response
    item = Topic.objects.get(id=delete_id)
    item.delete()

    return HttpResponseRedirect(reverse('learning_logs:topics_table'))

# Tables--------------------------------------------------------------------------


class PagedFilteredTableView(SingleTableView):
    filter_class = None
    formhelper_class = None
    context_filter_name = 'filter'

    def get_queryset(self, **kwargs):
        qs = super(PagedFilteredTableView, self).get_queryset()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs

    def get_context_data(self, **kwargs):
        context = super(PagedFilteredTableView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        return context


@method_decorator(permission_required('learning_logs.view_all_sports'), name='dispatch')
class TopicsTableView(PagedFilteredTableView):
    model = Topic
    table_class = TopicTable
    template_name = 'learning_logs/topics_table.html'
    paginate_by = 40
    filter_class = TopicFilter
    formhelper_class = TopicFilterFormHelper
