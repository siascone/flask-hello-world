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
def creating():
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

@app.route('/db_insert')
def inserting():
    # establish db connection
    conn = psycopg2.connect("postgresql://flask_hello_world_3308_db_zhm2_user:WGcP8mSCQvIZcVm71PiG7FbodJS6iuvp@dpg-d76ret15pdvs7384es0g-a/flask_hello_world_3308_db_zhm2")
    
    # open cursor to connection
    cur = conn.cursor()
    
    # run sql query to populate basketball table with 4 players
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2); 
    ''')
    
    # save insert to db
    conn.commit()
    
    # close db connectino
    conn.close()
    
    return "Basketball Table Successfully Populated"

@app.route('/db_select')
def selecting():
    # establish db connection
    conn = psycopg2.connect("postgresql://flask_hello_world_3308_db_zhm2_user:WGcP8mSCQvIZcVm71PiG7FbodJS6iuvp@dpg-d76ret15pdvs7384es0g-a/flask_hello_world_3308_db_zhm2")
    
    # open cursor to connection
    cur = conn.cursor()    
    
    # select all players from basketball table
    cur.execute('''
        SELECT * FROM Basketball;
    ''')
    
    # fetch results of query
    players = cur.fetchall()
    
    # print out records in table format using HTML tags
    response_string = ""
    response_string += "<table>" # open table tag
    # add table row headers
    response_string += "<tr><td><strong>First</strong></td><td><strong>Last</strong></td><td><strong>City</strong></td><td><strong>Name</strong></td><td><strong>Number</strong></td></tr>"
    for player in players:
        response_string += "<tr>" # open table row tag for each player
        for info in player:
            response_string += f"<td>{info}</td>" # open table data cell tag 
                                                  # for each piece of info for a 
                                                  # player
        response_string += "</tr>" # close table row tag
    response_string += "</table>" # close table tag
    
    return response_string # recall from html lecture, all html on a page is 
                           # just a string
                           
@app.route('/db_drop')
def dropping():
    # establish db connection
    conn = psycopg2.connect("postgresql://flask_hello_world_3308_db_zhm2_user:WGcP8mSCQvIZcVm71PiG7FbodJS6iuvp@dpg-d76ret15pdvs7384es0g-a/flask_hello_world_3308_db_zhm2")
    
    # open cursor to connection
    cur = conn.cursor()   
    
    # execute drop table sql command
    cur.execute('''
        DROP TABLE Basketball;            
    ''')
    
    # commit drop to db
    conn.commit()
    
    # close connection
    conn.close()
    
    return "Basketball Table Successfully Dropped"