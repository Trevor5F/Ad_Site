# Generated by Django 4.2.7 on 2023-12-04 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_alter_ad_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='image',
        ),
    ]
