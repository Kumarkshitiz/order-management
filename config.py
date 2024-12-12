from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# Database configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '#raik1005@'
app.config['MYSQL_DB'] = 'hotwax'

mysql = MySQL(app)
