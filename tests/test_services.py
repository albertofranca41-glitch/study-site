from datetime import datetime, timezone
from unittest.mock import patch

import pytest

from models import Note, Subject, Topic
from services import (
    create_note,
    create_subject,
    create_topic,
    delete_note,
    delete_subject,
    delete_topic,
    update_note,
    update_subject,
    update_topic,
)


BASE_TIME = datetime(2024, 1, 1, tzinfo=timezone.utc)


# =================================================
# SUBJECT
# =================================================

# ---------------- CREATE ----------------

def test_create_subject():
    with patch("services.save_subject") as save:
        subject = create_subject("Filosofia")

    assert subject.name == "Filosofia"
    assert subject.id is not None
    assert subject.created_at == subject.updated_at
    assert subject.created_at.tzinfo == timezone.utc
    save.assert_called_once_with(subject)


# ---------------- UPDATE ----------------

def test_update_subject_updates():
    subject = Subject("subject-1", "Filosofia", BASE_TIME, BASE_TIME)

    with (
        patch("services.find_subject", return_value=subject),
        patch("services.repository_update_subject") as save,
    ):
        result = update_subject(subject.id, "Teologia")

    assert result is subject
    assert subject.name == "Teologia"
    assert subject.updated_at > BASE_TIME
    save.assert_called_once_with(subject)


def test_update_subject_no_change():
    subject = Subject("subject-1", "Filosofia", BASE_TIME, BASE_TIME)

    with (
        patch("services.find_subject", return_value=subject),
        patch("services.repository_update_subject") as save,
    ):
        result = update_subject(subject.id, "Filosofia")

    assert result is subject
    assert subject.updated_at == BASE_TIME
    save.assert_not_called()


def test_update_subject_not_found():
    with patch("services.find_subject", return_value=None), patch(
        "services.repository_update_subject"
    ) as save:
        with pytest.raises(ValueError, match="Subject subject-1 não encontrado"):
            update_subject("subject-1", "Teologia")

    save.assert_not_called()


# ---------------- DELETE ----------------

def test_delete_subject():
    subject = Subject("subject-1", "Filosofia", BASE_TIME, BASE_TIME)

    with (
        patch("services.find_subject", return_value=subject),
        patch("services.repository_find_topics_by_subject", return_value=[]),
        patch("services.repository_delete_subject") as delete,
    ):
        result = delete_subject(subject.id)

    assert result is subject
    delete.assert_called_once_with(subject.id)


def test_delete_subject_not_found():
    with patch("services.find_subject", return_value=None), patch(
        "services.repository_delete_subject"
    ) as delete:
        with pytest.raises(ValueError, match="Subject subject-1 não encontrado"):
            delete_subject("subject-1")

    delete.assert_not_called()


# =================================================
# TOPIC
# =================================================

# ---------------- CREATE ----------------

def test_create_topic():
    subject_id = "subject-1"
    subject = Subject(subject_id, "Filosofia", BASE_TIME, BASE_TIME)

    with (
        patch("services.find_subject", return_value=subject) as find,
        patch("services.save_topic") as save,
    ):
        topic = create_topic(subject_id, "Metafísica")

    assert topic.name == "Metafísica"
    assert topic.subject_id == subject_id
    assert topic.created_at == topic.updated_at
    assert topic.id is not None
    assert topic.created_at.tzinfo == timezone.utc
    find.assert_called_once_with(subject_id)
    save.assert_called_once_with(topic)


def test_create_topic_subject_not_found():
    with patch("services.find_subject", return_value=None), patch(
        "services.save_topic"
    ) as save:
        with pytest.raises(ValueError, match="Subject subject-1 não encontrado"):
            create_topic("subject-1", "Metafísica")

    save.assert_not_called()


# ---------------- UPDATE ----------------

def test_update_topic_updates():
    topic = Topic("topic-1", "Metafísica", "subject-1", BASE_TIME, BASE_TIME)

    with (
        patch("services.find_topic", return_value=topic),
        patch("services.repository_update_topic") as save,
    ):
        result = update_topic(topic.id, "Ética")

    assert result is topic
    assert topic.name == "Ética"
    assert topic.updated_at > BASE_TIME
    save.assert_called_once_with(topic)


def test_update_topic_no_change():
    topic = Topic("topic-1", "Metafísica", "subject-1", BASE_TIME, BASE_TIME)

    with (
        patch("services.find_topic", return_value=topic),
        patch("services.repository_update_topic") as save,
    ):
        result = update_topic(topic.id, "Metafísica")

    assert result is topic
    assert topic.updated_at == BASE_TIME
    save.assert_not_called()


def test_update_topic_not_found():
    with patch("services.find_topic", return_value=None), patch(
        "services.repository_update_topic"
    ) as save:
        with pytest.raises(ValueError, match="Topic topic-1 não encontrado"):
            update_topic("topic-1", "Ética")

    save.assert_not_called()


# ---------------- DELETE ----------------

def test_delete_topic():
    topic = Topic("topic-1", "Metafísica", "subject-1", BASE_TIME, BASE_TIME)

    with (
        patch("services.find_topic", return_value=topic),
        patch("services.repository_find_notes_by_topic", return_value=[]),
        patch("services.repository_delete_topic") as delete,
    ):
        result = delete_topic(topic.id)

    assert result is topic
    delete.assert_called_once_with(topic.id)


def test_delete_topic_not_found():
    with patch("services.find_topic", return_value=None), patch(
        "services.repository_delete_topic"
    ) as delete:
        with pytest.raises(ValueError, match="Topic topic-1 não encontrado"):
            delete_topic("topic-1")

    delete.assert_not_called()


# =================================================
# NOTE
# =================================================

# ---------------- CREATE ----------------

def test_create_note():
    topic_id = "topic-1"
    topic = Topic(topic_id, "Metafísica", "subject-1", BASE_TIME, BASE_TIME)

    with (
        patch("services.find_topic", return_value=topic) as find,
        patch("services.save_note") as save,
    ):
        note = create_note(topic_id, "Resumo", "Conteúdo da nota")

    assert note.title == "Resumo"
    assert note.content == "Conteúdo da nota"
    assert note.topic_id == topic_id
    assert note.created_at == note.updated_at
    assert note.created_at.tzinfo == timezone.utc
    assert note.id is not None
    find.assert_called_once_with(topic_id)
    save.assert_called_once_with(note)


def test_create_note_topic_not_found():
    with patch("services.find_topic", return_value=None), patch(
        "services.save_note"
    ) as save:
        with pytest.raises(ValueError, match="Topic topic-1 não encontrado"):
            create_note("topic-1", "Resumo", "Conteúdo da nota")

    save.assert_not_called()


# ---------------- UPDATE ----------------

def test_update_note_updates_when_title_changes():
    note = Note("note-1", "Rascunho", "Conteúdo", "topic-1", BASE_TIME, BASE_TIME)

    with (
        patch("services.find_note", return_value=note),
        patch("services.repository_update_note") as save,
    ):
        result = update_note(note.id, "Resumo", "Conteúdo")

    assert result is note
    assert note.title == "Resumo"
    assert note.content == "Conteúdo"
    assert note.updated_at > BASE_TIME
    save.assert_called_once_with(note)


def test_update_note_updates_when_content_changes():
    note = Note("note-1", "Resumo", "Antigo", "topic-1", BASE_TIME, BASE_TIME)

    with (
        patch("services.find_note", return_value=note),
        patch("services.repository_update_note") as save,
    ):
        result = update_note(note.id, "Resumo", "Novo")

    assert result is note
    assert note.title == "Resumo"
    assert note.content == "Novo"
    assert note.updated_at > BASE_TIME
    save.assert_called_once_with(note)


def test_update_note_no_change():
    note = Note("note-1", "Resumo", "Conteúdo", "topic-1", BASE_TIME, BASE_TIME)

    with (
        patch("services.find_note", return_value=note),
        patch("services.repository_update_note") as save,
    ):
        result = update_note(note.id, "Resumo", "Conteúdo")

    assert result is note
    assert note.updated_at == BASE_TIME
    save.assert_not_called()


def test_update_note_not_found():
    with patch("services.find_note", return_value=None), patch(
        "services.repository_update_note"
    ) as save:
        with pytest.raises(ValueError, match="Note note-1 não encontrado"):
            update_note("note-1", "Resumo", "Conteúdo")

    save.assert_not_called()


# ---------------- DELETE ----------------

def test_delete_note():
    note = Note("note-1", "Resumo", "Conteúdo", "topic-1", BASE_TIME, BASE_TIME)

    with (
        patch("services.find_note", return_value=note),
        patch("services.repository_delete_note") as delete,
    ):
        result = delete_note(note.id)

    assert result is note
    delete.assert_called_once_with(note.id)


def test_delete_note_not_found():
    with patch("services.find_note", return_value=None), patch(
        "services.repository_delete_note"
    ) as delete:
        with pytest.raises(ValueError, match="Note note-1 não encontrado"):
            delete_note("note-1")

    delete.assert_not_called()


# =================================================
# DEPENDENCY / CASCADE DELETE
# =================================================

# ---------------- SUBJECT ----------------

def test_delete_subject_removes_dependent_topics_and_notes():
    subject = Subject("subject-1", "Filosofia", BASE_TIME, BASE_TIME)
    topic = Topic("topic-1", "Metafísica", subject.id, BASE_TIME, BASE_TIME)
    note = Note("note-1", "Resumo", "Conteúdo", topic.id, BASE_TIME, BASE_TIME)

    with (
        patch("services.find_subject", return_value=subject),
        patch("services.repository_find_topics_by_subject", return_value=[topic]),
        patch("services.find_topic", return_value=topic),
        patch("services.repository_find_notes_by_topic", return_value=[note]),
        patch("services.find_note", return_value=note),
        patch("services.repository_delete_note") as delete_note_repo,
        patch("services.repository_delete_topic") as delete_topic_repo,
        patch("services.repository_delete_subject") as delete_subject_repo,
    ):
        result = delete_subject(subject.id)

    assert result is subject
    delete_note_repo.assert_called_once_with(note.id)
    delete_topic_repo.assert_called_once_with(topic.id)
    delete_subject_repo.assert_called_once_with(subject.id)


# ---------------- TOPIC ----------------

def test_delete_topic_removes_dependent_notes():
    topic = Topic("topic-1", "Metafísica", "subject-1", BASE_TIME, BASE_TIME)
    note = Note("note-1", "Resumo", "Conteúdo", topic.id, BASE_TIME, BASE_TIME)

    with (
        patch("services.find_topic", return_value=topic),
        patch("services.repository_find_notes_by_topic", return_value=[note]),
        patch("services.find_note", return_value=note),
        patch("services.repository_delete_note") as delete_note_repo,
        patch("services.repository_delete_topic") as delete_topic_repo,
    ):
        result = delete_topic(topic.id)

    assert result is topic
    delete_note_repo.assert_called_once_with(note.id)
    delete_topic_repo.assert_called_once_with(topic.id)
