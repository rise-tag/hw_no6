import sqlite3
from datetime import datetime


conn = sqlite3.connect('School.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    age INTEGER,
    grade TEXT NOT NULL,
    enrollment_date DATE DEFAULT CURRENT_DATE
)
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_name TEXT NOT NULL,
    teacher_name TEXT NOT NULL
)
''')


conn.commit()


def register_student():
    full_name = input("Введите полное имя студента: ")
    age = int(input("Введите возраст студента: "))
    grade = input("Введите класс студента: ")

    cursor.execute('''
    INSERT INTO students (full_name, age, grade)
    VALUES (?, ?, ?)
    ''', (full_name, age, grade))
    
    conn.commit()
    print("Студент успешно добавлен!")

def add_subject():
    subject_name = input("Введите название предмета: ")
    teacher_name = input("Введите имя учителя: ")

    cursor.execute('''
    INSERT INTO subjects (subject_name, teacher_name)
    VALUES (?, ?)
    ''', (subject_name, teacher_name))
    
    conn.commit()
    print("Предмет успешно добавлен!")


def get_students():
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    
    for student in students:
        print(student)

def get_subjects():
    cursor.execute('SELECT * FROM subjects')
    subjects = cursor.fetchall()
    
    for subject in subjects:
        print(subject)

def get_students_by_grade(grade):
    cursor.execute('SELECT * FROM students WHERE grade = ?', (grade,))
    students = cursor.fetchall()
    
    for student in students:
        print(student)


def update_student_age(student_id, new_age):
    cursor.execute('''
    UPDATE students
    SET age = ?
    WHERE id = ?
    ''', (new_age, student_id))
    
    conn.commit()
    print("Возраст студента успешно обновлен!")

def delete_student(student_id):
    cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
    
    conn.commit()
    print("Студент успешно удален!")


def get_student_count_by_grade():
    cursor.execute('''
    SELECT grade, COUNT(*) 
    FROM students 
    GROUP BY grade
    ''')
    grades = cursor.fetchall()
    
    for grade in grades:
        print(f"Класс: {grade[0]}, Количество студентов: {grade[1]}")

def get_teacher_subjects(teacher_name):
    cursor.execute('SELECT subject_name FROM subjects WHERE teacher_name = ?', (teacher_name,))
    subjects = cursor.fetchall()
    
    for subject in subjects:
        print(subject[0])


def close_connection():
    conn.close()


    while True:
        print("\nВыберите действие:")
        print("1. Добавить студента")
        print("2. Добавить предмет")
        print("3. Показать всех студентов")
        print("4. Показать все предметы")
        print("5. Показать студентов по классу")
        print("6. Обновить возраст студента")
        print("7. Удалить студента")
        print("8. Показать количество студентов по классу")
        print("9. Показать предметы по имени учителя")
        print("0. Выход")

        choice = input("Ваш выбор: ")

        if choice == '1':
            register_student()
        elif choice == '2':
            add_subject()
        elif choice == '3':
            get_students()
        elif choice == '4':
            get_subjects()
        elif choice == '5':
            grade = input("Введите класс: ")
            get_students_by_grade(grade)
        elif choice == '6':
            student_id = int(input("Введите ID студента: "))
            new_age = int(input("Введите новый возраст студента: "))
            update_student_age(student_id, new_age)
        elif choice == '7':
            student_id = int(input("Введите ID студента: "))
            delete_student(student_id)
        elif choice == '8':
            get_student_count_by_grade()
        elif choice == '9':
            teacher_name = input("Введите имя учителя: ")
            get_teacher_subjects(teacher_name)
        elif choice == '0':
            close_connection()
            break
        else:
            print("Неверный выбор, попробуйте снова.")
