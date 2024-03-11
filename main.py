import sqlite3
import logging
from pathlib import Path

from src.create_db import create_db
from src.fill_data import *
from src.config import *


def init():
    db_path = Path("students.db")

    if not db_path.exists():
        create_db()

        insert_data_to_db(
            *prepare_data(
                *generate_fake_data(
                    NUMBER_STUDENTS,
                    NUMBER_TEACHERS,
                    NUMBER_SUBJECTS
                )
            )
        )


def execute_query(sql: str) -> list:
    with sqlite3.connect('students.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


def main():
    while True:
        input_data: str = input(
            "Enter the script number '1-10', or 'exit' to end the program: ")
        if input_data.isdigit():
            number = int(input_data)
            if number >= 0 and number <= 10:
                # читаємо файл зі скриптом для створення БД
                with open(f'sql/query_{number}.sql', 'r') as f:
                    sql = f.read()

                print(execute_query(sql))
            else:
                print("Wrong number. Enter a number '1-10'.")
        elif input_data.lower() == 'exit':
            break
        else:
            print(
                f"You have entered {input_data}. Please enter a number '1-10'."
                )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    init()
    main()
