# Generated by Django 3.1.7 on 2021-03-09 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='color',
            field=models.CharField(blank=True, default='#000000', max_length=7, null=True, verbose_name='color'),
        ),
        migrations.AlterField(
            model_name='label',
            name='name',
            field=models.CharField(max_length=30, verbose_name='name'),
        ),
    ]