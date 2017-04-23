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


def index(request):
    '''Home page for learning_log'''
    logged = request.user
    context = {'logged': logged}
    return render(request, 'learning_logs/index.html', context)


@login_required
def topics(request):
    # Show only the topics created by user
     #topics = Topic.objects.annotate(n_ent=Count('entry')).filter(owner=request.user).order_by('text')
    topics = Topic.objects.annotate(n_ent=Count('entry')).order_by('text')
    # topics = Topic.objects.order_by('date_added')
    # Total number of entries
    total_entries = Entry.objects.count()
    context = {'topics': topics, 'total_entries': total_entries}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    '''Show one topic'''
    topic = Topic.objects.get(id=topic_id)
    # Make sure the topic belongs to the current user.
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
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
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


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


@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    # check for user
    if topic.owner != request.user:
        raise Http404
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


@login_required
def delete_entry(request, delete_id):
   # delete an object and send a confirmation response
    item = Entry.objects.get(id=delete_id)
    topic = item.topic
    item.delete()
    return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))


@login_required
def delete_topic(request, delete_id):
   # delete an object and send a confirmation response
    item = Topic.objects.get(id=delete_id)
    item.delete()

    return HttpResponseRedirect(reverse('learning_logs:topics'))
