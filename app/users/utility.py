import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from app import mail


def save_profile_picture(form_picture):
  random_hex = secrets.token_hex(8)
  _, f_ext = os.path.splitext(form_picture.filename)
  picture_fn = random_hex + f_ext
  picture_path = os.path.join(current_app.root_path, 'static/images', picture_fn )
  output_size = (150, 150)
  resized_image = Image.open(form_picture)
  resized_image.thumbnail(output_size)
  resized_image.save(picture_path)
  return picture_fn


def send_reset_email(user):
  token = user.get_reset_token()
  msg = Message('Password Reset Request', sender='noreplaymail84@gmail.com', recipients=[user.email])
  msg.body = f''' We heard that you lost your PitchCapital password. Sorry about that! \n But don’t worry! You can use the following link to reset your password: {url_for('users.reset_token',token=token, _external=True)}

  If you did not make this request then simply ignore this email. 

  This reset link will expire after 30 mins
  '''
  mail.send(msg)

def send_welcome_email(user_email):
  msg = Message('Welcome to PitchCapital', sender='noreplaymail84@gmail.com', recipients=[user_email])
  msg.body = ''' Welcome to PitchCapital! An important skill for those looking to build their career is learning to effectively sell oneself and the value they have to offer. PitchCapital will allow you to build this skill by exposing you to a variety of insightful pitches from other users from across the globe. \n Get started by posting your first pitch today.
  '''
  mail.send(msg)
