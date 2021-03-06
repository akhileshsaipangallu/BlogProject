from __future__ import unicode_literals
from django.forms import ModelForm
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_details', kwargs={'id': self.id})

    class Meta:
        ordering = ['-timestamp', '-updated']


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content']
