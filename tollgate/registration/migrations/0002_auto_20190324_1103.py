# Generated by Django 2.1.7 on 2019-03-24 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logindb1',
            name='lane',
            field=models.CharField(default='lane1', max_length=50),
        ),
    ]
