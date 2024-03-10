-- Table: group
DROP TABLE IF EXISTS students_groups;
CREATE TABLE students_groups (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	students_group INTEGER UNIQUE NOT NULL
);


-- Table: students
DROP TABLE IF EXISTS students;
CREATE TABLE students (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(255) UNIQUE NOT NULL,
	group_id INTEGER,
	FOREIGN KEY (group_id) REFERENCES students_groups (id)
		ON DELETE CASCADE
		ON UPDATE CASCADE
);


--Table:teachers
DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(255) UNIQUE NOT NULL
);


-- Table: subjects
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	subject_name VARCHAR(255) UNIQUE NOT NULL,
	teacher_id INTEGER,
	FOREIGN KEY (teacher_id) REFERENCES teachers (id)
		ON DELETE CASCADE
		ON UPDATE CASCADE
);


-- Table: grades
DROP TABLE IF EXISTS grades;
CREATE TABLE grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    subject_id INTEGER,
    date_of DATE NOT NULL,
    grade INTEGER NOT NULL,
    CHECK (grade BETWEEN 1 AND 5),
    FOREIGN KEY (student_id) REFERENCES students (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);