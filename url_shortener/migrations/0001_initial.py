# Generated by Django 4.1.7 on 2023-02-20 12:25

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ShortUrl",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("description", models.CharField(max_length=500)),
                ("short_url", models.CharField(max_length=15)),
                ("original_url", models.CharField(max_length=1000)),
                ("add_date", models.DateTimeField(auto_now_add=True)),
                ("update_date", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
