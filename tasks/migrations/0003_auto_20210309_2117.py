# Generated by Django 3.1.7 on 2021-03-09 12:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0002_auto_20210309_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
        migrations.AlterField(
            model_name='taskprogress',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task', verbose_name='progresses'),
        ),
    ]
