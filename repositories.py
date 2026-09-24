import os
import mysql.connector
from dotenv import load_dotenv

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