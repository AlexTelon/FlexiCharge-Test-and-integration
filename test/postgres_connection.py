import psycopg2
import pytest

class psql_connection:
    

    def createCursor(connection):
        #creates a cursor used to execute SQL commands in the database
        try:
            cursor = connection.cursor()
        except: 
            pytest.fail('Cursor could not be created')
        else:
            print('Cursor was created!')
            return cursor
        finally:
            assert cursor != None
        

    def connect():
        print('Connecting to the PostgreSQL database...')
        connection = None

        # Connect to the database
        try:
            connection = psycopg2.connect(
                "dbname=example_database user=postgres password=abc123")    
        except:
            pytest.fail('Connection Failed') 
        else:
            print('Connection to Database Successful!')
            return connection
        finally:
            assert(connection != None)  
    


    def closeConnection(connection):
        # Close database connection
        try: 
            assert connection != None
            connection.close()
        except:
            pytest.fail('Connection could not be closed. Did connection succeed?')
            