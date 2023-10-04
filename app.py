from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'gadgetkart'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
    user = cur.fetchone()
    cur.close()

    if user:
        # Successful login
        return redirect(url_for('dashboard'))
    else:
        # Failed login
        return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    return 'Welcome to the dashboard!'

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contacts (fullname, email, phone, message) VALUES (%s, %s, %s, %s)", (fullname, email, phone, message))
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('index'))
        
if __name__ == '__main__':
    app.run(debug=True)
