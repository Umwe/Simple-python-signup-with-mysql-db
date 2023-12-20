import mysql.connector

# Replace these values with your MySQL server information
host = "localhost"
user = "******"
password = "********"

# Connect to MySQL server
conn = mysql.connector.connect(host=host, user=user, password=password)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create a new database
database_name = "pythonlogin"
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
print(f"Database '{database_name}' created successfully")

# Switch to the new database
cursor.execute(f"USE {database_name}")

# Create a table named 'user' with columns: ID (auto increment), name, username, and password
table_creation_query = """
CREATE TABLE IF NOT EXISTS user (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    username VARCHAR(255),
    password VARCHAR(255)
)
"""

cursor.execute(table_creation_query)
print("Table 'user' created successfully")

# Close the cursor and connection
cursor.close()
conn.close()
