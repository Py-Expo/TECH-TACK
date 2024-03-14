from flask import Flask, render_template, request, session, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__, static_url_path='/static')

# MySQL configuration
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_DB'] = "deal"  # Changed the database name to "deal"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "password"
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

# Secret key for session management
app.secret_key = "myapp"

# Initialize MySQL
mysql = MySQL(app)

# Route for the index page
@app.route('/')
def index():
    return render_template("index.html")

# Route for the home page
@app.route('/home.html')
def home():
    return render_template('home.html')

# Route for the user profile page
@app.route('/myprofile.html')
def myprofile():
    return render_template('myprofile.html')

# Route for the wishlist page
@app.route('/wishlist.html')
def wishlist():
    return render_template('wishlist.html')

# Route for the category page
@app.route('/category.html')
def category():
    return render_template('category.html')

# Route for the notification page
@app.route('/notification.html')
def notification():
    return render_template('notification.html')

# Route for the shopkeeper page
@app.route('/shopkeeper.html')
def shopkeeper():
    return render_template('shopkeeper.html')

# Route for handling login requests
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Establish a database connection
        cur = mysql.connection.cursor()

        # Execute SQL query to check if the username and password match
        cur.execute("SELECT * FROM login WHERE username = %s AND password = %s", (username, password))
        user = cur.fetchone()

        # Close the database cursor
        cur.close()

        if user:
            # Store the username in the session to keep the user logged in
            session['username'] = user['username']

            # Redirect to the home page after successful login
            return redirect(url_for('home'))
        else:
            # If login fails, redirect back to the login page with an error message
            return render_template('index.html', error="Invalid username or password")

# Route for handling logout requests
@app.route('/logout')
def logout():
    # Clear session data to log the user out
    session.clear()
    
    # Redirect to the index page after logout
    return redirect(url_for('index'))

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
