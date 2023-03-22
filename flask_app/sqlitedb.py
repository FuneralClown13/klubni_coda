import sqlite3

db = 'books.db'
table = 'books_shop'


def connector(f):
    def wrapper(*args, **kwargs):
        try:
            sqlite_connection = sqlite3.connect(f'{db}')
            cursor = sqlite_connection.cursor()
            return f(cursor, sqlite_connection, *args, **kwargs)
        except sqlite3.Error as error:
            print(error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                print('\n\nConnection close')

    return wrapper


@connector
def create_table(cursor, connection):
    """id
Book
Author
Price
Count"""
    pattern = f"""CREATE TABLE IF NOT EXISTS {table}(
                            id INTEGER PRIMARY KEY,
                            book TEXT NOT NULL,
                            author TEXT NOT NULL,
                            count INTEGER,
                            price INTEGER,
                            annotation text);
                            """

    cursor.execute(pattern)
    connection.commit()


@connector
def create(cursor, connection, book, author, count, price, annotation=''):
    pattern = f'''
                INSERT INTO {table}
                (book, author, count, price, annotation)
                VALUES
                ('{book}', '{author}', {int(count)}, {int(price)}, '{annotation}')
                '''
    cursor.execute(pattern)
    connection.commit()


@connector
def read(cursor, connection, id=0):
    if not id:
        pattern = f'''
                SELECT *
                FROM {table}
                '''
    else:
        pattern = f'''
                SELECT *
                FROM {table}
                WHERE id = {id}
                '''
    cursor.execute(pattern)
    return cursor.fetchall()


@connector
def update(cursor, connection, id, book, author, count, price, annotation=''):
    pattern = f'''
                UPDATE {table}
                SET book = '{book}',
                author = '{author}', 
                count = {int(count)},
                price = {int(price)},
                annotation = '{annotation}'
                WHERE id = {id}
                '''
    cursor.execute(pattern)
    connection.commit()


@connector
def delete(cursor, connection, id):
    pattern = f'''
                    DELETE
                    FROM {table}
                    WHERE id = {id}
                    '''
    cursor.execute(pattern)
    connection.commit()
