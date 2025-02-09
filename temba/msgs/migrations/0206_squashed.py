# Generated by Django 4.0.8 on 2023-01-11 15:35

import django.db.models.deletion
import django.db.models.expressions
import django.db.models.functions.text
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("tickets", "0044_squashed"),
        ("flows", "0315_squashed"),
        ("orgs", "0118_squashed"),
        ("channels", "0158_squashed"),
        ("msgs", "0205_squashed"),
        ("contacts", "0171_squashed"),
        ("schedules", "0018_squashed"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="systemlabelcount",
            name="org",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="system_labels", to="orgs.org"
            ),
        ),
        migrations.AddField(
            model_name="msg",
            name="broadcast",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.PROTECT, related_name="msgs", to="msgs.broadcast"
            ),
        ),
        migrations.AddField(
            model_name="msg",
            name="channel",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.PROTECT, related_name="msgs", to="channels.channel"
            ),
        ),
        migrations.AddField(
            model_name="msg",
            name="contact",
            field=models.ForeignKey(
                db_index=False, on_delete=django.db.models.deletion.PROTECT, related_name="msgs", to="contacts.contact"
            ),
        ),
        migrations.AddField(
            model_name="msg",
            name="contact_urn",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.PROTECT, related_name="msgs", to="contacts.contacturn"
            ),
        ),
        migrations.AddField(
            model_name="msg",
            name="flow",
            field=models.ForeignKey(
                db_index=False, null=True, on_delete=django.db.models.deletion.PROTECT, to="flows.flow"
            ),
        ),
        migrations.AddField(
            model_name="msg",
            name="labels",
            field=models.ManyToManyField(related_name="msgs", to="msgs.label"),
        ),
        migrations.AddField(
            model_name="msg",
            name="org",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="msgs", to="orgs.org"),
        ),
        migrations.AddField(
            model_name="media",
            name="created_by",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name="media",
            name="org",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="orgs.org"),
        ),
        migrations.AddField(
            model_name="media",
            name="original",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, related_name="alternates", to="msgs.media"
            ),
        ),
        migrations.AddField(
            model_name="labelcount",
            name="label",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="counts", to="msgs.label"
            ),
        ),
        migrations.AddField(
            model_name="label",
            name="created_by",
            field=models.ForeignKey(
                help_text="The user which originally created this item",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_creations",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="label",
            name="folder",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.PROTECT, related_name="children", to="msgs.label"
            ),
        ),
        migrations.AddField(
            model_name="label",
            name="modified_by",
            field=models.ForeignKey(
                help_text="The user which last modified this item",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_modifications",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="label",
            name="org",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="msgs_labels", to="orgs.org"
            ),
        ),
        migrations.AddField(
            model_name="exportmessagestask",
            name="created_by",
            field=models.ForeignKey(
                help_text="The user which originally created this item",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_creations",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="exportmessagestask",
            name="label",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to="msgs.label"),
        ),
        migrations.AddField(
            model_name="exportmessagestask",
            name="modified_by",
            field=models.ForeignKey(
                help_text="The user which last modified this item",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_modifications",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="exportmessagestask",
            name="org",
            field=models.ForeignKey(
                help_text="The organization of the user.",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(class)ss",
                to="orgs.org",
            ),
        ),
        migrations.AddField(
            model_name="exportmessagestask",
            name="with_fields",
            field=models.ManyToManyField(related_name="%(class)s_exports", to="contacts.contactfield"),
        ),
        migrations.AddField(
            model_name="exportmessagestask",
            name="with_groups",
            field=models.ManyToManyField(related_name="%(class)s_exports", to="contacts.contactgroup"),
        ),
        migrations.AddField(
            model_name="broadcastmsgcount",
            name="broadcast",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="counts", to="msgs.broadcast"
            ),
        ),
        migrations.AddField(
            model_name="broadcast",
            name="channel",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to="channels.channel"),
        ),
        migrations.AddField(
            model_name="broadcast",
            name="contacts",
            field=models.ManyToManyField(related_name="addressed_broadcasts", to="contacts.contact"),
        ),
        migrations.AddField(
            model_name="broadcast",
            name="created_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="broadcast_creations",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="broadcast",
            name="groups",
            field=models.ManyToManyField(related_name="addressed_broadcasts", to="contacts.contactgroup"),
        ),
        migrations.AddField(
            model_name="broadcast",
            name="modified_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="broadcast_modifications",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="broadcast",
            name="org",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="orgs.org"),
        ),
        migrations.AddField(
            model_name="broadcast",
            name="parent",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.PROTECT, related_name="children", to="msgs.broadcast"
            ),
        ),
        migrations.AddField(
            model_name="broadcast",
            name="schedule",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="broadcast",
                to="schedules.schedule",
            ),
        ),
        migrations.AddField(
            model_name="broadcast",
            name="ticket",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.PROTECT, related_name="broadcasts", to="tickets.ticket"
            ),
        ),
        migrations.AddField(
            model_name="broadcast",
            name="urns",
            field=models.ManyToManyField(related_name="addressed_broadcasts", to="contacts.contacturn"),
        ),
        migrations.AlterIndexTogether(
            name="systemlabelcount",
            index_together={("org", "label_type")},
        ),
        migrations.AddIndex(
            model_name="msg",
            index=models.Index(
                condition=models.Q(("direction", "O"), ("next_attempt__isnull", False), ("status__in", ("P", "E"))),
                fields=["next_attempt", "created_on", "id"],
                name="msgs_outgoing_to_retry",
            ),
        ),
        migrations.AddIndex(
            model_name="msg",
            index=models.Index(
                condition=models.Q(("direction", "O"), ("status__in", ("W", "S", "D")), ("visibility", "V")),
                fields=["org", "-sent_on", "-id"],
                name="msgs_outgoing_visible_sent",
            ),
        ),
        migrations.AddConstraint(
            model_name="msg",
            constraint=models.CheckConstraint(
                check=models.Q(("sent_on__isnull", True), ("status__in", ("W", "S", "D")), _negated=True),
                name="no_sent_status_without_sent_on",
            ),
        ),
        migrations.AddConstraint(
            model_name="label",
            constraint=models.UniqueConstraint(
                django.db.models.expressions.F("org"),
                django.db.models.functions.text.Lower("name"),
                name="unique_label_names",
            ),
        ),
        migrations.AddIndex(
            model_name="broadcast",
            index=models.Index(
                condition=models.Q(("is_active", True), ("schedule__isnull", True)),
                fields=["org", "-created_on", "-id"],
                name="msgs_broadcasts_api",
            ),
        ),
        migrations.AddIndex(
            model_name="broadcast",
            index=models.Index(
                condition=models.Q(("is_active", True), ("schedule__isnull", False)),
                fields=["org", "-created_on"],
                name="msgs_broadcasts_scheduled",
            ),
        ),
    ]
