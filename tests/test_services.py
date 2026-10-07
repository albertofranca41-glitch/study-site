import pytest

from services import create_subject
from services import create_topic
from services import create_note
from services import update_subject

def test_create_topic_with_invalid_subject():
    with pytest.raises(ValueError):
        create_topic(
            "id-que-nao-existe",
            "Topic inválido"
        )

def test_create_note_with_invalid_topic():
    with pytest.raises(ValueError):
        create_note(
            "id-que-nao-existe",
            "Note inválida",
            "Conteúdo inválido"
        )  

def test_update_invalid_subject():
    with pytest.raises(ValueError):
        update_subject(
            "id-invalido",
            "Subject invalido"
        )



