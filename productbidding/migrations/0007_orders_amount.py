# Generated by Django 3.0.7 on 2020-07-08 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productbidding', '0006_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default=0, max_length=100),
        ),
    ]