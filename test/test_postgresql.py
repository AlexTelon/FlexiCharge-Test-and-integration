import datetime
import pytest
import psycopg2
from postgres_connection import psql_connection


def test_create_database():
    connection = psql_connection.connect("postgres")
    cursor = psql_connection.createCursor(connection)

    # Attempt to create a table
    createDataBase(cursor, connection)

    psql_connection.closeConnection(connection)


def test_create_Table():
    # Establsih connection and create a cursor to execute commands in the database
    connection = psql_connection.connect("testing_database7")
    cursor = psql_connection.createCursor(connection)

    # Attempt to create a table
    createTables(cursor, connection)

    psql_connection.closeConnection(connection)


def test_insert_to_table():
    # Establsih connection and create a cursor to execute commands in the database
    connection = psql_connection.connect("testing_database7")
    cursor = psql_connection.createCursor(connection)
    insertQuery = "INSERT INTO chargertable5 (chargername,created_on) VALUES ('chargerTestName',{timestamp}) RETURNING chargepointid".format(
        timestamp=datetime.datetime.now(datetime.timezone.utcoffset(hour=1)))
    dataToInsert = ("chargerTestName2")
    cursor.execute(insertQuery)
    psql_connection.closeConnection(connection)


def createDataBase(cursor, connection):
    print('Attempt to create Database \n')
    try:
        # Create a table structure
        cursor.execute('CREATE DATABASE testing_database7')
    except:
        pytest.fail(
            'An error exception was raised! Is the Database already created?')
    else:
        # if successful created, commit the table to the database
        print('Database was successfully created!')
        connection.commit()


def createTables(cursor, connection):

    print('Attempt to create Tables \n')
    try:
        # Create a table structure
        cursor.execute('''CREATE TABLE chargerTable5 (
            chargePointID SERIAL PRIMARY KEY,
            chargerName VARCHAR(20) UNIQUE NOT NULL,
            created_on TIMESTAMP NOT NULL,
            last_login TIMESTAMP
            );''')
    except:
        pytest.fail(
            'An error exception was raised! Is the table already created?')
    else:
        # if successful created, commit the table to the database
        print('Table was successfully created!')
        connection.commit()
