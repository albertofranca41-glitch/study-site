import uuid
from datetime import datetime, timezone

from models import Subject, Topic, Note
from services import (
    find_subject,
    find_topic,
    find_note,
    create_subject,
    create_topic,
    create_note,
    update_subject,
    update_topic,
    update_note,
    delete_subject,
    delete_topic,
    delete_note,
)

# ===========================================
#   Objects for testing
# ===========================================

subjects = []


topics = []


notes = []
