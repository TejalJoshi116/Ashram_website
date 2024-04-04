from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ashram_db'

mysql = MySQL(app)

# Define routes for each HTML page
@app.route('/')
def index():
#     cur = mysql.connection.cursor()
    
#     cur.execute("SELECT * FROM user_info")
#     data = cur.fetchall()
#     cur.close()

#     return render_template('main.html', data=data)
     return render_template('main.html')

@app.route('/information')
def information():
    cur = mysql.connection.cursor()
    cur.execute("SELECT full_name, age, class FROM students_info")
    data = cur.fetchall()
    cur.close()
    student_list = [{'full_name': row[0], 'age': row[1], 'class': row[2]} for row in data]
    return render_template('information.html', data=student_list)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/donate', methods=['GET', 'POST'])
def donate():
    if request.method == 'POST':
        # Fetch form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone = request.form['phone']
        email = request.form['email']
        address = request.form['address']
        occupation = request.form['occupation']
        donation_amount = request.form['donation_amount']
        items_donated = request.form['items_donated']
        donation_time = request.form['donation_time']
        image_path = request.form['image']  # This will need additional handling for file upload

        # Store data in the database
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO donation_info (first_name, last_name, phone, email, address, occupation, donation_amount, items_donated, donation_time, image_path) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (first_name, last_name, phone, email, address, occupation, donation_amount, items_donated, donation_time, image_path)
        )
        mysql.connection.commit()
        cur.close()

        # Redirect to a thank you page or home page
        return redirect(url_for('index'))
    return render_template('donate.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


@app.route('/new_student', methods=['GET', 'POST'])
def new_student():
    if request.method == 'POST':
        full_name = request.form['full_name']
        age = request.form['age']
        dob = request.form['dob']
        known_family = request.form['known_family']
        date_of_admission = request.form['date_of_admission']
        gender = request.form['gender']
        guardian_name = request.form['guardian_name']
        contact_number = request.form['contact_number']
        address = request.form['address']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students_info (full_name, age, dob, known_family, date_of_admission, gender, guardian_name, contact_number, address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (full_name, age, dob, known_family, date_of_admission, gender, guardian_name, contact_number, address))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))
    return render_template('new_student.html')

@app.route('/visit')
def visit():
    return render_template('visit.html')



if __name__ == '__main__':
    app.run(debug=True)
