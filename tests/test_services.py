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

def test_create_subject_...():
    ...


# ---------------- UPDATE ----------------

def test_update_subject_...():
    ...


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
