# Generated by Django 4.1.7 on 2023-03-02 21:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("msgs", "0226_msg_created_by"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="msg",
            index=models.Index(
                condition=models.Q(("external_id__isnull", False)),
                fields=["channel_id", "external_id"],
                name="msgs_by_external_id",
            ),
        ),
        migrations.RunSQL("DROP INDEX msgs_msg_channel_external_id_not_null;"),
    ]
