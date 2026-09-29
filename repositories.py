import os
import mysql.connector
from dotenv import load_dotenv
from models import Subject
from models import Topic
from models import Note

# Carrega as variáveis definidas no arquivo .env
load_dotenv()

# Cria uma conexão com o banco de dados por meio de uma funcao
def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

# ===========================================
#   SUBJECT OPERATIONS
# ===========================================

def save_subject(subject):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO Subjects (id, name, created_at, updated_at) "
                "VALUES (%s, %s, %s, %s)",
                (
                    str(subject.id),
                    subject.name,
                    subject.created_at,
                    subject.updated_at            
                )
            )

            connection.commit()
        finally:
            cursor.close()
    finally:
        connection.close()


def find_subject(subject_id):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        try:
            cursor.execute(
                " SELECT id, name, created_at, updated_at FROM Subjects WHERE id = %s;",
                (str(subject_id),)
            )

            result = cursor.fetchone()

            if result is None:
                return None

            subject_id, name, created_at, updated_at = result

            subject = Subject(
                subject_id,
                name, 
                created_at,
                updated_at
            )

        finally:
            cursor.close()
    finally:
        connection.close()

    return subject


def update_subject(subject):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "UPDATE Subjects SET name = %s, updated_at = %s WHERE id = %s",
                (
                    subject.name,
                    subject.updated_at,
                    str(subject.id)
                )
            )

            connection.commit()
        finally:
            cursor.close()
    finally:
        connection.close()

def delete_subject(subject_id):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        try:
            cursor.execute(
               "DELETE FROM Subjects WHERE id = %s",
               (str(subject_id),)
            )

            connection.commit()
        finally:
            cursor.close()
    finally:
        connection.close()

# ===========================================
#   TOPIC OPERATIONS
# ===========================================

def save_topic(topic):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO Topics (id, name, subject_id, created_at, updated_at)"
                "VALUES (%s, %s, %s, %s, %s)",
                (
                    str(topic.id),
                    topic.name,
                    str(topic.subject_id),
                    topic.created_at,
                    topic.updated_at
                )
            )

            connection.commit()
        finally:
            cursor.close()
    finally:
        connection.close()


def find_topics_by_subject(subject_id):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "SELECT id, name, subject_id, created_at, updated_at FROM Topics WHERE subject_id = %s;",
                (str(subject_id),)
            )

            results = cursor. fetchall()

            if not results:
                return []

            topics = []

            for result in results:
                topic_id, name, subject_id, created_at, updated_at = result

                topic = Topic(
                    topic_id,
                    name,
                    subject_id,
                    created_at,
                    updated_at
                )
                topics.append(topic)

        finally:
            cursor.close()
    finally:
        connection.close()

    return topics

def find_topic(topic_id):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        try:
            cursor.execute(
                " SELECT id, name, subject_id, created_at, updated_at FROM Topics WHERE id = %s;",
                (str(topic_id),)
            )

            result = cursor.fetchone()

            if result is None:
                return None

            topic_id, name, subject_id, created_at, updated_at = result

            topic = Topic(
                topic_id,
                name,
                subject_id,
                created_at,
                updated_at
            )

        finally:
            cursor.close()
    finally:
        connection.close()

    return topic


def update_topic(topic):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "UPDATE Topics SET name = %s, updated_at = %s WHERE id = %s",
                (
                    topic.name,
                    topic.updated_at,
                    str(topic.id)
                )

            )

            connection.commit()
        finally:
            cursor.close()
    finally:
        connection.close()

def delete_topic(topic_id):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        try:
            cursor.execute(
               "DELETE FROM Topics WHERE id = %s",
               (str(topic_id),)
            )

            connection.commit()
        finally:
            cursor.close()
    finally:
        connection.close()

# ===========================================
#   NOTE OPERATIONS
# ===========================================~

def save_note(note):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO Notes (id, title, content, topic_id, created_at, updated_at)"
                "VALUES (%s, %s, %s, %s, %s, %s)",
                (
                    str(note.id),
                    note.title,
                    note.content,
                    str(note.topic_id),
                    note.created_at,
                    note.updated_at
                )
            )

            connection.commit()
        finally:
            cursor.close()
    finally:
        connection.close()

def find_notes_by_topic(topic_id):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "SELECT id, title, content, topic_id, created_at, updated_at FROM Notes WHERE topic_id = %s;",
                (str(topic_id),)
            )

            results = cursor. fetchall()

            if not results:
                return []

            notes = []

            for result in results:
                note_id, title, content, topic_id, created_at, updated_at = result

                note = Note(
                    note_id,
                    title,
                    content,
                    topic_id,
                    created_at,
                    updated_at
                )
                notes.append(note)

        finally:
            cursor.close()
    finally:
        connection.close()

    return notes

def find_note(note_id):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        try:
            cursor.execute(
                " SELECT id, title, content, topic_id, created_at, updated_at FROM Notes WHERE id = %s;",
                (str(note_id),)
            )

            result = cursor.fetchone()

            if result is None:
                return None

            note_id, title, content, topic_id, created_at, updated_at = result

            note = Note(
                note_id, 
                title,
                content,
                topic_id,
                created_at,
                updated_at
            )

        finally:
            cursor.close()
    finally:
        connection.close()

    return note




def update_note(note):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        try:
            cursor.execute(
                 "UPDATE Notes SET title = %s, content = %s, updated_at = %s WHERE id = %s",
                (
                    note.title,
                    note.content,
                    note.updated_at,
                    str(note.id)
                )
            )

            connection.commit()
        finally:
            cursor.close()
    finally:
        connection.close()

def delete_note(note_id):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        try:
            cursor.execute(
               "DELETE FROM Notes WHERE id = %s",
               (str(note_id),)
            )

            connection.commit()
        finally:
            cursor.close()
    finally:
        connection.close()