# Generated by Django 3.0.7 on 2020-07-21 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productbidding', '0010_auto_20200721_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidentry',
            name='amount',
            field=models.CharField(max_length=20),
        ),
    ]
