# Generated by Django 3.1.7 on 2021-03-18 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20210318_1711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='report_writer',
        ),
    ]