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

# ==============================================

subjects = []


topics = []


notes = []

# ===============================================
# CRUD OPERATIONS
# ===============================================

def main():
    subject_id = subject_crud()
    topic_id = topic_crud(subject_id)
    note_id = note_crud(topic_id)

    delete_note_flow(note_id)
    delete_topic_flow(topic_id)
    delete_subject_flow(subject_id)

def subject_crud():
    subject = create_subject(subjects, "Subject Name")
    print(subject.name)

    found_subject = find_subject(subjects, subject.id)
    print(found_subject.name)

    update_subject(subjects, subject.id, "Updated Subject")
    print(subject.name)
    return subject.id

def topic_crud(subject_id):
    topic = create_topic(subjects, topics, subject_id, "Topic Name")
    print(topic.name)

    found_topic = find_topic(topics, topic.id)
    print(found_topic.name)

    update_topic(topics, topic.id, "Updated Topic")
    print(topic.name)
    return topic.id

def note_crud(topic_id):

    note = create_note(topics, notes, topic_id, "Note Title", "Note Content")
    print(note.title)

    found_note = find_note(notes, note.id)
    print(found_note.title)

    update_note(notes, note.id, "Updated Title", "Updated Content")
    print(note.title)
    return note.id

# ===============================================
# DELETE FUNCTIONS
# ===============================================

def delete_subject_flow(subject_id):
    delete_subject(subjects, topics, notes, subject_id)

def delete_topic_flow(topic_id):
    delete_topic(topics, notes, topic_id)

def delete_note_flow(note_id):
    delete_note(notes, note_id)

# ------------------------------------------------

if __name__ == "__main__":
    main()