from flask import Flask
import mysql.connector

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'DESKTOP-D1EGVS0'
app.config['MYSQL_USER'] = 'root@localhost'
app.config['MYSQL_DB'] = 'your_mysql_database'


mysql = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)

cursor = mysql.cursor()
cursor.execute("SELECT * FROM your_table")
data = cursor.fetchall()


cursor.close()
mysql.close()

