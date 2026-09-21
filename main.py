import uuid

# ===========================================
#   Creating the classes
# ===========================================

class Subject:
    def __init__(self, id, name, created_at, updated_at):
        self.id = id
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at


class Topic:
    def __init__(self, id, name, subject_id, created_at, updated_at):
        self.id = id
        self.name = name
        self.subject_id = subject_id
        self.created_at = created_at
        self.updated_at = updated_at


class Note:
    def __init__(self, id, title, content, topic_id, created_at, updated_at):
        self.id = id
        self.title = title
        self.content = content
        self.topic_id = topic_id
        self.created_at = created_at
        self.updated_at = updated_at

# ===========================================
#   Objects for testing
# ===========================================

subjects = []


topics = []


notes = []

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
    new_id = uuid.uuid4()

    subject = Subject(
        new_id,
        name,
        "2026-09-17",
        "2026-09-17"
    )

    subjects.append(subject)

    return subject


def create_topic(subjects, topics, subject_id, name):
    subject = find_subject(subjects, subject_id)

    if subject is None:
        raise ValueError(f"Subject {subject_id} não encontrado")

    new_id = uuid.uuid4()

    topic = Topic(
        new_id,
        name,
        subject_id,
        "2026-09-17",
        "2026-09-17"
    )

    topics.append(topic)

    return topic


def create_note(topics, notes, topic_id, title, content):
    topic = find_topic(topics, topic_id)

    if topic is None:
        raise ValueError(f"Topic {topic_id} não encontrado")

    new_id = uuid.uuid4()

    note = Note(
        new_id,
        title,
        content,
        topic_id,
        "2026-09-17",
        "2026-09-17"
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

    subject.name = name


def update_topic(topics, topic_id, name):
    topic = find_topic(topics, topic_id)

    if topic is None:
        raise ValueError(f"Topic {topic_id} não encontrado")

    topic.name = name

def update_note(notes, note_id, title, content):
    note = find_note(notes, note_id)

    if note is None:
        raise ValueError(f"Note {note_id} não encontrado")

    note.title = title
    note.content = content

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


filosofia = create_subject(subjects, "Filosofia")
programacao = create_subject(subjects, "Programacao")
teologia = create_subject(subjects, "Teologia")

aristoteles = create_topic(
    subjects,
    topics,
    filosofia.id,
    "Aristoteles"
)

python = create_topic(
    subjects,
    topics,
    programacao.id,
    "Python"
)

web = create_topic(
    subjects,
    topics,
    programacao.id,
    "Web"
)

forLoop = create_note(
    topics,
    notes,
    python.id,
    "For loop",
    "..."
)

metafisica = create_note(
    topics,
    notes,
    aristoteles.id,
    "Metafisica",
    "..."
)
