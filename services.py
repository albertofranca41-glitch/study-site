import uuid
from datetime import datetime, timezone

from models import Subject, Topic, Note

# ===========================================
#   READ
# ===========================================

def find_subject(subjects, subject_id):
    for subject in subjects:
        if subject.id == subject_id:
            return subject

def find_topic(topics, topic_id):
    for topic in topics:
        if topic.id == topic_id:
            return topic

def find_note(notes, note_id):
    for note in notes:
        if note.id == note_id:
            return note

# ===========================================
#   CREATE
# ===========================================

def create_subject(subjects, name):
    now = datetime.now(timezone.utc)

    subject = Subject(
        uuid.uuid4(),
        name,
        now,
        now
    )

    subjects.append(subject)

    return subject


def create_topic(subjects, topics, subject_id, name):
    subject = find_subject(subjects, subject_id)

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

    topics.append(topic)

    return topic


def create_note(topics, notes, topic_id, title, content):
    topic = find_topic(topics, topic_id)

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

    notes.append(note)

    return note


# ===========================================
#   UPDATE
# ===========================================

def update_subject(subjects, subject_id, name):
    subject = find_subject(subjects, subject_id)

    if subject is None:
        raise ValueError(f"Subject {subject_id} não encontrado")
       
    if subject.name != name:
        now = datetime.now(timezone.utc)
        subject.name = name
        subject.updated_at = now

def update_topic(topics, topic_id, name):
    topic = find_topic(topics, topic_id)

    if topic is None:
        raise ValueError(f"Topic {topic_id} não encontrado")

    if topic.name != name:
        now = datetime.now(timezone.utc)
        topic.name = name
        topic.updated_at = now

def update_note(notes, note_id, title, content):
    note = find_note(notes, note_id)

    if note is None:
        raise ValueError(f"Note {note_id} não encontrado")

    if note.title != title or note.content != content:
        now = datetime.now(timezone.utc)
        note.title = title
        note.content = content
        note.updated_at = now

# ===========================================
#   DELETE
# ===========================================

def delete_subject(subjects, topics, notes, subject_id):
    subject = find_subject(subjects, subject_id)

    if subject is None:
        raise ValueError(f"Subject {subject_id} não encontrado")

    related_topics = []

    for topic in topics:
        if topic.subject_id == subject_id:
            related_topics.append(topic)

    for topic in related_topics:
        delete_topic(topics, notes, topic.id)

    subjects.remove(subject)


def delete_topic(topics, notes, topic_id):
    topic = find_topic(topics, topic_id)

    if topic is None:
        raise ValueError(f"Topic {topic_id} não encontrado")

    related_notes = []

    for note in notes:
        if note.topic_id == topic_id:
            related_notes.append(note)

    for note in related_notes:
        notes.remove(note)

    topics.remove(topic)

def delete_note(notes, note_id):
    note = find_note(notes, note_id)

    if note is None:
        raise ValueError(f"Note {note_id} não encontrado")

    notes.remove(note)