import logging
import sqlite3

from src.config import *


def create_db():
    # читаємо файл зі скриптом для створення БД
    with open('sql/students.sql', 'r') as f:
        sql = f.read()

    # створюємо з'єднання з БД (якщо файлу з БД немає, він буде створений)
    with sqlite3.connect(DATABASE) as con:
        logging.info(f'Created a new database named: {DATABASE}')
        cur = con.cursor()
        # виконуємо скрипт із файлу, який створить таблиці в БД
        cur.executescript(sql)
        logging.info(f'Created a table structure in the {DATABASE} database')


if __name__ == "__main__":
    create_db()
