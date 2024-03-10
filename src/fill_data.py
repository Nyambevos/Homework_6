from datetime import datetime
import faker
from random import randint
import sqlite3

NUMBER_STUDENTS = 50
NUMBER_GROUPS = 3
NUMBER_SUBJECTS = 8
NUMBER_TEACHERS = 5
NUMBER_EVALUATIONS = 20


def generate_fake_data(number_students, number_teachers, number_subjects) -> tuple:
    fake_students = []  # тут зберігатимемо студентів
    fake_teachers = []  # тут зберігатимемо викладачів
    fake_subjects = []  # тут зберігатимемо предмети

    fake_data = faker.Faker()

    # Створимо набір студентів у кількості number_students
    for _ in range(number_students):
        fake_students.append(fake_data.name())

    # Згенеруємо тепер number_teachers кількість викладачів'''
    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())

    # Та number_subjects набір предметів
    for _ in range(number_subjects):
        fake_subjects.append(fake_data.job())

    return fake_students, fake_teachers, fake_subjects


def prepare_data(students, teachers, subjects) -> tuple:
    for_groups = []

    for group in range(1, NUMBER_GROUPS + 1):
        for_groups.append((group,))

    for_students = []

    for student in students:
        for_students.append((student, randint(1, NUMBER_GROUPS)))

    for_teachers = []

    for teacher in teachers:
        for_teachers.append((teacher,))

    for_subjects = []

    for subject in subjects:
        for_subjects.append((subject, randint(1, NUMBER_TEACHERS)))

    for_grades = []

    for student_id in range(1, NUMBER_STUDENTS + 1):
        for _ in range(randint(1, NUMBER_EVALUATIONS)):
            grade_date = datetime(2023, randint(9, 12), randint(1, 30)).date()
            for_grades.append((student_id, randint(1, NUMBER_SUBJECTS), grade_date, randint(1, 5)))

    return for_groups, for_students, for_teachers, for_subjects, for_grades


def insert_data_to_db(groups, students, teachers, subjects, grades) -> None:
    # Створимо з'єднання з нашою БД та отримаємо об'єкт курсору для маніпуляцій з даними

    with sqlite3.connect('students.db') as con:

        cur = con.cursor()

        sql_to_groups = """INSERT INTO students_groups(students_group)
                               VALUES (?)"""

        cur.executemany(sql_to_groups, groups)

        sql_to_students = """INSERT INTO students(name, group_id)
                               VALUES (?, ?)"""

        cur.executemany(sql_to_students, students)

        sql_to_teachers = """INSERT INTO teachers(name)
                               VALUES (?)"""

        cur.executemany(sql_to_teachers, teachers)

        sql_to_subjects = """INSERT INTO subjects(subject_name, teacher_id)
                               VALUES (?, ?)"""

        cur.executemany(sql_to_subjects, subjects)

        # Останньою заповнюємо таблицю із зарплатами

        sql_to_grades = """INSERT INTO grades(student_id, subject_id, date_of, grade)
                                    VALUES (?, ?, ?, ?)"""

        # Вставляємо дані про зарплати

        cur.executemany(sql_to_grades, grades)

        # Фіксуємо наші зміни в БД

        con.commit()

if __name__ == "__main__":
    groups, students, teachers, subjects, evaluations = prepare_data(*generate_fake_data(NUMBER_STUDENTS, NUMBER_TEACHERS, NUMBER_SUBJECTS))

    insert_data_to_db(groups, students, teachers, subjects, evaluations)