# Generated by Django 2.1.7 on 2019-03-23 19:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tollgatedb',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 24, 0, 50, 1, 978247)),
        ),
    ]
