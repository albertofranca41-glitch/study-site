import os
import mysql.connector
from dotenv import load_dotenv
from models import Subject

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

def save_topic():
    ...

def find_topic():
    ...

def update_topic():
    ...

def delete_topic():
    ...

# ===========================================
#   NOTE OPERATIONS
# ===========================================~

def save_note():
    ...

def find_note():
    ...

def update_note():
    ...

def delete_topic():
    ...