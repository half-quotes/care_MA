# Generated by Django 4.1.7 on 2023-05-02 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("patient", "0004_patientprofile_life_span"),
    ]

    operations = [
        migrations.AddField(
            model_name="patientprofile",
            name="county",
            field=models.CharField(blank=True, default="null", max_length=30),
        ),
    ]
