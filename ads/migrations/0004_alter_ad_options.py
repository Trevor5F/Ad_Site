# Generated by Django 4.2.7 on 2023-12-04 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_alter_ad_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ad',
            options={'ordering': ['-created_at'], 'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
    ]