# Generated by Django 4.1.5 on 2023-04-01 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='table',
        ),
        migrations.AddField(
            model_name='orders',
            name='note',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
