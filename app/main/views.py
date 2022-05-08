from flask import render_template 
from . import main
# from app.models import Pitch


# main = Blueprint('main', __name__)

@main.route('/')
# @main.route('/home')
def index():

  title = "Welcome to Pitch Central"
  # pitches = Pitch.query.all()

  return render_template('index.html', title=title)

