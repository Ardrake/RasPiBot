import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def init_data(conn):
    sql_create_robots_table = """ CREATE TABLE IF NOT EXISTS robots (
                                            id integer PRIMARY KEY,
                                            name text NOT NULL
                                        ); """

    sql_create_servos_table = """CREATE TABLE IF NOT EXISTS servos (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    value integer,
                                    robot_id integer not null, 
                                    FOREIGN KEY (robot_id) REFERENCES robots (id)
                                );"""
    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_robots_table)
        create_table(conn, sql_create_servos_table)