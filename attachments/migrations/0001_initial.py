# Generated by Django 3.1.7 on 2021-03-16 01:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment_name', models.CharField(max_length=255, verbose_name='attachment_name')),
                ('attachment_type', models.CharField(blank=True, max_length=50, null=True, verbose_name='attachment_type')),
                ('attachment_file', models.FileField(max_length=255, upload_to='attachments')),
                ('parent_type', models.CharField(max_length=50, verbose_name='parent_type')),
                ('parent', models.IntegerField(verbose_name='parent_id')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
                ('uploader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='uploader')),
            ],
        ),
    ]
