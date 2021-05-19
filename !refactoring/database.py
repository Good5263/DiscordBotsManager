import sqlite3


def create_database(path):
    connection = sqlite3.connect(path)
    cursor = connection.cursor()

    tables = [
        "CREATE TABLE IF NOT EXISTS users (id INT PRIMARY KEY UNIQUE, login TEXT, hash_password TEXT, bot_group INT UNIQUE)",
        "CREATE TABLE IF NOT EXISTS groups (id INT PRIMARY KEY UNIQUE, bot_ids TEXT)",
        "CREATE TABLE IF NOT EXISTS bots (id INT PRIMARY KEY UNIQUE, name TEXT, token TEXT)"
    ]

    for table in tables:
        cursor.execute(table)

    connection.commit()
    connection.close()
