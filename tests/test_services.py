from datetime import datetime, timezone
from unittest.mock import call, patch

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

# =================================================
#  CREATING TESTS
# =================================================


def test_create_subject_salva_e_retorna_objeto():
    with patch("services.save_subject") as save:
        subject = create_subject("Biologia")

    assert subject.name == "Biologia"
    assert subject.id is not None
    assert subject.created_at == subject.updated_at
    assert subject.created_at.tzinfo == timezone.utc
    save.assert_called_once_with(subject)


def test_create_topic_salva_e_retorna_objeto():
    subject_id = "subject-1"
    subject = Subject(subject_id, "Biologia", None, None)
    with (
        patch("services.find_subject", return_value=subject) as find,
        patch("services.save_topic") as save,
    ):
        topic = create_topic(subject_id, "Células")

    assert topic.name == "Células"
    assert topic.subject_id == subject_id
    assert topic.id is not None
    assert topic.created_at == topic.updated_at
    find.assert_called_once_with(subject_id)
    save.assert_called_once_with(topic)


def test_create_note_salva_e_retorna_objeto():
    topic_id = "topic-1"
    topic = Topic(topic_id, "Células", "subject-1", None, None)
    with (
        patch("services.find_topic", return_value=topic) as find,
        patch("services.save_note") as save,
    ):
        note = create_note(topic_id, "Membrana", "Resumo da membrana")

    assert note.title == "Membrana"
    assert note.content == "Resumo da membrana"
    assert note.topic_id == topic_id
    assert note.id is not None
    assert note.created_at == note.updated_at
    find.assert_called_once_with(topic_id)
    save.assert_called_once_with(note)

# =================================================
#  UPDATING TESTS
# =================================================

def test_update_subject_atualiza_e_persiste():
    subject = Subject("subject-1", "Biologia", None, datetime(2024, 1, 1, tzinfo=timezone.utc))
    with (
        patch("services.find_subject", return_value=subject),
        patch("services.repository_update_subject") as save,
    ):
        result = update_subject(subject.id, "Biologia celular")

    assert result is subject
    assert subject.name == "Biologia celular"
    assert subject.updated_at > datetime(2024, 1, 1, tzinfo=timezone.utc)
    save.assert_called_once_with(subject)


def test_update_subject_sem_alteracao_nao_persiste():
    subject = Subject("subject-1", "Biologia", None, None)
    with (
        patch("services.find_subject", return_value=subject),
        patch("services.repository_update_subject") as save,
    ):
        result = update_subject(subject.id, "Biologia")

    assert result is subject
    save.assert_not_called()


def test_update_topic_atualiza_e_persiste():
    topic = Topic("topic-1", "Células", "subject-1", None, None)
    with (
        patch("services.find_topic", return_value=topic),
        patch("services.repository_update_topic") as save,
    ):
        result = update_topic(topic.id, "Organelas")

    assert result is topic
    assert topic.name == "Organelas"
    assert topic.updated_at.tzinfo == timezone.utc
    save.assert_called_once_with(topic)


def test_update_note_atualiza_titulo_conteudo_e_persiste():
    note = Note("note-1", "Rascunho", "Texto antigo", "topic-1", None, None)
    with (
        patch("services.find_note", return_value=note),
        patch("services.repository_update_note") as save,
    ):
        result = update_note(note.id, "Resumo", "Texto novo")

    assert result is note
    assert note.title == "Resumo"
    assert note.content == "Texto novo"
    assert note.updated_at.tzinfo == timezone.utc
    save.assert_called_once_with(note)

# =================================================
#  DELETE TESTS
# =================================================

def test_delete_subject_remove_e_retorna_subject():
    subject = Subject("subject-1", "Biologia", None, None)
    with (
        patch("services.find_subject", return_value=subject),
        patch("services.repository_find_topics_by_subject", return_value=[]),
        patch("services.repository_delete_subject") as remove,
    ):
        result = delete_subject(subject.id)

    assert result is subject
    remove.assert_called_once_with(subject.id)


def test_delete_topic_remove_e_retorna_topic():
    topic = Topic("topic-1", "Células", "subject-1", None, None)
    with (
        patch("services.find_topic", return_value=topic),
        patch("services.repository_find_notes_by_topic", return_value=[]),
        patch("services.repository_delete_topic") as remove,
    ):
        result = delete_topic(topic.id)

    assert result is topic
    remove.assert_called_once_with(topic.id)


def test_delete_note_remove_e_retorna_note():
    note = Note("note-1", "Resumo", "Texto", "topic-1", None, None)
    with (
        patch("services.find_note", return_value=note),
        patch("services.repository_delete_note") as remove,
    ):
        result = delete_note(note.id)

    assert result is note
    remove.assert_called_once_with(note.id)


def test_delete_subject_apaga_topicos_em_cascata():
    subject = Subject("subject-1", "Biologia", None, None)
    topics = [
        Topic("topic-1", "Células", subject.id, None, None),
        Topic("topic-2", "Genética", subject.id, None, None),
    ]
    with (
        patch("services.find_subject", return_value=subject),
        patch("services.repository_find_topics_by_subject", return_value=topics),
        patch("services.delete_topic") as remove_topic,
        patch("services.repository_delete_subject") as remove_subject,
    ):
        delete_subject(subject.id)

    assert remove_topic.call_args_list == [call("topic-1"), call("topic-2")]
    remove_subject.assert_called_once_with(subject.id)


def test_delete_topic_apaga_notas_em_cascata():
    topic = Topic("topic-1", "Células", "subject-1", None, None)
    notes = [
        Note("note-1", "Membrana", "Texto 1", topic.id, None, None),
        Note("note-2", "Núcleo", "Texto 2", topic.id, None, None),
    ]
    with (
        patch("services.find_topic", return_value=topic),
        patch("services.repository_find_notes_by_topic", return_value=notes),
        patch("services.delete_note") as remove_note,
        patch("services.repository_delete_topic") as remove_topic,
    ):
        delete_topic(topic.id)

    assert remove_note.call_args_list == [call("note-1"), call("note-2")]
    remove_topic.assert_called_once_with(topic.id)

# =================================================================

def test_create_topic_com_subject_inexistente():
    with patch("services.find_subject", return_value=None):
        with pytest.raises(ValueError, match="Subject .* não encontrado"):
            create_topic("id-que-nao-existe", "Topic inválido")


def test_create_note_com_topic_inexistente():
    with patch("services.find_topic", return_value=None):
        with pytest.raises(ValueError, match="Topic .* não encontrado"):
            create_note("id-que-nao-existe", "Note inválida", "Conteúdo inválido")


@pytest.mark.parametrize(
    ("find_name", "operation", "entity_id", "message"),
    [
        ("find_subject", update_subject, "subject-404", "Subject"),
        ("find_topic", update_topic, "topic-404", "Topic"),
        ("find_note", update_note, "note-404", "Note"),
    ],
)
def test_update_com_entidade_inexistente_levanta_value_error(
    find_name, operation, entity_id, message
):
    with patch(f"services.{find_name}", return_value=None):
        with pytest.raises(ValueError, match=f"{message} .* não encontrado"):
            if operation is update_note:
                operation(entity_id, "Título", "Conteúdo")
            else:
                operation(entity_id, "Nome")


@pytest.mark.parametrize(
    ("find_name", "operation", "entity_id", "message"),
    [
        ("find_subject", delete_subject, "subject-404", "Subject"),
        ("find_topic", delete_topic, "topic-404", "Topic"),
        ("find_note", delete_note, "note-404", "Note"),
    ],
)
def test_delete_com_entidade_inexistente_levanta_value_error(
    find_name, operation, entity_id, message
):
    with patch(f"services.{find_name}", return_value=None):
        with pytest.raises(ValueError, match=f"{message} .* não encontrado"):
            operation(entity_id)
