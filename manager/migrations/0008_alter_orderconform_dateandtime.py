# Generated by Django 4.1.5 on 2023-04-05 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0007_remove_orderconform_paymentstatus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderconform',
            name='dateandtime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]