import sqlite3


def connect():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    connection.commit()
    connection.close()


def insert(title, author, year, isbn):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    connection.commit()
    connection.close()


def view():
    print("inside backend.view...")
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM book")
    rows = cursor.fetchall()
    connection.close()
    return rows


def search(title="", author="", year="", isbn=""):
    print("inside backend.search with author: ", author)
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = cursor.fetchall()
    connection.close()
    return rows


def delete(id):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute(
        "DELETE FROM book WHERE id=?", (id,))
    connection.commit()
    connection.close()


def update(id, title, author, year, isbn):
    print("inside backend.update...")
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE book SET title=?, author=?, year=?, isbn=? where id=?", (title, author, year, isbn, id))
    connection.commit()
    connection.close()


connect()
# view()
# search()
# insert("The sea1", "John", 1997, 123545515)
# insert("The sea2", "John", 1998, 123545516)
# insert("The sea3", "John", 1999, 123545517)
# print(view())
# print("searching for John")
# print(search(author="John"))
# delete(1)
# delete(3)
# delete(4)
# delete(5)
# delete(6)
# delete(7)
# update(id=1, title="The sea3", author="John", year="1999", isbn="123545515")
# print(view())