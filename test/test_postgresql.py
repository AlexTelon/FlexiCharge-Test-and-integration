import datetime
import pytest
import psycopg2
from postgres_connection import psql_connection


def test_create_database():
    connection = psql_connection.connect("example_database")
    cursor = psql_connection.createCursor(connection)

    # Attempt to create a table
    createDataBase(cursor, connection)

    psql_connection.closeConnection(connection)


def test_create_Table():
    # Establsih connection and create a cursor to execute commands in the database
    connection = psql_connection.connect("example_database")
    cursor = psql_connection.createCursor(connection)

    # Attempt to create a table
    createTables(cursor, connection)

    psql_connection.closeConnection(connection)


def test_insert_to_table():
    # Establsih connection and create a cursor to execute commands in the database
    connection = psql_connection.connect("example_database")
    cursor = psql_connection.createCursor(connection)
    insertQuery = '''INSERT INTO 
        public."ChargePoints"(name, location, price, klarnaReservationAmount) 
        VALUES("Nässjö Centralstation",{57.652328901782795,14.694810832097543},123.00,500);
    '''
    cursor.execute(insertQuery)
    psql_connection.closeConnection(connection)


def createDataBase(cursor, connection):
    print('Attempt to create Database \n')
    try:
        # Create a table structure
        cursor.execute('CREATE DATABASE example_database')
    except:
        pytest.fail(
            'An error exception was raised! Is the Database already created?')
    else:
        # if successful created, commit the table to the database
        print('Database was successfully created!')
        connection.commit()


def createTables(cursor, connection):
    chargePoints_Table = '''CREATE TABLE IF NOT EXISTS public."ChargePoints" (
        ChargePointID SERIAL PRIMARY KEY NOT NULL,
        name VARCHAR(255) NOT NULL,
        location DOUBLE PRECISION NOT NULL,
        price NUMERIC(10,2) NOT NULL,
        klarnaReservationAmount INTEGER NOT NULL
    );'''
    cursor.execute(chargePoints_Table)
    print('Attempt to create Tables \n')
    try:
        # Create a table structure
        print('hi')
    except:
        pytest.fail(
            'An error exception was raised! Is the table already created?')
    else:
        # if table was successfully created, commit the table to the database
        print('Table was successfully created!')
        connection.commit()
