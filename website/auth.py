from flask import Blueprint, flash, render_template, request, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
    return render_template("login.html")

@auth.route('/logout')
def login_out():


    return render_template("login.html")



@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        Nickname = request.form.get('Nickname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        if user :
            flash('This user is already exist', category='error')
        elif len(email) < 5:
            flash('Email is to short', category='error')
        elif len(Nickname) < 2:
            flash('Nickname is to short, must be longer than 2', category='error')
        elif password1 != password2:
            flash("Passwrods don't match", category='error')
        elif len(password1) < 10:
            flash('Password msut be more than 10 characters', category='error')
        else:
            # Add user to DB
            new_user = User(email=email,Nickname = Nickname, password = generate_password_hash(password1, method= 'sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
    return render_template("sign_up.html", )


