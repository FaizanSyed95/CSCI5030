# This file will hold useful functions
from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL
from datetime import datetime
import logic
import itertools

app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'Osamas-MacBook-Pro.local'
# app.config['MYSQL_USER'] = 'Osama'
# app.config['MYSQL_PASSWORD'] = 'CSCI5030SLU2021'
# app.config['MYSQL_DATABASE_DB'] = 'wordsense'

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'CSCI5030@SLU2021'
app.config['MYSQL_DATABASE_DB'] = 'wordsense'

mysql = MySQL(app)
conn = mysql.connect()
cursor = conn.cursor()

def tuple2list(ExTuple):
    ExList = list(itertools.chain(*ExTuple))
    return ExList 

def SQLQuery(statment):
    cursor.execute(statment)
    conn.commit()
    data = logic.tuple2list(cursor.fetchall()) 
    return data

def SQLInsertQuery(statment):
    cursor.execute(statment)
    conn.commit()