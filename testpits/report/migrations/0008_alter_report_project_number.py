# Generated by Django 5.0.3 on 2024-03-28 15:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0007_alter_project_project_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='project_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='report.project'),
        ),
    ]
