# Generated by Django 4.1.5 on 2023-04-05 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0008_alter_orderconform_dateandtime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderconform',
            name='dateandtime',
        ),
    ]
