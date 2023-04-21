from flask import Flask, render_template, request
import hashlib
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    # get the username and password from the form
    username = request.form.get('username')
    password = request.form.get('password')
    
    # hash the password using SHA-256
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    
    # save the username and hashed password in the database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
    conn.commit()
    conn.close()
    
    # redirect to the login page
    return redirect('/login.html')

if __name__ == '__main__':
    app.run()

