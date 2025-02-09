# Generated by Django 4.1.7 on 2023-03-14 22:27

import mptt.fields

import django.contrib.gis.db.models.fields
import django.db.models.deletion
import django.db.models.functions.text
from django.db import migrations, models

SQL = """
DROP INDEX locations_adminboundary_name;
DROP INDEX locations_boundaryalias_name;
"""


class Migration(migrations.Migration):
    dependencies = [
        ("orgs", "0122_alter_org_config"),
        ("sql", "0005_squashed"),
        ("locations", "0027_squashed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="adminboundary",
            name="level",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="adminboundary",
            name="name",
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name="adminboundary",
            name="osm_id",
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name="adminboundary",
            name="parent",
            field=mptt.fields.TreeForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="children",
                to="locations.adminboundary",
            ),
        ),
        migrations.AlterField(
            model_name="adminboundary",
            name="path",
            field=models.CharField(max_length=768),
        ),
        migrations.AlterField(
            model_name="adminboundary",
            name="simplified_geometry",
            field=django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name="boundaryalias",
            name="boundary",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="aliases", to="locations.adminboundary"
            ),
        ),
        migrations.AlterField(
            model_name="boundaryalias",
            name="org",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="orgs.org"),
        ),
        migrations.AddIndex(
            model_name="adminboundary",
            index=models.Index(django.db.models.functions.text.Upper("name"), name="adminboundaries_by_name"),
        ),
        migrations.AddIndex(
            model_name="boundaryalias",
            index=models.Index(django.db.models.functions.text.Upper("name"), name="boundaryaliases_by_name"),
        ),
        migrations.RunSQL(SQL),
    ]
