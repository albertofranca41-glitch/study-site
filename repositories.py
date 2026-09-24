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

def save_subject(subject):
    connection = get_connection()
    cursor = connection.cursor()
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

    cursor.close()
    connection.close()

def find_subject(subject_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        " SELECT * FROM Subjects WHERE id = %s;",
        (str(subject_id),)
    )

    result = cursor.fetchone()

    if result is None:
        cursor.close()
        connection.close()
        return None

    subject_id, name, created_at, updated_at = result

    subject = Subject(
        subject_id,
        name, 
        created_at,
        updated_at
    )

    cursor.close()
    connection.close()

    return subject