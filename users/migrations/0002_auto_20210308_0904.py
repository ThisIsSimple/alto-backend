# Generated by Django 3.1.7 on 2021-03-08 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='entered_at',
            field=models.DateField(blank=True, null=True, verbose_name='entered at'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='nickname',
            field=models.TextField(blank=True, verbose_name='nickname'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.TextField(blank=True, max_length=11, null=True, unique=True, verbose_name='phone'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='profile',
            field=models.TextField(blank=True, verbose_name='profile'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile', verbose_name='profile image'),
        ),
    ]
