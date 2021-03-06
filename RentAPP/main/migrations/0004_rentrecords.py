# Generated by Django 3.0.8 on 2020-08-22 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200820_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentRecords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Previous_Balance', models.IntegerField(default=0)),
                ('Rent', models.IntegerField(default=0)),
                ('Electricity', models.IntegerField(default=0, help_text='Units')),
                ('Other', models.IntegerField(help_text='Waste Dumping and Water')),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Customers_model')),
            ],
        ),
    ]
