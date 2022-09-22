import datetime
import pytest
import psycopg2
from postgres_connection import psql_connection


def test_create_database():
    connection = psql_connection.connect("postgres")
    connection.autocommit = True
    cursor = psql_connection.createCursor(connection)

    # Attempt to create a table
    createDataBase(cursor, connection)
    psql_connection.closeConnection(connection)


def test_create_Table():
    # Establsih connection and create a cursor to execute commands in the database
    connection = psql_connection.connect("example_database")
    cursor = psql_connection.createCursor(connection)

    # Attempt to create a table
    createTable(cursor, connection)

    psql_connection.closeConnection(connection)


def test_insert_to_table():
    # Establsih connection and create a cursor to execute commands in the database
    connection = psql_connection.connect("example_database")
    cursor = psql_connection.createCursor(connection)
    chargePointIDs=20,24,25,27
    locationNames = 'Nässjö Centralstation', 'Coop, Forserum', 'Airport Parking, Jönköping', 'Testotesto'
    locationCoordinates = {57.652328901782795,14.694810832097543}, {57.70022044183724,14.475150415104222}, {57.749812214261034,14.070100435207065}, {52.77771,14.16301}
    prices = 123.00, 7500.00, 100000.00, 3000.00
    klarnaReservationAmounts = 500, 500, 5000,  2000
    chargePointsTable = 'public."ChargePoints"(name, location[0], location[1], price, klarnaReservationAmount)'
    sqlQuery = '''INSERT INTO public."ChargePoints"("chargePointID",name, location[0], location[1], price, "klarnaReservationAmount") 
    VALUES (20,'Nässjö Centralstation', 57.652328901782795, 14.694810832097543, 123.00, 500)'''
    cursor.execute(sqlQuery)
    connection.commit()
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


def createTable(cursor, connection):
    chargePoints_Table = '''CREATE TABLE IF NOT EXISTS public."ChargePoints" (
        "chargePointID" SERIAL PRIMARY KEY NOT NULL,
        name VARCHAR(255) NOT NULL,
        location DOUBLE PRECISION[] NOT NULL,
        price NUMERIC(10,2) NOT NULL,
        "klarnaReservationAmount" INTEGER NOT NULL
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
