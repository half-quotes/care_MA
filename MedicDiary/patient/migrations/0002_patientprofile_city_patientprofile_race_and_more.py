# Generated by Django 4.1.7 on 2023-04-26 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("patient", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="patientprofile",
            name="city",
            field=models.TextField(default="brown", max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="patientprofile",
            name="race",
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name="labreports",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="patientprofile",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="patientvitals",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="records",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
