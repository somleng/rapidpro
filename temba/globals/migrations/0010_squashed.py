# Generated by Django 4.0.8 on 2023-01-11 15:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("globals", "0009_squashed"),
        ("orgs", "0118_squashed"),
    ]

    operations = [
        migrations.AddField(
            model_name="global",
            name="org",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="globals", to="orgs.org"
            ),
        ),
    ]
