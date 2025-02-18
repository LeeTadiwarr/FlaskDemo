from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def init_db():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            email TEXT UNIQUE,
                            password TEXT)''')
        conn.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE email = ? AND password = ?' , (email, password))
            user = cursor.fetchone()
            if user:
                session['user'] = {'name': user[1], 'email': user[2]}
                return redirect(url_for('dashboard'))
        return 'Invalid credentials'
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)', (name, email, password))
                conn.commit()
                return redirect(url_for('login'))
            except sqlite3.IntegrityError:
                return 'User already exists'
    return render_template('registration.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', user=session['user'])

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)