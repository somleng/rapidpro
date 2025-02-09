# Generated by Django 4.1.7 on 2023-04-20 21:16

from django.db import migrations

SQL = """
----------------------------------------------------------------------
-- Inserts a new assignee ticketcount row with the given values
----------------------------------------------------------------------
CREATE OR REPLACE FUNCTION temba_insert_ticketcount_for_assignee(_org_id INTEGER, _assignee_id INTEGER, status CHAR(1), _count INT) RETURNS VOID AS $$
BEGIN
    INSERT INTO tickets_ticketcount("org_id", "scope", "status", "count", "is_squashed")
    VALUES(_org_id, format('assignee:%s', coalesce(_assignee_id, 0)), status, _count, FALSE);
END;
$$ LANGUAGE plpgsql;


----------------------------------------------------------------------
-- Inserts a new topic ticketcount row with the given values
----------------------------------------------------------------------
CREATE OR REPLACE FUNCTION temba_insert_ticketcount_for_topic(_org_id INTEGER, _topic_id INTEGER, status CHAR(1), _count INT) RETURNS VOID AS $$
BEGIN
    INSERT INTO tickets_ticketcount("org_id", "scope", "status", "count", "is_squashed")
    VALUES(_org_id, format('topic:%s', _topic_id), status, _count, FALSE);
END;
$$ LANGUAGE plpgsql;


----------------------------------------------------------------------
-- Trigger procedure to update user and system labels on column changes
----------------------------------------------------------------------
CREATE OR REPLACE FUNCTION temba_ticket_on_change() RETURNS TRIGGER AS $$
BEGIN
  IF TG_OP = 'INSERT' THEN -- new ticket inserted
    PERFORM temba_insert_ticketcount_for_assignee(NEW.org_id, NEW.assignee_id, NEW.status, 1);
    PERFORM temba_insert_ticketcount_for_topic(NEW.org_id, NEW.topic_id, NEW.status, 1);

    IF NEW.status = 'O' THEN
      UPDATE contacts_contact SET ticket_count = ticket_count + 1, modified_on = NOW() WHERE id = NEW.contact_id;
    END IF;
  ELSIF TG_OP = 'UPDATE' THEN -- existing ticket updated
    IF OLD.assignee_id IS DISTINCT FROM NEW.assignee_id OR OLD.status != NEW.status THEN
      PERFORM temba_insert_ticketcount_for_assignee(OLD.org_id, OLD.assignee_id, OLD.status, -1);
      PERFORM temba_insert_ticketcount_for_assignee(NEW.org_id, NEW.assignee_id, NEW.status, 1);
    END IF;

    IF OLD.topic_id != NEW.topic_id OR OLD.status != NEW.status THEN
      PERFORM temba_insert_ticketcount_for_topic(OLD.org_id, OLD.topic_id, OLD.status, -1);
      PERFORM temba_insert_ticketcount_for_topic(NEW.org_id, NEW.topic_id, NEW.status, 1);
    END IF;

    IF OLD.status = 'O' AND NEW.status = 'C' THEN -- ticket closed
      UPDATE contacts_contact SET ticket_count = ticket_count - 1, modified_on = NOW() WHERE id = OLD.contact_id;
    ELSIF OLD.status = 'C' AND NEW.status = 'O' THEN -- ticket reopened
      UPDATE contacts_contact SET ticket_count = ticket_count + 1, modified_on = NOW() WHERE id = OLD.contact_id;
    END IF;
  ELSIF TG_OP = 'DELETE' THEN -- existing ticket deleted
    PERFORM temba_insert_ticketcount_for_assignee(OLD.org_id, OLD.assignee_id, OLD.status, -1);
    PERFORM temba_insert_ticketcount_for_topic(OLD.org_id, OLD.topic_id, OLD.status, -1);

    IF OLD.status = 'O' THEN -- open ticket deleted
      UPDATE contacts_contact SET ticket_count = ticket_count - 1, modified_on = NOW() WHERE id = OLD.contact_id;
    END IF;
  END IF;
  RETURN NULL;
END;
$$ LANGUAGE plpgsql;


DROP FUNCTION temba_insert_ticketcount(INTEGER, INTEGER, CHAR(1), INT);
"""


class Migration(migrations.Migration):
    dependencies = [
        ("tickets", "0050_ticketcount_trigger_update"),
    ]

    operations = [
        migrations.RemoveField(model_name="ticketcount", name="assignee"),
        migrations.RunSQL(SQL),
    ]
