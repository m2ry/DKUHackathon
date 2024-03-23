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


