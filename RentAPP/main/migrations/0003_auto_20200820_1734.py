# Generated by Django 3.0.8 on 2020-08-20 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200820_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers_model',
            name='total',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='customers_model',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=6),
        ),
    ]
