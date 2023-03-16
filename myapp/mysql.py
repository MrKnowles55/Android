import sqlite3


def connect(name="myapp.db"):
    return sqlite3.connect(name)


def create_database(name="myapp.db"):
    conn = connect(name)
    conn.close()
    return name


def add_entry(conn, date, time, category, note, amount):
    if not check_for_duplicate_entry(conn, date, time, category, note, amount):
        conn.execute("INSERT INTO entries (date, time, category, note, amount) VALUES (?, ?, ?, ?, ?)",
                     (date, time, category, note, amount))


def create_table(conn):
    conn.execute('''CREATE TABLE IF NOT EXISTS entries
                     (id INTEGER PRIMARY KEY, date DATE, time TIME, category VARCHAR(25), note VARCHAR(25), amount FLOAT)''')


def print_table(conn):
    result = conn.execute("SELECT * FROM entries")
    for row in result:
        print(row)


def check_for_duplicate_entry(conn, date, time, category, note, amount):

    result = conn.execute("SELECT * FROM entries WHERE date = ? AND time = ? AND category = ? AND note = ? AND amount = ?", (date, time, category, note, amount))
    for row in result:
        return True


if __name__ == "__main__":
    conn = connect()

    create_table(conn)

    add_entry(conn, '2023-03-15', '14:56:00', 'Category', 'Type', 3.00)
    add_entry(conn, '2023-03-16', '15:56:00', 'Category', 'Type', 3.50)
    add_entry(conn, '2023-03-17', '16:56:00', 'Category', 'Type', 3.75)

    conn.commit()

    print_table(conn)

    conn.close()



# # create a connection to a new database file
# conn = sqlite3.connect('myapp.db')
#
# # create a new table
# conn.execute('''CREATE TABLE IF NOT EXISTS entries
#                  (id INTEGER PRIMARY KEY, date DATE, time TIME, category VARCHAR(25), note VARCHAR(25), amount FLOAT)''')
#
# # insert some data into the table
# conn.execute("INSERT INTO entries (date, time, category, type, amount) VALUES (?, ?, ?, ?, ?)", ('2023-03-15', '14:56:00', 'Category', 'Type', 3.14))
# conn.execute("INSERT INTO entries (date, time, category, type, amount) VALUES (?, ?, ?, ?, ?)", ('2023-03-16', '12:56:00', 'Category', 'Type', 2.0))
# conn.execute("INSERT INTO entries (date, time, category, type, amount) VALUES (?, ?, ?, ?, ?)", ('2023-03-17', '10:56:00', 'Category2', 'Type2', 1.0))
#
# # commit the changes
# conn.commit()
#
# # query the table
# result = conn.execute("SELECT * FROM entries")
# for row in result:
#     print(row)
#
# # close the connection
# conn.close()

