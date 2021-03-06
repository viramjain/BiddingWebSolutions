# Generated by Django 3.0.7 on 2020-06-28 10:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Productdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptitle', models.CharField(max_length=100)),
                ('pdesc', models.TextField()),
                ('price', models.CharField(max_length=10)),
                ('Image', models.ImageField(upload_to='images')),
                ('pdate', models.DateTimeField(auto_now=True)),
                ('bidstatus', models.BooleanField(default=False)),
                ('biddate', models.DateField(default=datetime.datetime(2020, 6, 28, 16, 7, 31, 54188))),
                ('bidst', models.TimeField(default=datetime.time(16, 7, 31))),
                ('bidet', models.TimeField(default=datetime.time(16, 7, 31))),
            ],
        ),
    ]
