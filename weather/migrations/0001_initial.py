# Generated by Django 4.2.3 on 2023-10-23 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='meteoData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stn', models.IntegerField()),
                ('sdate', models.CharField(max_length=100)),
                ('RRR', models.FloatField()),
                ('Tmax', models.FloatField()),
                ('T2', models.FloatField()),
                ('soil_temp_mean', models.FloatField()),
                ('RH', models.FloatField()),
                ('AH', models.FloatField()),
                ('ff', models.FloatField()),
                ('dirn', models.CharField(max_length=100)),
                ('dp', models.FloatField()),
            ],
        ),
    ]
