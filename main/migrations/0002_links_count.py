# Generated by Django 4.1.1 on 2022-09-12 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='links',
            name='count',
            field=models.CharField(default=0, max_length=200),
        ),
    ]
