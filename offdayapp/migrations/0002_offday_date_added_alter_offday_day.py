# Generated by Django 4.2 on 2024-09-21 21:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("offdayapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="offday",
            name="date_added",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="offday",
            name="day",
            field=models.CharField(max_length=10),
        ),
    ]
