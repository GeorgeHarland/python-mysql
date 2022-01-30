import mysql.connector as mysql

# Apache error: 

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
    # set command handler
    ch = db.cursor()
    ch.execute("CREATE DATABASE users")
    print("Database has been created.")
except Exception as e:
    print(e)
    print("Could not create database.")

# View all databases
try:
    ch.execute("SHOW DATABASES")
    print("Current databases:")
    for db in ch:
        print(db)
except Exception as e:
    print(e)
    print("Could not show all databases")

# connect to existing database
db_to_connect = "users"
try:
    db1 = mysql.connect(host=host,user=user,password=password, database=db_to_connect)
    print("Connected to users database")
except Exception as e:
    print(e)
    print(f"Could not connect to the {db_to_connect} database.")

# Creating tables in a database
try:
    ch = db1.cursor()
    ch.execute("CREATE TABLE employees (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), salary INT")
    print("Table created")
except Exception as e:
    print(e)
    print("Table creation failed")

# show tables in db selected
ch.execute("SHOW TABLES")
print("Tables in current db:")
for table in ch:
    print(table)

# insert one row into table
new_query = "INSERT INTO employees(name,salary) VALUES(%s,%s)"
new_query_vals = ("Thomas","40000")
ch.execute(new_query,new_query_vals)
db1.commit() # save the changes
print(ch.rowcount, "record(s) inserted into the table.") # returns number of rows inserted in last query

# Inserting multiple rows
new_query = "INSERT INTO employees(name,salary) VALUES(%s,%s)"
new_query_vals = [("Jim","35000"),
("Mary","50000"),
("Jane","18000")]
ch.executemany(new_query,new_query_vals)
db1.commit()
print(ch.rowcount, " record(s) inserted into the table.")

# Show all records from selected tables
ch.execute("SELECT * from employees")
records = ch.fetchall()
print("All employee records:")
for record in records:
    print(record)

# Display specific columns
ch.execute("SELECT name from employees")
records = ch.fetchall()
print("Employee names:")
for record in records:
    print(record)

# ------------------------------------------

# 