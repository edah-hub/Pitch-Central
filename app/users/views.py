from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, current_user, logout_user, login_required
from app import db, bcrypt
from app.models import User, Pitch
from app.users.forms import RegistrationForm, LoginForm, UpdateAccountForm, RequestResetForm, ResetPasswordForm
from app.users.utlis import save_profile_picture, send_reset_email, send_welcome_email

users = Blueprint('users', __name__)

@users.route('/register', methods=['GET', 'POST'])
def register():
  if current_user.is_authenticated:
    return redirect(url_for('main.index'))
  form = RegistrationForm()
  if form.validate_on_submit():
    hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = User(username=form.username.data, email = form.email.data, password = hashed_password)
    db.session.add(user)
    db.session.commit()
    user_email = user.email
    send_welcome_email(user_email)

    flash(f'Hello { form.username.data}, Your Account was created succesfully! You are now able to log in', 'success')
    return redirect(url_for('users.login'))
  return render_template('register.html', title='Register', form=form)

@users.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('main.index'))
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
      login_user(user, remember=form.remember.data)
      next_page = request.args.get('next')
      return redirect(next_page) if next_page else redirect(url_for('main.index'))   
    else:
      flash('Login Unsuccessful. Please check email and password', 'danger')

  return render_template('login.html', title='Login', form=form)

@users.route('/logout')
def logout():
  logout_user()
  return redirect (url_for('main.index'))

@users.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
  if current_user.is_authenticated:
    return redirect(url_for('main.index'))
  form = RequestResetForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    send_reset_email(user)
    flash('Check your email for a link to reset your password.', 'info')
    return redirect(url_for('users.login'))
  return render_template('reset_request.html', title='Reset Password', form=form)

@users.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_token(token): 
  if current_user.is_authenticated:
    return redirect(url_for('main.index'))
  user = User.verify_reset_token(token)
  if user is None:
    flash('The reset token has either expired or is invalid', 'warning')
    return redirect(url_for('users.reset_request'))
  form = ResetPasswordForm()
  if form.validate_on_submit():
    hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user.password = hashed_password
    db.session.commit()
    flash('Your password has been updated! You can now login to your account', 'success')
    return redirect(url_for('users.login'))
  return render_template('reset_token.html', title='Reset Password', form=form)

@users.route('/user/<string:username>')
def user_account(username):
  user = User.query.filter_by(username=username).first_or_404()
  pitches = Pitch.query.filter_by(author=user).order_by(Pitch.pub_date.desc())
  image_file= url_for('static', filename=f'images/{user.image_file}')
  return render_template('profile.html', pitches=pitches, user=user, image_file=image_file,)

@users.route('/update_account', methods=['GET', 'POST'])
@login_required
def update_account():
  form = UpdateAccountForm()
  if form.validate_on_submit():
    if form.picture.data:
      picture_file =  save_profile_picture(form.picture.data)
      current_user.image_file = picture_file
    current_user.username = form.username.data
    current_user.email = form.email.data
    db.session.commit()
    flash('Your account information has been updated!', 'success')
    return redirect(url_for('users.update_account'))
  elif request.method == 'GET':
    form.username.data = current_user.username
    form.email.data = current_user.email
  image_file= url_for('static', filename=f'images/{current_user.image_file}')
  return render_template('update_account.html', title='Account', image_file=image_file, form=form)


