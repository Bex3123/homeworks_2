import sqlite3
from sqlite3 import Error


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return conn


def create_countries_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS countries 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                      title TEXT NOT NULL)''')
    conn.commit()


def insert_countries(conn):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO countries (title) VALUES (?)", ('USA',))
    cursor.execute("INSERT INTO countries (title) VALUES (?)", ('Germany',))
    cursor.execute("INSERT INTO countries (title) VALUES (?)", ('China',))
    cursor.execute("INSERT INTO countries (title) VALUES (?)", ('Japan',))
    conn.commit()


def create_cities_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS cities 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                      title TEXT NOT NULL, 
                      area FLOAT DEFAULT 0, 
                      country_id INTEGER,
                      FOREIGN KEY (country_id) REFERENCES countries(id))''')
    conn.commit()


def insert_cities(conn):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO cities (title, area, country_id) VALUES (?, ?, ?)", ('San Francisco', 120, 1))
    cursor.execute("INSERT INTO cities (title, area, country_id) VALUES (?, ?, ?)", ('New York', 1223, 1))
    cursor.execute("INSERT INTO cities (title, area, country_id) VALUES (?, ?, ?)", ('Berlin', 891, 2))
    cursor.execute("INSERT INTO cities (title, area, country_id) VALUES (?, ?, ?)", ('Beijing', 16410, 3))
    cursor.execute("INSERT INTO cities (title, area, country_id) VALUES (?, ?, ?)", ('Tokyo', 1896, 4))
    cursor.execute("INSERT INTO cities (title, area, country_id) VALUES (?, ?, ?)", ('Hamburg', 891, 2))
    cursor.execute("INSERT INTO cities (title, area, country_id) VALUES (?, ?, ?)", ('Guangzhou', 16410, 3))
    conn.commit()


def create_students_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                      first_name TEXT NOT NULL, 
                      last_name TEXT NOT NULL, 
                      city_id INTEGER,
                      FOREIGN KEY (city_id) REFERENCES cities(id))''')
    conn.commit()


def insert_students(conn):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)", ('Brad', 'Pitt', 1))
    cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)", ('Erling', 'Holland', 2))
    cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)", ('Lionel', 'Messi', 3))
    cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)", ('Cristiano', 'Ronaldo', 4))
    cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)", ('Wesley', 'Glover', 1))
    cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)", ('Charles', 'West', 1))
    cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)", ('Lois', 'Carter', 4))
    cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)", ('Margaret', 'Perez', 2))
    cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)", ('Grace', 'Lane', 3))
    cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)", ('Timothy', 'Hill', 2))
    cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)", ('Thomas', 'Foster', 4))
    cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)", ('Martha', 'Smith', 3))
    cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)", ('Shirley', 'Howard', 4))
    cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)", ('Daniel', 'Johnson', 1))
    cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)", ('Shirley', 'Clark', 1))
    conn.commit()


def get_cities(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT title FROM cities")
    cities = cursor.fetchall()
    return cities


def get_students_by_city(conn, city_id):
    cursor = conn.cursor()
    cursor.execute("SELECT students.first_name, students.last_name, countries.title, cities.title, cities.area "
                   "FROM students "
                   "JOIN cities ON students.city_id = cities.id "
                   "JOIN countries ON cities.country_id = countries.id "
                   "WHERE cities.id = ?", (city_id,))
    students = cursor.fetchall()
    return students


def print_cities(cities):
    print("List of cities:")
    for city in cities:
        print(city[0])


def print_students(students):
    print("Information about students in the selected city:")
    for student in students:
        print("Name:", student[0])
        print("Last name:", student[1])
        print("Country:", student[2])
        print("City:", student[3])
        print("Area of the city:", student[4])
        print('------------------------------')


def main():
    conn = create_connection('students.db')
    if conn is not None:
        print('Successfully connected to DB!')

    create_countries_table(conn)
    insert_countries(conn)

    create_cities_table(conn)
    insert_cities(conn)

    create_students_table(conn)
    insert_students(conn)

    cities = get_cities(conn)

    print_cities(cities)

    while True:
        city_id = int(input("You can display a list of students "
                            "by the selected city id from the list of cities below, "
                            "to exit the program, enter 0: "))
        if city_id == 0:
            break
        students = get_students_by_city(conn, city_id)
        print_students(students)

    conn.close()

if __name__ == '__main__':
    main()





