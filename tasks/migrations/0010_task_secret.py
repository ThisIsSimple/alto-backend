# Generated by Django 3.1.7 on 2021-03-15 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_auto_20210310_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='secret',
            field=models.BooleanField(blank=True, null=True, verbose_name='secret'),
        ),
    ]
