# Generated by Django 3.1.7 on 2021-03-09 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_auto_20210310_0838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='task_name',
        ),
        migrations.AddField(
            model_name='task',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='name'),
        ),
    ]
