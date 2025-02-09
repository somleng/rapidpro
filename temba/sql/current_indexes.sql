-- Generated by collect_sql on 2023-03-16 15:29 UTC

CREATE INDEX IF NOT EXISTS campaigns_eventfire_fired_not_null_idx on campaigns_eventfire(fired) WHERE fired IS NOT NULL;

CREATE UNIQUE INDEX campaigns_eventfire_unfired_unique
ON campaigns_eventfire (event_id, contact_id, (fired IS NULL))
WHERE fired IS NULL;

-- indexes for fast fetching of android channels by last seen
CREATE INDEX IF NOT EXISTS channels_channel_android_last_seen_active
ON channels_channel(last_seen ASC NULLS LAST) WHERE channel_type = 'A' and is_active = True;

-- index for fast fetching of unsquashed rows
CREATE INDEX channels_channelcount_unsquashed
ON channels_channelcount(channel_id, count_type, day) WHERE NOT is_squashed;

CREATE INDEX channels_channellog_channel_created_on
ON channels_channellog(channel_id, created_on desc);

CREATE INDEX contacts_contact_modified_on ON contacts_contact(modified_on);

CREATE INDEX contacts_contact_org_modified_id_active
ON contacts_contact (org_id, modified_on DESC, id DESC)
WHERE is_active = true;

CREATE INDEX contacts_contact_org_modified_id_inactive
ON contacts_contact (org_id, modified_on DESC, id DESC)
WHERE is_active = false;

-- index for fast fetching of unsquashed rows
CREATE INDEX contacts_contactgroupcount_unsquashed
ON contacts_contactgroupcount(group_id) WHERE NOT is_squashed;

CREATE INDEX contacts_contacturn_org_scheme_display ON contacts_contacturn (org_id, scheme, display)WHERE display IS NOT NULL;

CREATE INDEX contacts_contacturn_path ON contacts_contacturn (org_id, UPPER(path), contact_id);

-- indexes for fast fetching of unsquashed rows
CREATE INDEX flows_flowcategorycount_unsquashed
ON flows_flowcategorycount(flow_id, node_uuid, result_key, result_name, category_name) WHERE NOT is_squashed;

CREATE INDEX flows_flownodecount_unsquashed
ON flows_flownodecount(flow_id, node_uuid) WHERE NOT is_squashed;

CREATE INDEX flows_flowpathcount_unsquashed ON flows_flowpathcount(flow_id, from_uuid, to_uuid, period) WHERE NOT is_squashed;

CREATE INDEX flows_flowrun_flow_modified_id ON flows_flowrun (flow_id, modified_on DESC, id DESC);

CREATE INDEX flows_flowrun_flow_modified_id_where_responded ON flows_flowrun (flow_id, modified_on DESC, id DESC) WHERE responded = TRUE;

CREATE INDEX flows_flowrun_org_modified_id ON flows_flowrun (org_id, modified_on DESC, id DESC);

CREATE INDEX flows_flowrun_org_modified_id_where_responded ON flows_flowrun (org_id, modified_on DESC, id DESC) WHERE responded = TRUE;

-- for removing ended sessions
CREATE INDEX flows_flowsession_ended_on_not_null
ON flows_flowsession(ended_on ASC)
WHERE ended_on IS NOT NULL;

CREATE INDEX flows_flowsession_timeout
ON flows_flowsession(timeout_on) WHERE timeout_on IS NOT NULL AND status = 'W';

-- for finding the waiting session for a contact
CREATE INDEX flows_flowsession_waiting
ON flows_flowsession(contact_id)
WHERE status = 'W';

-- index for fast fetching of unsquashed rows
CREATE INDEX flows_flowstartcount_unsquashed
ON flows_flowstartcount(start_id) WHERE NOT is_squashed;

-- index for fast fetching of unsquashed rows
CREATE INDEX msgs_systemlabel_unsquashed
ON msgs_systemlabelcount(org_id, label_type) WHERE NOT is_squashed;

