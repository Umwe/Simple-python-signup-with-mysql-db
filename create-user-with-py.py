import mysql.connector
import bcrypt

def create_user(conn, name, username, password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    cursor = conn.cursor()

    
    insert_query = """
    INSERT INTO user (name, username, password) VALUES (%s, %s, %s)
    """
    user_data = (name, username, hashed_password)
    cursor.execute(insert_query, user_data)

    
    conn.commit()


    cursor.close()

def main():
    
    host = "localhost"
    user = "******"
    password = "*****"
    database_name = "pythonlogin"

    # Connect to MySQL server
    conn = mysql.connector.connect(host=host, user=user, password=password, database=database_name)

    # Get user input
    name = input("Enter your name: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Create the user in the database
    create_user(conn, name, username, password)
    print("User created successfully")

    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()
