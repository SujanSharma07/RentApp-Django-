# Generated by Django 3.0.8 on 2020-08-23 16:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rentrecords_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentrecords',
            name='info',
        ),
        migrations.AddField(
            model_name='customers_model',
            name='report',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.RentRecords'),
        ),
        migrations.AddField(
            model_name='rentrecords',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='customers_model',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]