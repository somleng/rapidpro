# Generated by Django 4.0.4 on 2022-08-12 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orgs", "0101_remove_org_administrators_remove_org_agents_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="org",
            name="brand",
            field=models.CharField(default="rapidpro.io", max_length=128, verbose_name="Brand"),
        ),
        migrations.AlterField(
            model_name="org",
            name="plan",
            field=models.CharField(default="topups", max_length=16, verbose_name="Plan"),
        ),
    ]
