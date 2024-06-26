# Generated by Django 5.0.3 on 2024-03-26 11:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_number', models.CharField(max_length=100)),
                ('client', models.CharField(default='0000', max_length=100)),
                ('agreement_number', models.CharField(default='0000', max_length=100)),
                ('client_project_number', models.CharField(default='0000', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_pit', models.IntegerField(default=1)),
                ('coordinator', models.CharField(max_length=200)),
                ('tech_name', models.CharField(max_length=200)),
                ('date_project', models.DateField(auto_now=True)),
                ('utility_found', models.BooleanField(default=True)),
                ('weather', models.CharField(default='Sunny', max_length=200)),
                ('timeproject', models.TimeField()),
                ('project_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.project')),
            ],
        ),
    ]
