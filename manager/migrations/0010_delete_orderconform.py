# Generated by Django 4.1.5 on 2023-04-06 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0009_remove_orderconform_dateandtime'),
    ]

    operations = [
        migrations.DeleteModel(
            name='orderconform',
        ),
    ]