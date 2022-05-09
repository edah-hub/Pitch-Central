from flask import render_template,request,redirect,url_for,abort
from ..models import User

from . import main
from flask_login import login_required
# from app.models import Pitch


# main = Blueprint('main', __name__)

@main.route('/')
# @main.route('/home')
def index():

  title = "Welcome to Pitch Central"
  # pitches = Pitch.query.all()

  return render_template('index.html', title=title)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

