import psycopg2


def connect():
    print('Connecting to the PostgreSQL database...')

# Connect to database
    connection = psycopg2.connect(
        "dbname=example_database user=postgres password=abc123")
    cursor = connection.cursor()

# Print Database version
    print('PostgreSQL database version:')
    cursor.execute('SELECT version()')
    db_version = cursor.fetchone()
    print(db_version)

# Create tables
    print('Attempt to create Tables \n')
    try:
        cursor.execute('''CREATE TABLE chargerTable (
            chargePointID SERIAL PRIMARY KEY,
            chargerName VARCHAR(20) UNIQUE NOT NULL,
            created_on TIMESTAMP NOT NULL,
            last_login TIMESTAMP
            )''')
    except:
        print('An error exception was raised!')
    else:
        print('The table was created successfully!')

    return connection


def closeConnection(connection):
    # Close database connection
    connection.close()


def createTables(crsr):
    print('Attempt to create Tables \n')
    try:
        crsr.execute('''CREATE TABLE [IF NOT EXISTS] chargerTable (
            chargePointID SERIAL(10) PRIMARY KEY, 
            chargerName VARCHAR(20) UNIQUE NOT NULL,
            created_on TIMESTAMP NOT NULL,
            last_login TIMESTAMP 
            NOT NULL);''')
    except:
        print('An error exception was raised!')
    else:
        print('The table was created successfully!')


conn = connect()
closeConnection(conn)
