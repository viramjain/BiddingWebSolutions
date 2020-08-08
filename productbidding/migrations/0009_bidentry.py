# Generated by Django 3.0.7 on 2020-07-21 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productbidding', '0008_auto_20200708_2039'),
    ]

    operations = [
        migrations.CreateModel(
            name='BidEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lname', models.CharField(max_length=100)),
                ('fname', models.CharField(max_length=100)),
                ('useremail', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=20)),
                ('bidtime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
