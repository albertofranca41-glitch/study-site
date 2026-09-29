import uuid
from datetime import datetime, timezone

from models import Subject, Topic, Note
from repositories import save_subject
from repositories import find_subject as repository_find_subject
from repositories import update_subject as repository_update_subject
from repositories import delete_subject as repository_delete_subject
from repositories import save_topic
from repositories import find_topics_by_subject as repository_find_topics_by_subject
from repositories import find_topic as repository_find_topic
from repositories import update_topic as repository_update_topic
from repositories import delete_topic as repository_delete_topic
from repositories import save_note
from repositories import find_notes_by_topic as repository_find_notes_by_topic
from repositories import find_note as repository_find_note
from repositories import update_note as repository_update_note
from repositories import delete_note as repository_delete_note

# ===========================================
#   READ
# ===========================================

def find_subject(subject_id):
    return repository_find_subject(subject_id)

def find_topic(topic_id):
    return repository_find_topic(topic_id)

def find_note(note_id):
    return repository_find_note(note_id)

# ===========================================
#   CREATE
# ===========================================

def create_subject(name):
    now = datetime.now(timezone.utc)

    subject = Subject(
        uuid.uuid4(),
        name,
        now,
        now
    )

    save_subject(subject)

    return subject


def create_topic(subject_id, name):
    subject = find_subject(subject_id)

    if subject is None:
        raise ValueError(f"Subject {subject_id} não encontrado")

    now = datetime.now(timezone.utc)

    topic = Topic(
        uuid.uuid4(),
        name,
        subject_id,
        now,
        now
    )

    save_topic(topic)

    return topic


def create_note(topic_id, title, content):
    topic = find_topic(topic_id)

    if topic is None:
        raise ValueError(f"Topic {topic_id} não encontrado")

    now = datetime.now(timezone.utc)

    note = Note(
        uuid.uuid4(),
        title,
        content,
        topic_id,
        now,
        now
    )

    save_note(note)

    return note


# ===========================================
#   UPDATE
# ===========================================

def update_subject(subject_id, name):
    subject = find_subject(subject_id)

    if subject is None:
        raise ValueError(f"Subject {subject_id} não encontrado")
       
    if subject.name != name:
        now = datetime.now(timezone.utc)
        subject.name = name
        subject.updated_at = now

        repository_update_subject(subject)
    return subject

def update_topic(topic_id, name):
    topic = find_topic(topic_id)

    if topic is None:
        raise ValueError(f"Topic {topic_id} não encontrado")

    if topic.name != name:
        now = datetime.now(timezone.utc)
        topic.name = name
        topic.updated_at = now

        repository_update_topic(topic)
    return topic

def update_note(note_id, title, content):
    note = find_note(note_id)

    if note is None:
        raise ValueError(f"Note {note_id} não encontrado")

    if note.title != title or note.content != content:
        now = datetime.now(timezone.utc)
        note.title = title
        note.content = content
        note.updated_at = now

        repository_update_note(note)
    return note

# ===========================================
#   DELETE
# ===========================================

def delete_subject(subject_id):
    subject = find_subject(subject_id)

    if subject is None:
        raise ValueError(f"Subject {subject_id} não encontrado")

    topics = repository_find_topics_by_subject(subject_id)

    for topic in topics:
        delete_topic(topic.id)

    repository_delete_subject(subject_id)
    return subject



def delete_topic(topic_id):
    topic = find_topic(topic_id)

    if topic is None:
        raise ValueError(f"Topic {topic_id} não encontrado")
    
    notes = repository_find_notes_by_topic(topic_id)

    for note in notes:
        delete_note(note.id)
    
    repository_delete_topic(topic_id)    
    return topic 

def delete_note(note_id):
    note = find_note(note_id)

    if note is None:
        raise ValueError(f"Note {note_id} não encontrado")

    repository_delete_note(note_id)
    return note