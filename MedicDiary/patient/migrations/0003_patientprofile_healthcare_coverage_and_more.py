# Generated by Django 4.1.7 on 2023-05-01 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("patient", "0002_patientprofile_city_patientprofile_race_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="patientprofile",
            name="healthcare_coverage",
            field=models.IntegerField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name="patientprofile",
            name="healthcare_expenses",
            field=models.IntegerField(blank=True, default=0.0),
        ),
        migrations.AlterField(
            model_name="patientprofile",
            name="city",
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
