# Generated by Django 3.0.7 on 2020-07-23 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productbidding', '0012_bidentry_product_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bidwinner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('useremail', models.IntegerField()),
                ('product_id', models.CharField(max_length=50)),
            ],
        ),
    ]
