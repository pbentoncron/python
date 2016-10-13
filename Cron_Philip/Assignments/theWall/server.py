from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'WeAreTheChampions!'
bcrypt = Bcrypt(app)

mysql = MySQLConnector(app,'theWall') 

@app.route('/')
def index():
  return render_template("homepage.html")

def validReg():
    if (len(request.form['email']) < 1 or 
        len(request.form['first_name']) < 1 or 
        len(request.form['last_name']) < 1 or  
        len(request.form['password']) < 1 or 
        len(request.form['confirm_password']) < 1):
        flash('All inputs required', 'regError')
        return False;
    elif (len(request.form['first_name']) < 2 or
             len(request.form['last_name']) < 2):
        flash('Name input fields require at least 2 characters', 'regError')
        return False
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Valid Email Format Required', 'regError')
        return False
    elif len(request.form['password']) < 8 or len(request.form['confirm_password']) < 8:
        flash('Passwords must be at least 8 charaters', 'regError')
        return False
    elif not request.form['password'] == request.form['confirm_password']:
        flash('Password and Confirm password fields must match', 'regError')
        return False

    return True

def validLog():

    if (len(request.form['email']) < 1 or len(request.form['password']) < 1):
        flash('All inputs required', 'logError')    
        return False
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Valid Email Format Required', 'logError')
        return False

    return True 

@app.route('/login', methods=['POST'])
def login():

    if not validLog():
        return redirect('/')

    email = request.form['email']
    password = request.form['password']
    query = "SELECT * FROM user WHERE email = :email LIMIT 1"
    data = { 'email': email }

    user = mysql.query_db(query, data)
    if len(user) < 1:
        flash('Not a registered user!' 'logError')
        return redirect('/')

    if bcrypt.check_password_hash(user[0]['password'], password):
        # flash('Thanks for submitting your information!', 'logError')
        #logging in.
        if not 'loggedIn' in session:
            print 'loggingin'
            session['loggedIn'] = user[0]['id']
            return redirect('/wall')
        else:
            print 'notloggingin'
    else:
        flash('Email or password conflict!', 'logError')
        return redirect('/')

    return redirect('/wall')

@app.route('/registration', methods=['POST'])
def registration():

    if not validReg():
        return redirect('/')

    password = bcrypt.generate_password_hash(request.form['password'])

    query = "INSERT INTO user (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
    data = { 
        'first_name': request.form['first_name'], 
        'last_name': request.form['last_name'], 
        'email': request.form['email'], 
        'password': password 
    }

    user_id = mysql.query_db(query, data)

    if not 'loggedIn' in session:
        session['loggedIn'] = user_id

    return redirect('/wall')

    mysql.query_db(query, data)

    flash('Thanks for submitting your information!')
    return redirect('/wall')

@app.route('/wall')
def successLogin():

    query = 'SELECT first_name, last_name FROM user WHERE id = :id'
    data = {
        'id': session['loggedIn']
    }

    user_data = mysql.query_db(query, data)

    query = "SELECT user.first_name, user.last_name, date_format(message.created_at, '%M %D, %Y') AS created_at, message.message, message.id FROM user JOIN message ON user.id = message.user_id ORDER BY message.id desc"
    messages = mysql.query_db(query)

    query = "SELECT user.first_name, user.last_name, message.id AS message_id, comment.user_id, date_format(comment.created_at, '%M %D, %Y') AS created_at, comment.comment FROM message JOIN comment ON comment.message_id = message.id JOIN user ON comment.user_id = user.id ORDER BY message.id desc, comment.id asc"
    comments = mysql.query_db(query)

    return render_template('wall.html', value=user_data[0], messages=messages, comments=comments)

@app.route('/logout')
def logout():
    session.clear()

    return redirect('/')

@app.route('/message', methods=['POST'])
def messagePost():
    print request.form['messageBody']
    query = "INSERT INTO message (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())"
    data = {
        'user_id': session['loggedIn'],
        'message': request.form['messageBody']
    }
    mysql.query_db(query, data)

    return redirect('/wall')

@app.route('/comment/<message_id>', methods=['POST'])
def commentPost(message_id):
    print message_id
    print session['loggedIn']
    query = "INSERT INTO comment (user_id, message_id, comment, created_at, updated_at) VALUES (:user_id, :message_id, :comment, NOW(), NOW())"
    data = {
        'user_id': session['loggedIn'],
        'message_id': message_id,
        'comment': request.form['commentBody']
    }
    mysql.query_db(query, data)

    return redirect('/wall')


app.run(debug=True)
