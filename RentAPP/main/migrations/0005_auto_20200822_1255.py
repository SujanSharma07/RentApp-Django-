# Generated by Django 3.0.8 on 2020-08-22 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rentrecords'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rentrecords',
            old_name='Electricity',
            new_name='Electricity_Units',
        ),
        migrations.AddField(
            model_name='rentrecords',
            name='Electricity_Rate',
            field=models.IntegerField(default=15),
        ),
    ]
