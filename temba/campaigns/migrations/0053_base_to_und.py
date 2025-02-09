# Generated by Django 4.0.8 on 2023-01-20 00:10

from django.db import migrations


def migrate_base_to_und(apps, schema_editor):
    CampaignEvent = apps.get_model("campaigns", "CampaignEvent")

    num_updated = 0
    for event in CampaignEvent.objects.filter(event_type="M", message__has_key="base"):
        event.message["und"] = event.message["base"]
        del event.message["base"]
        event.save(update_fields=("message",))
        num_updated += 1

    if num_updated:
        print(f"Updated {num_updated} campaign events")


def reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [("campaigns", "0052_squashed")]

    operations = [migrations.RunPython(migrate_base_to_und, reverse)]
