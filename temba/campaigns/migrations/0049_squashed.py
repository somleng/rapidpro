# Generated by Django 4.0.8 on 2023-01-11 15:35

import django.utils.timezone
from django.contrib.postgres.operations import HStoreExtension
from django.db import migrations, models

import temba.utils.fields
import temba.utils.models.fields
import temba.utils.uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        HStoreExtension(),
        migrations.CreateModel(
            name="Campaign",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "is_active",
                    models.BooleanField(
                        default=True, help_text="Whether this item is active, use this instead of deleting"
                    ),
                ),
                (
                    "created_on",
                    models.DateTimeField(
                        blank=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        help_text="When this item was originally created",
                    ),
                ),
                (
                    "modified_on",
                    models.DateTimeField(
                        blank=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        help_text="When this item was last modified",
                    ),
                ),
                ("uuid", models.UUIDField(default=temba.utils.uuid.uuid4, unique=True)),
                ("name", models.CharField(max_length=64, validators=[temba.utils.fields.NameValidator(64)])),
                ("is_system", models.BooleanField(default=False)),
                ("is_archived", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "Campaign",
                "verbose_name_plural": "Campaigns",
            },
        ),
        migrations.CreateModel(
            name="CampaignEvent",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "is_active",
                    models.BooleanField(
                        default=True, help_text="Whether this item is active, use this instead of deleting"
                    ),
                ),
                (
                    "created_on",
                    models.DateTimeField(
                        blank=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        help_text="When this item was originally created",
                    ),
                ),
                (
                    "modified_on",
                    models.DateTimeField(
                        blank=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        help_text="When this item was last modified",
                    ),
                ),
                ("uuid", models.UUIDField(default=temba.utils.uuid.uuid4, unique=True)),
                (
                    "event_type",
                    models.CharField(choices=[("F", "Flow Event"), ("M", "Message Event")], default="F", max_length=1),
                ),
                ("offset", models.IntegerField(default=0)),
                (
                    "unit",
                    models.CharField(
                        choices=[("M", "Minutes"), ("H", "Hours"), ("D", "Days"), ("W", "Weeks")],
                        default="D",
                        max_length=1,
                    ),
                ),
                (
                    "start_mode",
                    models.CharField(
                        choices=[("I", "Interrupt"), ("S", "Skip"), ("P", "Passive")], default="I", max_length=1
                    ),
                ),
                ("message", temba.utils.models.fields.TranslatableField(max_length=640, null=True)),
                ("delivery_hour", models.IntegerField(default=-1)),
            ],
            options={
                "verbose_name": "Campaign Event",
                "verbose_name_plural": "Campaign Events",
            },
        ),
        migrations.CreateModel(
            name="EventFire",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("scheduled", models.DateTimeField()),
                ("fired", models.DateTimeField(null=True)),
                (
                    "fired_result",
                    models.CharField(choices=[("F", "Fired"), ("S", "Skipped")], max_length=1, null=True),
                ),
            ],
            options={
                "ordering": ("scheduled",),
            },
        ),
    ]
