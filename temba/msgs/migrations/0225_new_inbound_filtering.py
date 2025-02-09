# Generated by Django 4.0.9 on 2023-02-27 22:05

from django.db import migrations, models

SQL = """
----------------------------------------------------------------------
-- Determines the (mutually exclusive) system label for a msg record
----------------------------------------------------------------------
CREATE OR REPLACE FUNCTION temba_msg_determine_system_label(_msg msgs_msg) RETURNS CHAR(1) AS $$
BEGIN
  IF _msg.direction = 'I' THEN
    -- incoming IVR messages aren't part of any system labels
    IF _msg.msg_type = 'V' THEN
      RETURN NULL;
    END IF;

    IF _msg.visibility = 'V' AND _msg.status = 'H' AND _msg.flow_id IS NULL THEN
      RETURN 'I';
    ELSIF _msg.visibility = 'V' AND _msg.status = 'H' AND _msg.flow_id IS NOT NULL THEN
      RETURN 'W';
    ELSIF _msg.visibility = 'A'  AND _msg.status = 'H' THEN
      RETURN 'A';
    END IF;
  ELSE
    IF _msg.VISIBILITY = 'V' THEN
      IF _msg.status = 'I' OR _msg.status = 'Q' OR _msg.status = 'E' THEN
        RETURN 'O';
      ELSIF _msg.status = 'W' OR _msg.status = 'S' OR _msg.status = 'D' THEN
        RETURN 'S';
      ELSIF _msg.status = 'F' THEN
        RETURN 'X';
      END IF;
    END IF;
  END IF;

  RETURN NULL; -- might not match any label
END;
$$ LANGUAGE plpgsql;

DROP INDEX msgs_msg_visibility_type_created_id_where_inbound;
"""


class Migration(migrations.Migration):
    dependencies = [
        ("msgs", "0224_msg_msgs_api_incoming"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="msg",
            index=models.Index(
                condition=models.Q(
                    ("direction", "I"),
                    ("flow__isnull", True),
                    ("msg_type__in", ("I", "F", "T")),
                    ("status", "H"),
                    ("visibility", "V"),
                ),
                fields=["org", "-created_on", "-id"],
                name="msgs_inbox",
            ),
        ),
        migrations.AddIndex(
            model_name="msg",
            index=models.Index(
                condition=models.Q(
                    ("direction", "I"),
                    ("flow__isnull", False),
                    ("msg_type__in", ("I", "F", "T")),
                    ("status", "H"),
                    ("visibility", "V"),
                ),
                fields=["org", "-created_on", "-id"],
                name="msgs_flows",
            ),
        ),
        migrations.AddIndex(
            model_name="msg",
            index=models.Index(
                condition=models.Q(
                    ("direction", "I"), ("msg_type__in", ("I", "F", "T")), ("status", "H"), ("visibility", "A")
                ),
                fields=["org", "-created_on", "-id"],
                name="msgs_archived",
            ),
        ),
        migrations.RunSQL(SQL),
    ]
