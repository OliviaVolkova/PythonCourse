from django.db import models
from django import forms


class Links(models.Model):
    originalLink = models.CharField(max_length=200)
    hashLink = models.CharField(max_length=200)
    count = models.IntegerField(default=0)
    user = models.IntegerField(default=0)

class LinkForm(forms.Form):
    link = forms.CharField(label='link', max_length=400)


class UserForm(forms.Form):
    username = forms.CharField(label='username', max_length=30)
    password = forms.CharField(label='password', max_length=30)
