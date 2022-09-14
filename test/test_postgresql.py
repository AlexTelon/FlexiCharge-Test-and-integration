import psycopg2

def test_createDB_Table():
    connection = connect()
    cursor = createCursor(connection)
    #check if table creation threw an exception
    if(createTables(cursor)):
        #if successful commit the created table to the database
        connection.commit()
        print('Table was successfully created!')
    else:
        print('An error exception was raised!')

    closeConnection(connection)

def createCursor(connection):
    #creates a cursor used to execute SQL commands in the database
    return connection.cursor()

def connect():
    print('Connecting to the PostgreSQL database...')
    connection = None

    # Connect to the database
    try:
        connection = psycopg2.connect(
            "dbname=example_database user=postgres password=abc123")
    except:
        print('Connection Failed')
    else:
        print('Connection to Database Successful!')
    finally:
        return connection


def closeConnection(connection):
    # Close database connection
    connection.close()


def createTables(cursor):
    # Create a table structure
    print('Attempt to create Tables \n')
    try:
        cursor.execute('''CREATE TABLE chargerTable5 (
            chargePointID SERIAL PRIMARY KEY,
            chargerName VARCHAR(20) UNIQUE NOT NULL,
            created_on TIMESTAMP NOT NULL,
            last_login TIMESTAMP
            );''')
    except:
        return False
    else:
        return True

test_createDB_Table()
