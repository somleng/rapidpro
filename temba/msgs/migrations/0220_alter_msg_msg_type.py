# Generated by Django 4.0.9 on 2023-02-17 15:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("msgs", "0219_remove_broadcast_raw_urns"),
    ]

    operations = [
        migrations.AlterField(
            model_name="msg",
            name="msg_type",
            field=models.CharField(
                choices=[("I", "Inbox Message"), ("F", "Flow Message"), ("T", "Text Message"), ("V", "Voice Message")],
                max_length=1,
                null=True,
            ),
        ),
    ]
