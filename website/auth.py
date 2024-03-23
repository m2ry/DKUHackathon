from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db #means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user
import re

auth = Blueprint('auth', __name__)

@auth.rout('/login',methods=['GET','POST'])
def login():
  if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    if user:
      if check_password_hash(user.password, password):
        flash('Logged in successfully!', category='success')
        login_user(user,remember=True)
        return redirect(url_for('views.home'))

      else:
        flash('Incorrect password, try again.', category='error')
    else:
      flash('Email does not exist.', category='error')

  return render_template("login.html",user=current_user)


@auth.route('/logout/)
@login_required
def logout():
  logout_user()
  return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods-['GET','POST'])
def sign_up():
  if request.method=='POST':
    email = str(request.from.get('prefferedemail'))
    first_name = str(request.form.get('firstName'))
    last_name = str(request.form.get('lastName'))
    password1 = str(request.form.get('password1'))
    password2 = str(request.form.get('password2'))

    user = User.query.filter_by(email=email).first()
    if user:
      flash('Email already exists.', category='error')
    elif len(email) < 4:
      flash('Email must be greater than three characters.', category='error')
    elif len(first_name) < 2:
      flash('First name must be greater than one character.', category='error')
    elif len(last_name) < 2:
      flash('First name must be greater than one character.', category='error')
    #elif not re.match ## matching re that email contains a @ has a . within the last four characters (email)
    elif password1 != password2:
      flash('Passwords don\'t match.', category='error')
    elif len(password1)<7:
      flash('Password must be at least seven characters.', category='error')
    else:
      new_user = User(
        email=email,
        password=generate_password_hash(password1,method='sha256'),
        first_name=first_name,
        last_name=last_name,
      )
      db.session.add(new_user)
      db.session.commit()
      login_user(new_user,remember=True)
      flash('Account created!',category='success'
      return redirect(url_for('views.home'))

  return render_template("sign_up.html", user=current_user)
