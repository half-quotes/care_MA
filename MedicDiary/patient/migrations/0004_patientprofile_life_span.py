# Generated by Django 4.1.7 on 2023-05-01 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("patient", "0003_patientprofile_healthcare_coverage_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="patientprofile",
            name="life_span",
            field=models.IntegerField(blank=True, default=0.0),
        ),
    ]
