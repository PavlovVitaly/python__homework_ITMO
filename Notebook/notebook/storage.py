import sqlite3

SQL_SELECT_ALL = """
    SELECT
        id, name_of_note, text_of_note, status, start_date, end_date
    FROM
      notebook
"""

SQL_INSERT_NOTE = """
    INSERT INTO notebook (name_of_note, text_of_note, status, start_date, end_date) VALUES (?, ?, ?, ?, ?)
"""


def dict_factory(cursor, row):
    d = {}

    print("==>> Raw", row)
    print('==>>', cursor.description)

    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]

    return d


def connect(db_name=None):
    if db_name is None:
        db_name = ':memory:'
    conn = sqlite3.connect(db_name)
    conn.row_factory = dict_factory
    return conn


def initialize(conn, creation_schema):
    with conn, open(creation_schema) as f:
        conn.executescript(f.read())
