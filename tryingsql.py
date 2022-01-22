import mysql.connector as mysql

# variables 
host = "localhost" 
user = "root"
password = ""

# connect to mysql
try:
    db = mysql.connect(host=host,user=user,password=password)
    print("Connected.")
except Exception as e:
    print(e)
    print("Failed to connect.")

# creating a database
try:
    # Set command handler
    ch = db.cursor()
    ch.execute("CREATE DATABASE fruits")
    print("Database has been created.")
except Exception as e:
    print("Could not create database.")

# view all databases
try:
    ch.execute("SHOW DATABASES")
    print("Current databases:")
    for database in ch:
        print(database)
except Exception as e:
    print(e)
    print("Could not show all databases.")

# connect to existing database
db_to_connect = 'fruits'
try:
    db1 = mysql.connect(host=host,user=user,password=password,database=db_to_connect)
    print("Connected to fruits database.")
except Exception as e:
    print(e)
    print("Could not connect to the %s database." % db_to_connect)

# creating tables in a database
try:
    ch = db1.cursor()
    ch.execute("CREATE TABLE YellowFruit (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), avr_weight FLOAT)")
    print("Table created.")
except Exception as e:
    print("Table creation failed.")
    print(e)