# Generated by Django 4.0.8 on 2023-01-11 15:35

import pyotp
import timezone_field.fields

import django.contrib.auth.models
import django.contrib.postgres.fields
import django.contrib.postgres.validators
import django.utils.timezone
from django.db import migrations, models

import temba.utils.json
import temba.utils.models.fields
import temba.utils.text
import temba.utils.uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="BackupToken",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("token", models.CharField(default=temba.utils.text.generate_token, max_length=18, unique=True)),
                ("is_used", models.BooleanField(default=False)),
                ("created_on", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name="Invitation",
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
                ("email", models.EmailField(max_length=254)),
                ("secret", models.CharField(max_length=64, unique=True)),
                (
                    "user_group",
                    models.CharField(
                        choices=[
                            ("A", "Administrator"),
                            ("E", "Editor"),
                            ("V", "Viewer"),
                            ("T", "Agent"),
                            ("S", "Surveyor"),
                        ],
                        default="V",
                        max_length=1,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Org",
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
                ("name", models.CharField(max_length=128, verbose_name="Name")),
                ("brand", models.CharField(default="rapidpro", max_length=128, verbose_name="Brand")),
                ("plan", models.CharField(blank=True, max_length=16, null=True, verbose_name="Plan")),
                ("plan_start", models.DateTimeField(null=True)),
                ("plan_end", models.DateTimeField(null=True)),
                (
                    "stripe_customer",
                    models.CharField(
                        blank=True,
                        help_text="Our Stripe customer id for your organization",
                        max_length=32,
                        null=True,
                        verbose_name="Stripe Customer",
                    ),
                ),
                (
                    "language",
                    models.CharField(
                        choices=[
                            ("en-us", "English"),
                            ("cs", "Czech"),
                            ("es", "Spanish"),
                            ("fr", "French"),
                            ("mn", "Mongolian"),
                            ("pt-br", "Portuguese"),
                            ("ru", "Russian"),
                        ],
                        default="en-us",
                        help_text="The default website language for new users.",
                        max_length=64,
                        null=True,
                        verbose_name="Default Language",
                    ),
                ),
                ("timezone", timezone_field.fields.TimeZoneField(verbose_name="Timezone")),
                (
                    "date_format",
                    models.CharField(
                        choices=[("D", "DD-MM-YYYY"), ("M", "MM-DD-YYYY"), ("Y", "YYYY-MM-DD")],
                        default="D",
                        help_text="Whether day comes first or month comes first in dates",
                        max_length=1,
                        verbose_name="Date Format",
                    ),
                ),
                (
                    "config",
                    temba.utils.models.fields.JSONAsTextField(
                        default=dict,
                        help_text="More Organization specific configuration",
                        null=True,
                        verbose_name="Configuration",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        blank=True,
                        error_messages={"unique": "This slug is not available"},
                        max_length=255,
                        null=True,
                        unique=True,
                        verbose_name="Slug",
                    ),
                ),
                (
                    "features",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=32), default=list, size=None
                    ),
                ),
                (
                    "limits",
                    temba.utils.models.fields.JSONField(
                        decoder=temba.utils.json.TembaDecoder, default=dict, encoder=temba.utils.json.TembaEncoder
                    ),
                ),
                (
                    "api_rates",
                    temba.utils.models.fields.JSONField(
                        decoder=temba.utils.json.TembaDecoder, default=dict, encoder=temba.utils.json.TembaEncoder
                    ),
                ),
                (
                    "is_anon",
                    models.BooleanField(
                        default=False,
                        help_text="Whether this organization anonymizes the phone numbers of contacts within it",
                    ),
                ),
                (
                    "is_flagged",
                    models.BooleanField(default=False, help_text="Whether this organization is currently flagged."),
                ),
                (
                    "is_suspended",
                    models.BooleanField(default=False, help_text="Whether this organization is currently suspended."),
                ),
                (
                    "flow_languages",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=3),
                        default=list,
                        size=None,
                        validators=[django.contrib.postgres.validators.ArrayMinLengthValidator(1)],
                    ),
                ),
                (
                    "surveyor_password",
                    models.CharField(
                        default=None,
                        help_text="A password that allows users to register as surveyors",
                        max_length=128,
                        null=True,
                    ),
                ),
                ("released_on", models.DateTimeField(null=True)),
                ("deleted_on", models.DateTimeField(null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="OrgMembership",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("role_code", models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name="UserSettings",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "language",
                    models.CharField(
                        choices=[
                            ("en-us", "English"),
                            ("cs", "Czech"),
                            ("es", "Spanish"),
                            ("fr", "French"),
                            ("mn", "Mongolian"),
                            ("pt-br", "Portuguese"),
                            ("ru", "Russian"),
                        ],
                        default="en-us",
                        max_length=8,
                    ),
                ),
                ("otp_secret", models.CharField(default=pyotp.random_base32, max_length=16)),
                ("two_factor_enabled", models.BooleanField(default=False)),
                ("last_auth_on", models.DateTimeField(null=True)),
                ("external_id", models.CharField(max_length=128, null=True)),
                ("verification_token", models.CharField(max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("auth.user",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
