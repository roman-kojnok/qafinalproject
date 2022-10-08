#!/usr/bin/python
from flask import render_template, request, Blueprint, redirect, abort
from flask_login import current_user, login_user, logout_user, login_required
from main import db
from main.models import User, UserSchema

page = Blueprint('page', __name__, template_folder='templates')
calc = Blueprint('calc', __name__, template_folder='templates')

users_schema = UserSchema(many=True)

bp = Blueprint('main', __name__, template_folder='templates', static_folder='static')


@bp.route('/')
@bp.route('/index')
def hello():
    return render_template('index.html')


@bp.route('/login', methods=['POST', 'GET'])
def login():
    msg = ''
    if current_user.is_authenticated:
        return redirect('/dashboard')
    if request.method == 'POST':
        email = request.form['email']
        user = User.query.filter_by(email=email).first()
        if user is not None and user.is_correct_password(request.form['password']):
            user.authenticated = True
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect('/dashboard')
        msg = "Wrong username or password"
    return render_template('login.html', msg=msg)


@bp.route('/dashboard')
@login_required
def dashboard():
    result = users_schema.dump(User.get_all_users())
    return render_template('dashboard.html', rows=result)


@bp.route('/register', methods=['POST', 'GET'])
def register():
    msg = ''
    if current_user.is_authenticated:
        return redirect('/dashboard')

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if User.query.filter_by(email=email).first():
            msg = 'Email-ID Already Present!'
            # return ('Email-ID Already Present')
        elif not password or not email:
            msg = 'Please fill Email and Password!'
        else:
            user = User(email, password)
            # user.set_password(password)
            db.session.add(user)
            db.session.commit()
            msg = email + ' : You have successfully registered. Redirecting to Login Page...'
            return render_template('register.html', msg=msg), {"Refresh": "3; url=/login"}
    return render_template('register.html', msg=msg)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')


"""@bp.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(e):
    # defining function
    return render_template("404.html")"""


@bp.route('/home')
def home():
    return render_template('home.html')


@bp.route('/terms')
def terms():
    return render_template('page/terms.html')


@bp.route('/privacy')
def privacy():
    return render_template('page/privacy.html')


@bp.route('/FAQ')
def FAQ():
    return render_template('page/FAQ.html')


@bp.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    user = User.query.filter_by(id=id).first()
    if request.method == 'POST':
        if user:
            db.session.delete(user)
            db.session.commit()
            return redirect('/dashboard')
        return abort(404)

    return render_template('delete.html')


@bp.route('/form-update/<int:id>')
def updateForm(id):
    mhs = User.query.filter_by(id=id).first()
    return render_template("form-update.html", data=mhs)


@bp.route('/form-update', methods=['POST'])
def update():
    if request.method == 'POST':
        id = request.form['id']
        email = request.form['email']
        try:
            mhs = User.query.filter_by(id=id).first()
            mhs.email = email
            db.session.commit()
        except Exception as e:
            print("Failed to update data")
            print(e)
        return redirect("/dashboard")
    result = users_schema.dump(User.get_all_users())
    return render_template('dashboard.html', rows=result)
