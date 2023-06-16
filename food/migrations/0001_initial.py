# Generated by Django 4.1.5 on 2023-03-30 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chaat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('price', models.IntegerField()),
                ('cImage', models.ImageField(upload_to='chaat/')),
            ],
        ),
        migrations.CreateModel(
            name='drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('price', models.IntegerField()),
                ('jImage', models.ImageField(upload_to='juices/')),
            ],
        ),
        migrations.CreateModel(
            name='hotdrink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('price', models.IntegerField()),
                ('hImage', models.ImageField(upload_to='hotdrinks/')),
            ],
        ),
        migrations.CreateModel(
            name='milkshack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('price', models.IntegerField()),
                ('mImage', models.ImageField(upload_to='milkshacks/')),
            ],
        ),
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100000)),
                ('date', models.DateTimeField()),
                ('total', models.IntegerField()),
                ('notes', models.CharField(max_length=350)),
            ],
        ),
        migrations.CreateModel(
            name='ourspecial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('price', models.IntegerField()),
                ('oImage', models.ImageField(upload_to='ourspecial/')),
            ],
        ),
        migrations.CreateModel(
            name='pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('price', models.IntegerField()),
                ('iImage', models.ImageField(upload_to='pizza/')),
            ],
        ),
        migrations.CreateModel(
            name='sandwich',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('price', models.IntegerField()),
                ('wImage', models.ImageField(upload_to='sandwich/')),
            ],
        ),
        migrations.CreateModel(
            name='tablenumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tablename', models.CharField(max_length=20)),
            ],
        ),
    ]