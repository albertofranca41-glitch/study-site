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

def test_update_subject_no_change():
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
        result = update_subject(subject.id, "Filosofia")

        assert result is subject
        assert subject.name == "Filosofia"
        save.assert_not_called()



# ---------------- DELETE ----------------

def test_delete_subject():
    subject = Subject(
        "subject-1",
        "Filosofia",
        None,
        datetime(2024, 1, 1, tzinfo=timezone.utc),
    )

    with (
        patch("services.find_subject", return_value=subject),
        patch("services.repository_delete_subject") as delete,
    ):
        result = delete_subject(subject.id)

    assert result is subject
    delete.assert_called_once_with(subject.id)


# =================================================
# TOPIC
# =================================================

# ---------------- CREATE ----------------

def test_create_topic():
    pass


# ---------------- UPDATE ----------------

def test_update_topic():
    pass


# ---------------- DELETE ----------------

def test_delete_topic():
    pass


# =================================================
# NOTE
# =================================================

# ---------------- CREATE ----------------

def test_create_note():
    pass


# ---------------- UPDATE ----------------

def test_update_note():
    pass


# ---------------- DELETE ----------------

def test_delete_note():
    pass


# =================================================
# DEPENDENCY / CASCADE DELETE
# =================================================

# ---------------- SUBJECT ----------------

def test_delete_subject_remove_topicos_dependentes():
    pass


# ---------------- TOPIC ----------------

def test_delete_topic_remove_notas_dependentes():
    pass
