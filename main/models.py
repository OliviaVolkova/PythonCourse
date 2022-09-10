from django.db import models
from django import forms


class Links(models.Model):
    originalLink = models.CharField(max_length=200)
    hashLink = models.CharField(max_length=200)


class LinkForm(forms.Form):
    link = forms.CharField(label='link', max_length=400)
