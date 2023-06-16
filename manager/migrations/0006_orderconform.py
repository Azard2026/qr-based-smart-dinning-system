# Generated by Django 4.1.5 on 2023-04-05 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_alter_orders_orderstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='orderconform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billnumber', models.IntegerField()),
                ('tableno', models.CharField(max_length=25)),
                ('itemnames', models.TextField()),
                ('itemquantitys', models.IntegerField()),
                ('itemprices', models.IntegerField()),
                ('itemtotal', models.IntegerField()),
                ('dateandtime', models.DateTimeField()),
                ('paymenttype', models.CharField(blank=True, max_length=25)),
                ('paymentstatus', models.CharField(blank=True, max_length=25)),
            ],
        ),
    ]