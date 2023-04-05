create_book_table = "CREATE TABLE book (
    id INTEGER PRIMARY KEY,
    isbn TEXT NOT NULL,
    book_name TEXT NOT NULL,
    genre TEXT NOT NULL,
    author TEXT NOT NULL,
    book_year INTEGER NOT NULL,
    book_count INTEGER NOT NULL,
    book_page INTEGER NOT NULL,
    rank REAL NOT NULL
);"

create_operation_table = "CREATE TABLE operation (
    id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL,
    staff_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL,
    iss_date TEXT NOT NULL,
    return_date TEXT NOT NULL,
    return_indicator NUMERIC NOT NULL,
    FOREIGN KEY(student_id) REFERENCES student(id),
    FOREIGN KEY(staff_id) REFERENCES staff(id),
    FOREIGN KEY(book_id) REFERENCES book(id)
);"

create_student_table = "CREATE TABLE student (
    id INTEGER PRIMARY KEY,
    full_name TEXT NOT NULL,
    gender TEXT NOT NULL,
    date_of_birth TEXT NOT NULL
);"

create_staff_table = "CREATE TABLE staff (
    id INTEGER PRIMARY KEY,
    full_name TEXT NOT NULL,
    gender TEXT NOT NULL,
    date_of_birth TEXT NOT NULL
);"


insert_book_table = "INSERT INTO book 
VALUES 
    (1, '0393347095', 'The Metamorphosis', 'Novella', 'Franz Kafka', 2014, 2, 128, 4.4),
    (2, '0439358078', 'Harry Potter And The Order Of The Phoenix', 'Fantasy', 'J.K. Rowling', 2004, 3, 896, 4.2),
    (3, '0198800533', 'Anna Karenina', 'Realist Novel', 'Leo Tolstoy', 2017, 1, 896, 4.6);"

insert_staff_table = "INSERT INTO staff 
VALUES
    (1, 'Steve Smith', 'Male', date('1992-04-23')),
    (2, 'Ashley Miller', 'Female', date('1995-01-16'));"

insert_student_table = "INSERT INTO student 
VALUES
    (1, 'Mia Yang', 'Female', date('1996-09-15')),
    (2, 'Bob Lee', 'Male', date('1997-12-13')),
    (3, 'Eric Rampy', 'Male', date('1995-08-21')),
    (4, 'Stefany Ferenz', 'Female', date('1996-04-01'));"

insert_operation_table = "INSERT INTO operation 
VALUES
    (1, 3, 1, 1, date('now', '-4 days'), date('now', '10 days'), 0),
    (2, 1, 1, 3, date('now', '-1 days'), date('now', '13 days'), 0),
    (3, 2, 2, 2, date('now', '-1 days'), date('now', '6 days'), 0),
    (4, 4, 2, 2, date('now'), date('now', '14 days'), 0);"

update_staff_inf = "UPDATE staff
    SET full_name = 'Ashley Bailey'
    WHERE full_name = 'Ashley Miller';"

update_operation_inf = "UPDATE operation 
    SET 
        return_date = DATE(return_date, '-10 days'),
        return_indicator = 1
    WHERE 
        student_id = (
            SELECT id 
            FROM student 
            WHERE full_name = 'Eric Rampy');"

update_book_inf = "UPDATE book 
    SET book_count = book_count + 1
    WHERE book_name	 = 'The Metamorphosis';"

student_inf = "SELECT full_name 
FROM student
JOIN operation ON student.id = operation.student_id
WHERE operation.book_id = 2
ORDER BY full_name;"
