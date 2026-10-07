from datetime import datetime, timezone
from unittest.mock import patch

import pytest

from models import Subject, Topic, Note
from services import (
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
    subject = Subject(
        "subject-1",
        "Filosofia",
        None,
        datetime(2024, 1, 1, tzinfo=timezone.utc),
    )


    with (
        patch("services.find_subject", return_value=subject),
        patch("services.repository_update_subject") as save,
    ):

        result = update_subject(subject.id, "Teologia")

    assert result is subject
    assert subject.name == "Teologia"
    assert subject.updated_at > datetime(2024, 1, 1, tzinfo=timezone.utc)
    save.assert_called_once_with(subject)




# ---------------- DELETE ----------------

def test_delete_subject_...():
    ...


# =================================================
# TOPIC
# =================================================

# ---------------- CREATE ----------------

def test_create_topic_...():
    ...


# ---------------- UPDATE ----------------

def test_update_topic_...():
    ...


# ---------------- DELETE ----------------

def test_delete_topic_...():
    ...


# =================================================
# NOTE
# =================================================

# ---------------- CREATE ----------------

def test_create_note_...():
    ...


# ---------------- UPDATE ----------------

def test_update_note_...():
    ...


# ---------------- DELETE ----------------

def test_delete_note_...():
    ...


# =================================================
# DEPENDENCY / CASCADE DELETE
# =================================================

# ---------------- SUBJECT ----------------

def test_delete_subject_remove_topicos_dependentes_...():
    ...


# ---------------- TOPIC ----------------

def test_delete_topic_remove_notas_dependentes_...():
    ...
