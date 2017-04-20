from django.db import models
from django.contrib.auth.models import User

# A topic a user is learning about


class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.text


class Entry(models.Model):
    '''Something specific about topic'''
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

        def __str__(self):
            """Return a string representation of the model."""
            return self.text[:50] + "..."
