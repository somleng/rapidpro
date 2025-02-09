# Generated by Django 4.0.8 on 2023-01-19 19:16

from django.db import migrations, transaction
from django.db.models import Q


def fix_lang(lang: str):  # pragma: no cover
    return lang if len(lang) == 3 else "und"


def populate_bcast_translations(apps, schema_editor):  # pragma: no cover
    Broadcast = apps.get_model("msgs", "Broadcast")

    num_updated = 0
    while True:
        batch = list(
            Broadcast.objects.filter(Q(translations__isnull=True) | Q(base_language="base")).only("id", "text")[:1000]
        )
        if not batch:
            break

        with transaction.atomic():
            for bcast in batch:
                bcast.translations = {fix_lang(lang): {"text": text} for lang, text in bcast.text.items()}
                bcast.base_language = fix_lang(bcast.base_language)
                bcast.save(update_fields=("translations", "base_language"))

        num_updated += len(batch)
        print(f"Updated {num_updated} broadcasts")


def reverse(apps, schema_editor):  # pragma: no cover
    pass


def apply_manual():  # pragma: no cover
    from django.apps import apps

    populate_bcast_translations(apps, None)


class Migration(migrations.Migration):
    dependencies = [
        ("msgs", "0207_broadcast_translations_alter_broadcast_status_and_more"),
    ]

    operations = [migrations.RunPython(populate_bcast_translations, reverse)]
