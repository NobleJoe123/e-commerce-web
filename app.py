from flask import Flask, render_template, redirect, url_for, request,Response, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired




app = Flask(__name__)

app.secret_key = 'key'


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'commerce'


mysql = MySQL(app)



@app.route('/')
def index():   
    return render_template('index.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return redirect(url_for('home'))
    return render_template('index.html')




@app.route('/shop', methods=['GET', 'POST'])
def shop():
    if request.method == 'POST':
        return redirect(url_for('shop'))
    return render_template('shop.html')

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        return redirect(url_for('checkout'))
    return render_template('chackout.html')

@app.route('/shopdetail', methods=['GET', 'POST'])
def shopdetail():
    if request.method == 'POST':
        return redirect(url_for('shopdetail'))
    return render_template('shop-detail.html')

@app.route('/testimonial', methods=['GET', 'POST'])
def testimonial():
    if request.method == 'POST':
        return redirect(url_for('testimonial'))
    return render_template('testimonial.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return redirect(url_for('contact'))
    return render_template('contact.html')

@app.route('/cart', methods=['GET', 'POST'])
def cart():
    if request.method == 'POST':
        return redirect(url_for('cart'))
    return render_template('cart.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/login/index')
def loggegin():
    if 'loggedin' in session:
        return render_template('index.html', username=session['username'])
    return redirect(url_for('/log'))


     

@app.route('/reg', methods=['GET', 'POST'])
def reg():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO web VALUES (NULL, %s, %s, %s)', (username, password, email,))
        mysql.connection.commit()
        msg = 'You have successfully registered!'
        return render_template('login.html', msg=msg)
    elif request.method == 'POST':
        msg = 'Please fill out the form!'
    return render_template('register.html', msg=msg)
    
@app.route('/log', methods=['GET', 'POST'])
def log():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM web WHERE username = % s AND password = % s', (username, password, ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['Id'] = account['id']
            session['Username'] = account['username']
            msg = 'Logged in successfully !'
            return render_template('index.html', msg = 'username')
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)


class NameForm(FlaskForm):
     name = StringField('What is your name?', validators=[DataRequired()])
     submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
         name = form.name.data
         form.name.data = ''
    return render_template('index.html', form=form, name=name)




if __name__ == '__main__':
    app.run(debug=True)