from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField
from wtforms.validators import DataRequired
from app.models import Comment

class PitchForm(FlaskForm):
  title = StringField('Title', validators=[DataRequired()])
  content = TextAreaField('Content', validators=[DataRequired()])
  category = RadioField('Category',  choices=[('pickuplines','pickuplines'), ('elevatorpitch','elevatorpitch') ,('productpitch','productpitch'), ('randompitch','randompitch')], validators=[DataRequired()])
  submit = SubmitField('Post')

class CommentForm(FlaskForm):
	content = TextAreaField('Add comment', validators=[DataRequired()])
	submit = SubmitField('Post')
