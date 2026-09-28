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
    subject = create_subject("Subject Name")
    print(f"Subject criado: {subject.name}")

    found_subject = find_subject(subject.id)
    print(f"Subject encontrado: {found_subject.name}")

    update_subject(subject.id, "Updated Subject")

    updated_subject = find_subject(subject.id)
    print(f"Subject atualizado: {updated_subject.name}")

    return subject.id


def topic_crud(subject_id):
    topic = create_topic(subject_id, "Topic Name")
    print(f"Topic criado: {topic.name}")

    found_topic = find_topic(topic.id)
    print(f"Topic encontrado: {found_topic.name}")

    update_topic(topic.id, "Updated Topic")

    updated_topic = find_topic(topic.id)
    print(f"Topic atualizado: {updated_topic.name}")

    return topic.id


def note_crud(topic_id):
    note = create_note(topic_id, "Note Title", "Note Content")
    print(f"Note criada: {note.title}")

    found_note = find_note(note.id)
    print(f"Note encontrada: {found_note.title}")

    update_note(note.id, "Updated Title", "Updated Content")

    updated_note = find_note(note.id)
    print(f"Note atualizada: {updated_note.title}")

    return note.id


# ===============================================
# DELETE FUNCTIONS
# ===============================================

def delete_subject_flow(subject_id):
    delete_subject(subject_id)


def delete_topic_flow(topic_id):
    delete_topic(topic_id)


def delete_note_flow(note_id):
    delete_note(note_id)


# ------------------------------------------------

if __name__ == "__main__":
    main()
