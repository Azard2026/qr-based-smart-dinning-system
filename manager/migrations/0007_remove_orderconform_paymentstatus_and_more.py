# Generated by Django 4.1.5 on 2023-04-05 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0006_orderconform'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderconform',
            name='paymentstatus',
        ),
        migrations.RemoveField(
            model_name='orderconform',
            name='paymenttype',
        ),
        migrations.AlterField(
            model_name='orderconform',
            name='itemprices',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='orderconform',
            name='itemquantitys',
            field=models.TextField(),
        ),
    ]
