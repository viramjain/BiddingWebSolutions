# Generated by Django 3.0.7 on 2020-06-28 10:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('productbidding', '0002_auto_20200628_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='biddate',
            field=models.DateField(default=datetime.datetime(2020, 6, 28, 10, 42, 6, 257744, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='bidet',
            field=models.TimeField(default=datetime.time(16, 12, 6)),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='bidst',
            field=models.TimeField(default=datetime.time(16, 12, 6)),
        ),
    ]
