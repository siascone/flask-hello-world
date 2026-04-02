from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Spencer in 3308'

@app.route('/db_test')
def testing():
    # save db connection to variable
    conn = psycopg2.connect("postgresql://flask_hello_world_3308_db_zhm2_user:WGcP8mSCQvIZcVm71PiG7FbodJS6iuvp@dpg-d76ret15pdvs7384es0g-a/flask_hello_world_3308_db_zhm2")
    
    conn.close() #remember to always close the db connection
    return "Database Connection Successful"

@app.route('/db_create')
def db_create():
    # establish db connection
    conn = psycopg2.connect("postgresql://flask_hello_world_3308_db_zhm2_user:WGcP8mSCQvIZcVm71PiG7FbodJS6iuvp@dpg-d76ret15pdvs7384es0g-a/flask_hello_world_3308_db_zhm2")
    
    # open cursor to connection
    cur = conn.cursor()
    
    # create Basketball table with psycopg2 SQL query string
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
            );            
    ''')
    
    # commit the changes made by the query above to the db (i.e. save to the db)
    conn.commit()
    
    # close db connection
    conn.close()
    
    return "Basketball Table Successfully Created"