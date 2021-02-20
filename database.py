import sqlite3


def create_database(path="data_files\data.sqlite"):
    connection = sqlite3.connect(path)
    cursor = connection.cursor()

    tables = [
        "CREATE TABLE IF NOT EXISTS users (login TEXT, password TEXT, group_bots INT PRIMARY KEY)",
        "CREATE TABLE IF NOT EXISTS groups (group_id INT PRIMARY KEY, bots TEXT)",
        "CREATE TABLE IF NOT EXISTS bots (ID INT PRIMARY KEY, name_bot TEXT, token TEXT)"
    ]

    for table in tables:
        cursor.execute(table)

    connection.commit()
    connection.close()
