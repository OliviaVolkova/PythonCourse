# Generated by Django 4.1.1 on 2022-09-12 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('originalLink', models.CharField(max_length=200)),
                ('hashLink', models.CharField(max_length=200)),
            ],
        ),
    ]