# Generated by Django 4.0.7 on 2022-09-20 17:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ivr", "0020_add_call"),
        ("channels", "0150_remove_channelconnection_connection_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="channellog",
            name="call",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.PROTECT, related_name="channel_logs", to="ivr.call"
            ),
        ),
    ]
